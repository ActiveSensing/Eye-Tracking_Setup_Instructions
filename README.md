<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- TRACKING THE BALL -->
## Tracking the ball

### Install visual studio Community
1. Download visual studio Community from  from <a href="https://visualstudio.microsoft.com/free-developer-offers/">here</a>
2. During the installation process, make sure to include <i>Desktop development with C++</i> and <i>.NET desktop development</i>
   <img src="ReadMe_Ref/VisualStudioWorkloadsStep.png" width="630" height="450">
  

### Install spinnaker SDK
1. $\color{red}{\textrm{Install Spinnaker SDK 2.7.0.128 ☠️☠️☠️ because Fictrac might be incompatible with newest Spinnaker SDK}}$
  <a href="https://www.flir.com/support-center/iis/machine-vision/downloads/spinnaker-sdk-download/spinnaker-sdk--download-files/">Here</a>
2. Unzip and run SpinnakerSDK_FULL_2.7.0.128_x64.exe
  1. Check the box “Application Development”</p>
    <img src="ReadMe_Ref/SpinnakerInstallationProfile.png" width="210" height="280">
  2. Uncheck the box “I will use GigE Cameras”</p>
      <img src="ReadMe_Ref/SpinnakerGigEInterfaces.png" width="210" height="280">
  3. Install to
       ```
       C:\Program Files\FLIR Systems\Spinnaker
       ```
### Install FicTrac
1. Follow the instructions on <a href="https://github.com/rjdmoore/fictrac">Fictrac official page</a> OR assuming you are using windows 10 and we will work with FLIR cameras, do as follow:
  1. Install the Windows x64 version of <a href="https://git-scm.com/download/win">Git</a>
  2. Type “Developer Command Prompt” in the Window Search Bar and open the app “Developer Command Prompt for VS 2022” as an administrator
  3. To install and setup vcpkg, write:
     
     1.
         ```
         cd C:\Users\[your user folder]
         ```
     2.
         ```
         git clone https://github.com/microsoft/vcpkg
         ```
     3.
         ```
         .\vcpkg\bootstrap-vcpkg.bat
         ```
     4.
         ```
         .\vcpkg\vcpkg integrate install
         ```
     5. This might take a LOT of time, DO NOT PANIC
         ``` 
        .\vcpkg\vcpkg install opencv[ffmpeg]:x64-windows nlopt:x64-windows boost-asio:x64-windows ffmpeg[x264]:x64-windows
         ```
     6. This will install all the FicTrac files in your user folder
         ```
         git clone https://github.com/rjdmoore/fictrac.git
         ```
      
  4. Keep the command prompt window open
  5. Our setup requires some modification on Fictrac in order to send its output to a public memory on your computer (later used by the close-loop stimulus software).
     1. Download our <a href="https://drive.google.com/drive/folders/1S8Fbw5yJJ7K2ZgSIMgYnA-w1dTtG_ro4?usp=share_link">modified files</a> 
     2. Replace SocketRecorder.cpp in
          ```
          C:\Users\[your user folder]\fictrac\src\
          ```
     3. Replace SocketRecorder.h in
          ```
          C:\Users\[your user folder]\fictrac\include\
          ```
  6. Reopen the “Developer Command Prompt for VS 2022” window and write:
     
     1. 
         ```
         cd fictrac
         ```
     2. 
         ```
         mkdir build
         ```
     3. 
         ```
         cd build
         ```
     4. This will generate compilation files for FicTrac in the newly created “build” folder. Therefore we mention the path to the vcpkg, the fact that we are going to use USB3 cameras, and the path to spinnakerSDK
         ```
         cmake -A x64 -D CMAKE_TOOLCHAIN_FILE="C:\Users\[your user folder]\vcpkg\scripts/buildsystems/vcpkg.cmake" -D PGR_USB3=ON -D PGR_DIR="C:\Program Files\FLIR Systems\Spinnaker" ..
         ```
     5. 
         ```
         cmake --build . --config Release -j 4
         ```

  7. Close the “Developer Command Prompt for VS 2022”


### Use FicTrac
1. Make sure the camera looking at the ball is plugged to the computer
2. Configure FicTrac
  1. Create a new folder for your Fictrac project on the Desktop
  2. In this folder, paste <a href="https://drive.google.com/drive/folders/1S8Fbw5yJJ7K2ZgSIMgYnA-w1dTtG_ro4?usp=share_link">this config.txt file</a>

     1. All the parameters (except the modified sock_port) in the config.txt are explained <a href="https://github.com/rjdmoore/fictrac/blob/master/doc/params.m">in the fictrac's official documentation</a>
     
     2. In our specific setup, following parameters are important:
       1. Src_fn :  0 	# Mention which FLIR camera should be used. The camera that was first plugged into the computer is ‘0’, next ‘1’, …
      
       2. c2a_r : { 0, 4.712388, 0} 	# Align the fly in front of the camera
      
       3. vfov : 2.9		# Set the correct lens’ vertical field of view
      
       4. sock_port  : 2305	#Send the tracking output to a shared memory slot with the name “2305” (handled by our customised SocketRecorder files) !!! ONLY FOR CLOSED LOOP EXPERIMENTS, OTHERWISE REMOVE THIS LINE !!!
      
       5. Might want to adjust the thr_ratio and thr_win_pc parameters according to your stained ball

3. In a command prompt write:
   
    1.
       ```
       cd [Path to your FicTrac project]
       ```
    2.
       ```
       C:\Users\[your user folder]\fictrac\bin\Release\configGui.exe config.txt
       ```
       This will run the GUI interface to help visually setting up some FicTrac parameters from the config.txt file
       
       1. In the configGUI interface, you should see an image with a blue circle on it. If the view is from a wrong camera, change the Src_fn parameter in the config.txt file
          
       3. In the command prompt, write ‘n’ to modify the ball’s outline
          - In the GUI window, click three random points at the horizon of the ball, then press enter (right click undo your previous points)</p>
            <img src="ReadMe_Ref/FicTracGUIROI.png" width="350" height="290">
       4. Back in the command prompt, press n to modify the masked area (the part of the balls hidden by the ball holder and by the fly itself)
          - For each area click the corner of the shape you want to mask from the tracking, then press enter. When all the masked areas are defined, press enter again.</p>
            <img src="ReadMe_Ref/FicTracGUIMask.png" width="350" height="290">
       5. Back in the command prompt, press “y” to NOT MODIFY THE POSITION OF THE FLY since it is already set in the config file perfectly at the top of the ball and looking forward

1. Run FicTrac
  - In a command prompt write:

    1.
        ```
        cd [Path to your FicTrac project]
        ```
    2.
        ```
        C:\Users\[your user folder]\fictrac\bin\Release\fictrac.exe config.txt
        ```

  - TIPS:
    1. Once in a while, You might want to restart the GUI config in order to readjust the ball’s outline and masked areas. Because the camera position and lighting of the setup might have slightly changed
    2. In a text file inside your FicTrac project folder, save the command lines used previously. Next time you use Fictrac, you could just copy paste them in the command prompt.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
