Assignment-1 Part-1: 2D Isocontour Extraction using VTK

The Python script extracts 2D Isocontours from the Isabel_2D scalar dataset.
Here we are traversing each cell counter-clockwise and then counting the number
of intersections; if it exceeds or is less than 2, we skip the cell, and if it is 2 we perform Linear interpolation on it.

The output is written as a VTP file and can be visualized using ParaView.

Files:

-> Isabel_2D.vti : The 2D scalar dataset from which isocontours are extracted.
-> Isocontour.py : Our Python script for extracting and writing the isocontour.

Dependencies Used:

-> Python 3
-> VTK library : For reading/writing VTK formats and managing geometry.
Note: Run "pip install vtk" in your terminal/CMD to install the VTK module.

How to run the code:

The Python script is interactive.
It asks the user to enter the following inputs:

-> Path to Isabel_2D.vti : The path of the input 2D scalar dataset in your local(without quotes).
-> Output VTP filename   : The name of the output file (e.g., output.vtp).
-> Isovalue              : A float value representing the scalar threshold to extract the contour.

TERMINAL PROMPT ->
python3 Isocontour.py

Note:
->The output.vtp file will be created in the directory in which you have the Isocontour.py
