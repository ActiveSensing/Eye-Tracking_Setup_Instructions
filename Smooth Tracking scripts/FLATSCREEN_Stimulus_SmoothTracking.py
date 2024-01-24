import pandas as pd
import os
from sys import path
path.append(r'C:\Users\fenklab\Desktop\super_bowl_screen-main\Software') #path to the superbowl scripts
from bowl_stimulate_class import *

stim = Stimulation_Pipeline(is_flat_screen = True, xfov = 90)
log = stim.LoopScenes(arena = stim,
                      bouncing_limits = 60, side_duration = 3.0, side_per_scene = 4, break_duration =1.0, framerate = 60, iteration = 20,
                      scenes = [
                          [
                              "Black Bar on Cheker", #name of the scene
                              stim.bar_vertical(width=15, color=0, color_b=-1), #generate foreground picture
                              stim.checker_screen(pixel_size=10, color1=0, color2=80), #generate background picture
                              lambda f, b, s : (stim.Superpose(foreground = f, background = b, shift = s)) #function to adapt the foreground and background with an update angular shift
                              ],
                          [
                              "Black Bar on White", #name of the scene
                              stim.bar_vertical(width=30, color=0, color_b=125),
                              None, #the background should always be specified but can be None
                              lambda f, b, s : (stim.Superpose(foreground = f, background = b, shift = s))
                              ],
                          [
                              "Grating", #name of the scene
                              stim.grating_vertical(color1 = 255, color2 = 0, spatial_freq = 15),
                              None, #the background should always be specified but can be None
                              lambda f, b, s : (stim.Superpose(foreground = f, background = b, shift = s))
                              ],
                          [ # convergent and divergent scenes can be done by a background mirroring the foreground
                              "Convergent Grating", #name of the scene
                              stim.grating_vertical(color1 = 255, color2 = 0, spatial_freq = 15),
                              None,
                              lambda f, b, s : (stim.Superpose(foreground = f, shift = s, mask = stim.half_screen, background = stim.Superpose(foreground = f, shift = -s)))
                              ]
                          ])

output_directory_path = r"C:\Users\fenklab\Desktop\New folder"
flyID = "TEST"

# Extract flyUD and directroy path when script launched by EyeTracker
#if len(sys.argv) > 1:
#    output_directory_path = sys.argv[1]
#    flyID = sys.argv[2]

log.to_csv(os.path.join(output_directory_path, flyID + "_" + 'stimulus_log.csv'), index=False)

cv2.destroyAllWindows()
key = cv2.waitKey(1)