CS661 - Assignment-2
Group Members: Aryamann Srivastava ,Kshitiz Tyagi, Tejas Shrivastava
	

Description:

This Jupyter Notebook provides an interactive visualization of a 3D scalar volume using:

- Plotly for 3D isosurface and histogram plots
- ipywidgets for slider and reset button
- VTK for loading the .vti volume data

The isosurface updates dynamically with the slider value.
The histogram shows values in the range [isovalue - 0.25, isovalue + 0.25].
Clicking the reset button resets everything to the initial state.


Files Included:

1. Assignment-2.ipynb     → Main notebook
2. README.txt             → This file


How to Run:

1. Put the unique file path of the 'mixture.vti' dataset in your local.
2. Run the notebook in Jupyter Notebook.
3. Make sure these packages are installed:

   - vtk
   - plotly
   - ipywidgets

To install them:-   pip install vtk plotly ipywidgets

4. Run all cells. The interface will show:
   [  Isovalue Slider   |   Reset Button ]
   [  Isosurface Plot   |   Histogram  ]


Note:

- Plotly `FigureWidget` is used so the plots remain visible when the slider is changed.
- The colormap used is 'plasma' as specified in the assignment.
- Histogram bars are colored blue for visibility.


