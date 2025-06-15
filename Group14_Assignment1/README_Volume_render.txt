Assignment-1 Part-2 Volume Rendering using VTK

The Python script performs Volume Rendering on the Isabel_3D Scalar Dataset using VTK.
It allows the user to choose whether to enable Phong shading or not by responding to
a prompt.It then performs volume rendering and displays the result in a 1000x1000 window.

Files Provided:

-> Isabel_3D.vti    : The 3D volume data on which volume rendering has been performed.
-> Volume_render.py : Our Python script for Volume Rendering.
-> README.txt       : This README file which illustrates how to execute the Volume_render.py file.

Dependencies Used:

-> Python 3
-> VTK library : To perform Volume Rendering.
Note: Run "pip install vtk" on your terminal/CMD to install the VTK module.

How to run the code:

The script is now interactive and no longer requires command-line arguments.
It will prompt the user to:
-> Enable/disable Phong shading (by typing 'on' or 'off')
-> Enter the path to the .vti dataset

TERMINAL PROMPT ->
python3 Volume_render.py

EXAMPLE INTERACTION →

Enable shading? Type 'on' or 'off': on
Enter path to .vti dataset (e.g. Isabel_3D.vti): Isabel_3D.vti