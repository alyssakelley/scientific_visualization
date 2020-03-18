# scientific_visualization

This movie was created by Alyssa Kelley and Anne Glickenhaus as our final project for our scientific visualization course at the University of Oregon in Winter 2020.

## Summary of our work:

We used the aneurysm data set to produce a movie demonstrating the blood flow when an aneurysm in occuring. Our movie goes through the visuals for an affected blood vessel in the human body to demonstrate the pressure as a contour rendering, velocity as a contour rendering, pressure and velocity combined as contour renderings, volume and pressure combined as a volume rendering, and volume, pressure and velocity all together as a volume rendering. We thought it would be beneficial to see the different rendering representations so the viewer can visualize how a slice of the data looks compared to the blood vessel’s volume, which is more intuitive. We created these visuals using the Visit Visualization tool and python scripting to create many images, and then combine all of the images together to create a movie, which we then edited using iMovie. 

Aneurysm Dataset can be accessed [here](http://www.visitusers.org/index.php?title=Tutorial_Data)

Youtube Video Link to view our final movie:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=CgNcGBo7pfs
" target="_blank"><img src="http://img.youtube.com/vi/CgNcGBo7pfs/0.jpg" 
alt="Youtube Video Link" width="240" height="180" border="10" /></a>


## Script Summaries and How to Run Each:

### pressure.py
This script demonstrates the pressure of the affected blood vessel as a contour rendering of the data. We maintained
consistency of our window rendering by having this script access our pressure.session file. To run this script, you 
will need to change the "path_to_aneurysm_data" filepath variable at the top of the file to where your data is on your
machine. Once your add your filepath in, you will need to open Visit, go to the Controls, and click "Launch CLI",
this will then open a terminal window on your screen. You will need to open an addition terminal window, go to the directory
on your machine with the scripts present, and run the following command:

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pressure.py

This command is also listed at the top of the script file as a comment. Once you run the script, Visit will pop up a white
window. You will need to go back to the terminal window in which you ran that command, and call main(). This should then
have the rendering start in the Visit window. The window will close after the rendering is complete. 

### velocity.py

This script demonstrates the velocity of the affected blood vessel as a contour rendering of the data. We maintained
consistency of our window rendering by having this script access our velocity.session file. To run this script, you 
will need to change the "path_to_aneurysm_data" filepath variable at the top of the file to where your data is on your
machine. Once your add your filepath in, you will need to open Visit, go to the Controls, and click "Launch CLI",
this will then open a terminal window on your screen. You will need to open an addition terminal window, go to the directory
on your machine with the scripts present, and run the following command:

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s velocity.py

This command is also listed at the top of the script file as a comment. Once you run the script, Visit will pop up a white
window. You will need to go back to the terminal window in which you ran that command, and call main(). This should then
have the rendering start in the Visit window. The window will close after the rendering is complete. 


### velocity_and_pressure.py

This script demonstrates the velocity and pressure of the affected blood vessel as a contour rendering of the data. We maintained
consistency of our window rendering by having this script access our velocity_and_pressure.session file. To run this script, you 
will need to change the "path_to_aneurysm_data" filepath variable at the top of the file to where your data is on your
machine. Once your add your filepath in, you will need to open Visit, go to the Controls, and click "Launch CLI",
this will then open a terminal window on your screen. You will need to open an addition terminal window, go to the directory
on your machine with the scripts present, and run the following command:

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s velocity_and_pressure.py

This command is also listed at the top of the script file as a comment. Once you run the script, Visit will pop up a white
window. You will need to go back to the terminal window in which you ran that command, and call main(). This should then
have the rendering start in the Visit window. The window will close after the rendering is complete. 


### volume_pressure.py

This script demonstrates the volume and pressure of the affected blood vessel as a volume rendering of the data. We maintained
consistency of our window rendering by having this script access our velocity_pressure.session file. To run this script, you 
will need to change the "path_to_aneurysm_data" filepath variable at the top of the file to where your data is on your
machine. Once your add your filepath in, you will need to open Visit, go to the Controls, and click "Launch CLI",
this will then open a terminal window on your screen. You will need to open an addition terminal window, go to the directory
on your machine with the scripts present, and run the following command:

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s volume_pressure.py

This command is also listed at the top of the script file as a comment. Once you run the script, Visit will pop up a white
window. You will need to go back to the terminal window in which you ran that command, and call main(). This should then
have the rendering start in the Visit window. The window will close after the rendering is complete. 


### vpandv.py

This script demonstrates the volume, pressure and velocity of the affected blood vessel as a volume rendering of the data. We maintained
consistency of our window rendering by having this script access our vpandv.session file. To run this script, you 
will need to change the "path_to_aneurysm_data" filepath variable at the top of the file to where your data is on your
machine. Once your add your filepath in, you will need to open Visit, go to the Controls, and click "Launch CLI",
this will then open a terminal window on your screen. You will need to open an addition terminal window, go to the directory
on your machine with the scripts present, and run the following command:

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s vpandv.py

This command is also listed at the top of the script file as a comment. Once you run the script, Visit will pop up a white
window. You will need to go back to the terminal window in which you ran that command, and call main(). This should then
have the rendering start in the Visit window. The window will close after the rendering is complete. 

