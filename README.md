## Required Parts

<b>Thorlabs</b>:
- 1 Dovetail Rail Carrier <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=RC1">RC1</a>
- 1 Dovetail Optical Rail <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=RLA075/M">RLA075/M</a>
- 1 Adjustable Flip Platform <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=FP90/M">FP90/M</a>
- 1 Optical Post TR../M (of the appropriate length. e.g. <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=TR20/M">TR20/M</a>)
- 1 Post Holder PH../M (of the appropriate length. e.g. <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=PH20/M">PH20/M</a>)
- (optional) 1 Swivel Base Adapter <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=UPHA">UPHA</a>
- (optional) 1 Ø12.5 mm Bandpass Filter (Of the approriate filtering range e.g. <a href="https://www.thorlabs.de/thorproduct.cfm?partnumber=FBH05850-10">FBH05850-10 - Hard-Coated</a> for a DPP light of 850nm.

<b>Others suppliers</b>:
- Teledyne's Chameleon3 Camera, model: <a href="https://www.teledynevisionsolutions.com/en-150/products/chameleon3-usb3/?model=CM3-U3-13Y3M-CS&vertical=machine%20vision&segment=iis">CM3-U3-13Y3M-CS</a>
- InfiniStix Lens, model <a href="https://www.edmundoptics.de/p/infinistix-3x-44mm-wd-video-lens/3413/">3X 44mm WD</a>
- Macromanipulator LD40-LM (cheap, Constructor unknown but available on many website)

<b>Homemade Parts</b>:
- One 3D print of all stl files <a href="https://github.com/ActiveSensing/Eye-Tracking_Setup_Instructions/tree/main/Eye%20Camera%20Building%20Instructions/3D%20Printed%20and%20Manufactured%20Parts">here</a>, preferably using an ABS-R black filament

<b>Screws</b>:
- M6 of 10 mm
- M4 of 8mm and 10mm
- M3 of 10mm and 20mm
  
## Assemble Parts

<p align="center"><img src="ReadMe_Ref/SpinnakerInstallationProfile.png" width="210" height="297"></p>

1. Use 4 <b>M3 screws (10mm)</b> to screw the <b>camera</b> onto the flat side of the the <b>CasedRailMicromanipulatorAdaptor</b> 3D-print.

2. Use 1 <b>M6 screw (10mm)</b> to screw the <b>Dovetail Rail Carrier RC1</b> onto the <b>CasedRailMicromanipulatorAdaptor.</b>
    - $\color{red}{\textrm{Make sure that the RC1's thumb screw will face the user.}}$
    - $\color{red}{\textrm{Make sure that the camera cable will point in the most convinient direction within the setup.}}$

3. Use 1 <b>M4 screws (8mm)</b> to screw the <b>Dovetail Rail RLA075/M</b> onto the <b>CasedRailMicromanipulatorAdaptor</b>.
    - $\color{red}{\textrm{Make sure that the base of the Rail lies on the base of the CasedRailMicromanipulatorAdaptor, so the Rail Carrier can attach on top.}}$

4. Use 4 <b>M3 screws (10mm)</b> to screw the <b>CasedRailMicromanipulatorAdaptor</b> onto the top platform of the <b>macromaniplator LD40-LM</b>.
    - $\color{red}{\textrm{Orient the CasedRailMicromanipulatorAdaptor to make sure that the rail will point in the opposite direction than the fly.}}$
    - $\color{red}{\textrm{Orient the macromanipulator to make sure that all knobs will be easily accessible by the user.}}$
    - $\color{red}{\textrm{Depending on which platform of the macromanipulator is the top one, the caps of the screws will be either top or down.}}$

5. Use 4 <b>M4 screws (10mm)</b> to screw the <b>Adjustable Flip Platform FP90/M</b> onto the flatter side of the <b>MicromanipulatorPlatformAdaptor</b>.

6. Use 4 <b>M3 screws (10mm)</b> to screw the <b>MicromanipulatorPlatformAdaptor</b> onto the base platform of the <b>macromaniplator LD40-LM</b>.
    - $\color{red}{\textrm{Make sure that the locking screw of the Adjustable Flip Platform will face the user}}$
    - $\color{red}{\textrm{Make sure that that locking screw will be opposite direction of the fly (so the structure can tilt away from the fly)}}$

7. Use 2 <b>M4 screws (10mm)</b> to screw the <b>postFixer</b> onto the <b>Adjustable Flip Platform FP90/M</b>.

8. Use 1 <b>M3 screws (20mm)</b> to fix the <b>Optical Post</b> onto the <b>postFixer</b>.

9. Fix the <b>Post Holder</b> onto the Setup (More stable if using the optional <b>Swivel Base Adapter</b>).
    - $\color{red}{\textrm{The thumb screw of the Post Holder should face the user}}$

10. Fix the <b>Optical Post</b> into the <b>Post Holder</b>.

11. Fix the <b>Dovetail Rail Carrrier RC1</b> onto the <b>Dovetail Rail RLA075/M</b>.

12. Attach the <b>InfiniStix Lens</b> onto the <b>camera</b>
13. Insert the optional <b>Bandpass filter</b> into the <b>InfiniStix Lens</b> and secure it with the InfiniStix_FilterHolder.stl
