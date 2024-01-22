import pandas as pd
import os
from sys import path
path.append(r'C:\Users\fenklab\Desktop\super_bowl_screen-main\Software')
from bowl_stimulate_class import *

print(sys.argv)
if len(sys.argv) < 3:
    print("Usage: script.py <variable1> <variable2>")

# Extract command-line arguments
output_directory_path = " ".join(sys.argv[1:-1])
flyID = sys.argv[-1]

Arena = Stimulation_Pipeline()
log = Arena.generateLoop(arena = Arena,
                         bouncing_limits = 60, side_duration = 3.0, side_per_phase = 4, break_duration =1.0, framerate = 60, iteration = 20, inverted=True, rot_offset=(0,50,0),
                         objects_and_backgrounds = [ lambda:
                                                    ([Arena.generate_bar_vertical(width=30, color=0, color_b=125),
                                                      Arena.generate_colored_screen(color=80)]),
                                                    
                                                    lambda:
                                                    ([Arena.generate_checker_vertical(pixel_size =15, width_in_pixels=2, color1=0, color2=80, color_b=-1),
                                                    Arena.generate_checker_screen(pixel_size=15, color1=0, color2=80)]),

                                                    lambda:
                                                    ([Arena.generate_bar_vertical(width=30, color=0, color_b=-1),
                                                      Arena.generate_checker_screen(pixel_size=15, color1=0, color2=80)]),
                                                    
                                                    lambda:
                                                    ([Arena.generate_checker_screen(pixel_size=15, color1=0, color2=80),
                                                      Arena.generate_colored_screen(color=80)])
                                                   ])

if len(sys.argv) < 0:
    log.to_csv(os.path.join(output_directory_path, flyID + "_" + 'stimulus_log.csv'), index=False)

cv2.destroyAllWindows()
key = cv2.waitKey(1)