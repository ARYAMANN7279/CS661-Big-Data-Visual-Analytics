# Importing Dependencies
import vtk
# Defining the interpolation function 
def interpolate(p1,p2,v1,v2,isovalue):
    temp=(isovalue-v1)/(v2-v1)
    res=[0.0,0.0,0.0]
    #Interpolating the values of each corrdinate
    for i in range(3):
        interpolated=p1[i]+temp*(p2[i]-p1[i])
        res[i]=interpolated
    return res
def main():
    #Prompting user for input
    dataset=input("Enter path to .vti dataset (e.g. Isabel_2D.vti):").strip()
    output=input("Enter output filename (e.g. output.vtp):").strip()
    isovalue=float(input("Enter the isovalue you want to see:").strip())
    # Loading the reader function and setting dataset to be read by the reader
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(dataset)
    reader.Update()
    image=reader.GetOutput()         # Getting image output from the reader
    dims=image.GetDimensions()       # Extracting the image dimensions 
    scalars=image.GetPointData().GetScalars()        #Getting the scalar values/ Pressure values from the data
    points=vtk.vtkPoints()
    CellArray=vtk.vtkCellArray()

    def point_id(i, j):      #Function to ease the work of calculating point id or point index for the edges
        return j * dims[0] + i

    for j in range(dims[1]-1):
        for i in range(dims[0]-1):
            idx=[point_id(i, j),point_id(i + 1, j),point_id(i + 1, j + 1),point_id(i, j + 1)]
            # Getting the 3D coordinates to deal with the actual data points 
            coords=[]
            for id in idx:
                pt = image.GetPoint(id)
                coords.append(pt)
            # Storing the pressure values of the edges of the cell in an list
            values=[]
            for id in idx:
                val=scalars.GetTuple1(id)
                values.append(val)
            edges=[(0,1),(1,2),(2,3),(3,0)]
            # To get the edges which are being intersected or contain the isovalue
            intersecting_edges=[]
            for a,b in edges:
                v1,v2=values[a],values[b]
                if (v1-isovalue)*(v2-isovalue)<0:    #Logic to check the intersection of the edge with the isovalue
                    intersecting_edges.append((a,b))
            if len(intersecting_edges)==2:           #Checking the condition that the cell contain only two intersection points of the isovalue rest all cells to be skipped
                edge_list=[]
                for a,b in intersecting_edges:
                    p=interpolate(coords[a],coords[b],values[a],values[b],isovalue)
                    edge_list.append(p)
                pid1=points.InsertNextPoint(edge_list[0])
                pid2=points.InsertNextPoint(edge_list[1])
                line=vtk.vtkLine()
                line.GetPointIds().SetId(0,pid1)
                line.GetPointIds().SetId(1,pid2)
                CellArray.InsertNextCell(line)
    # Writing the data to vtp file
    polydata=vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetLines(CellArray)
    writer=vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(output)
    writer.SetInputData(polydata)
    writer.Write()
    print(f"Isocontour is in '{output}'")

if __name__ == "__main__":
    main()
