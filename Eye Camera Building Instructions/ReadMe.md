# Set up Arduino
  1. If the Tools_FenkLab Repository is not yet copy on your Desktop, open <a href="https://code.visualstudio.com/download">Visual Studio Code</a> and <a href="https://code.visualstudio.com/docs/sourcecontrol/intro-to-git">set up Git and clone</a> this repository in your Desktop location.
       ```
       https://github.com/ActiveSensing/Tools_Fenklab.git
       ```
        
  2. Plug the Arduino Board to the computer.
  3. Install <a href="https://www.arduino.cc/en/software">Arduino IDE</a>.
  4. In the Arduino IDE, open the file <i>ArduinoProgram.ino</i> located in <i>C:\Users\[your user folder]\Desktop\Tools_Fenklab\Arduino_Python_Controls\ArduinoProgram</i>.
  5. Select the connected Arduino Board in the dropdown list of connected devices (1) then press the upload button (2). Once the upload is over, you can close Arduino IDE.
    <p align="center">
      <img src="ReadMe_Ref/SelectBoardAndUpload.png" width="420" height="130">
    </p>
    
# ArduinoControl_class.py
- The <b>ArduinoControl_class.py</b> script in <i>C:\Users\[your user folder]\Desktop\Tools_Fenklab\Arduino_Python_Controls</i> is a python tool to communicate with the <b>ArduinoProgram.ino</b> running on the Arduino.
<br />

## RecordOptoLogs_FromEyeTracker.py
- the <b>RecordOptoLogs_FromEyeTracker.py</b> script in <i>C:\Users\[your user folder]\Desktop\Tools_Fenklab\Arduino_Python_Controls</i> is an exemple script demonstrating how to use the tool <b>ArduinoControl_class.py</b>.
- The aim of this exemple script is to stimulate the fly with an optogenetic LED cycling between on and off, and to save the exact times these LED changes occured.

- Open Visual Studio, press Ctrl + ` to open the Terminal and paste these lines to download the needed python libraries

        pip install opencv-python
        pip install numpy
        pip install pandas
        pip install pyserial

  
- In Visual Studio Code, open the <b>RecordOptoLogs_FromEyeTracker.py</b> script and have a look at it.
  - This first part loads the needed libraries, but most importantly, it imports everything present in the <i>OptoControl_class.py</i>
  
  $\color{red}{\textrm{Remember to change that path if your user account is not fenklab}}$

            import mmap
            import os
            import  sys
            import numpy as np
            import cv2
            sys.path.append(r"C:\Users\fenklab\Desktop\Tools_Fenklab\Arduino_Python_Controls")
            from ArduinoControl_class import *
  
  - This part allows some variables to be set automatically when the code is run directly through EyeTracker or any command line window. Otherwise, these variable will get customed default values.
        - When a python script is run through Eyetracker, all the parameters from the Eyetracker's experiment are passed to the script, even those you add as comments (as long as they were formated as "Paramater_Name|Paramater_Value").
        - In this exemple, "OptoOn|5" and "OptoOff|7" were added in the experiment's comments in Eyetracker. 
 
    $\color{red}{\textrm{If not run from EyeTracker, the variables will take default values (second parameter in get(...))}}$
    
            # Looks for cmd run parameters (sent when launched by EyeTracker)
            EyeTracker_param = {}
            for item in sys.argv:
                if '|' in item:
                    key, value = item.split('|', 1)  # expect parameters to be formated as "key|value"
                    EyeTracker_param[key.strip()] = value.strip()  # Strip any surrounding spaces
            
            #Extracts the parameters or gives them a default value
            flyID = EyeTracker_param.get('FlyID', "DefaultFlyID")  
            output_directory_path = EyeTracker_param.get('OutputPath', r"C:\Users\fenklab\Desktop")
            Opto_on_duration = float(EyeTracker_param.get('OptoOn', 3.)) #the duration (s) the Opto LED should be on every on/off cycle
            Opto_off_duration = float(EyeTracker_param.get('OptoOff', 0.01)) #the duration (s) the Opto LED should be off every on/off cycle

  - This line instantiates the communication with the Arduino and takes some parameters: To which usb port is the Arduino connected (1), and wheter or not we want to print everything that is being sent between the Arduino and the OptoControl_class (2).

          arduino = ArduinoControl(port='COM3', debug = True)

  - This line starts an <b>unsynchronised thread</b> that listens to the Arduino.

          opto.Start()

  - First we turn off the opto LED before the experiment. Then we ask the arduino to communciate all futture changes in the LED state 

          arduino.set_opto_static_state(on = False) #Make sure the Opto LED is Off at the beginning of the experiment
          arduino.register_to_Arduino_opto_logs() #Ask the Arduino to send messages everytime it turns its Opto LED On or Off

    
  - This part creates a window that displays the text "Waiting for Opto".

          # Create a window
          window_name = 'Recording Opto'
          cv2.namedWindow(window_name)
          screen = np.zeros((480, 600, 3), dtype=np.uint8)
          cv2.putText(screen, 'Waiting for Opto', (10,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
 
  - This part sends a ping request to the Arduino and passes the GetPing function as a callback. This means that GetPing() will be called whenever the ping request is answered by the Arduino. Once called, GetPing() will change the window's text to "Recording Opto",  and will ask the Arduino to make the Opto LED state loop between On and Off with specific durations. 

          # Change the window's text when the Arduino responds to Ping
          def GetPing():
              global screen
              screen = np.zeros((480, 600, 3), dtype=np.uint8)
              cv2.putText(screen, 'Recording Opto', (10,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
              arduino.set_opto_cycle(on_duration = Opto_on_duration, off_duration = Opto_off_duration)  #Start the Opto LED On/Off cycle
          arduino.ping(lambda s: GetPing())
          
  - This part keeps the window visible until the ESC key is pressed or until the EyeTracking recording is over.
 
    $\color{green}{\textrm{The sole purpose of this part is to keep the script running for the desired time. You can replace it by a simple timer or a stimulus display for exemple.}}$
    
          # Change the current window
          # Display the current window
          while True:
              key = cv2.waitKey(1) # Wait for 1 ms for a key event
              cv2.imshow(window_name, screen)
              
              if bool(EyeTracker_param):
                  with mmap.mmap(-1, 1024, "EyeTracker") as mm:
                      line = mm.readline().decode().strip()
                      if "Recording_Stopped" in line: #Exit if EyeTrackerRecording is Over
                          break
          
              if key == 27:  # Exit if the ESC key (ID: 27) is pressed
                  break
          cv2.destroyAllWindows()
    
  - This last part closes the communication with the Arduino and saves all the logs into a <i>.csv</i> file.

          arduino.Close() #VERY IMPORTANT to run this line at the end (kill the infinite thread listening to Arduino and free the Arduino USB connection)
          Optologs = arduino.GetLogs() #Get the recorded On and Off events
          Optologs.to_csv(os.path.join(output_directory_path, flyID + "_" + 'opto_log.csv'), index=False)
    

<br />

