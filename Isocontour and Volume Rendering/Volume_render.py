#importing vtk library 
import vtk
def main():
    #Prompting user to enter shading input and dataset path
    shading_input=input("Enable shading? Type 'on' or 'off':").strip().lower()
    while shading_input not in ['on','off']:
        shading_input=input("Invalid input. Please type 'on' or 'off':").strip().lower()
    shading=shading_input=='on'
    dataset_path=input("Enter path to .vti dataset (e.g. Isabel_3D.vti):").strip()

    #Reading the scaler data from Isabel_3D.vti
    reader=vtk.vtkXMLImageDataReader()
    reader.SetFileName(dataset_path)
    reader.Update()
    data=reader.GetOutput()

    #Creating the colour transfer function
    colour = vtk.vtkColorTransferFunction()
    colour.AddRGBPoint(-4931.54, 0.0, 1.0, 1.0)
    colour.AddRGBPoint(-2508.95, 0.0, 0.0, 1.0)
    colour.AddRGBPoint(-1873.9,  0.0, 0.0, 0.5)
    colour.AddRGBPoint(-1027.16, 1.0, 0.0, 0.0)
    colour.AddRGBPoint(-298.031, 1.0, 0.4, 0.0)
    colour.AddRGBPoint(2594.97,  1.0, 1.0, 0.0)

    #Creating the opacity transfer function
    opacity=vtk.vtkPiecewiseFunction()
    opacity.AddPoint(-4931.54, 1.0)
    opacity.AddPoint(101.815,  0.002)
    opacity.AddPoint(2594.97,  0.0)

    #Calculating the volume properties
    volume_property = vtk.vtkVolumeProperty()
    volume_property.SetColor(colour)
    volume_property.SetScalarOpacity(opacity)
    volume_property.SetInterpolationTypeToLinear()

    #This condition will be true if user has requested for shading
    if shading:
        volume_property.ShadeOn()
        volume_property.SetAmbient(0.5)
        volume_property.SetDiffuse(0.5)
        volume_property.SetSpecular(0.5)
    else:#If user has not requested for shading then it will be turned off
        volume_property.ShadeOff()

    #Creating the volume mapper and setting its input data
    mapper=vtk.vtkSmartVolumeMapper()
    mapper.SetInputData(data)

    #Creating the volume and setting its mapper and volume properties
    volume=vtk.vtkVolume()
    volume.SetMapper(mapper)
    volume.SetProperty(volume_property)

    #Creating the renderer,render window and the interactor
    renderer=vtk.vtkRenderer()
    renderer.SetBackground(0.1, 0.1, 0.1)
    renderer.AddVolume(volume)
    render_window=vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(1000, 1000)
    interactor=vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)
    render_window.Render()
    interactor.Start()

if __name__ == "__main__":
    main()
