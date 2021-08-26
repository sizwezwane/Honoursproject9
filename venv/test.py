import open3d as op
import numpy as np



mes=op.io.read_triangle_mesh("on now2.ply")
l= np.asarray(mes.vertices)
t=np.asarray(mes.triangles)
mi=0
ma=0
for i in l:
    mi=min(mi,i[2])
    ma=max(ma,i[2])
av=(mi+ma)/2
vertPos=[]

for i in range(len(l)):
    l[i][2]=mi


mes.compute_vertex_normals()
op.visualization.draw_geometries([mes])

print(mi,ma,av)


#vis=op.visualization.ViewControl()
#vis.convert_to_pinhole_camera_parameters()
#vis=op.visualization.Visualizer( )

#vis.create_window()
#vis.add_geometry(mes)

#for i in range(2):

 #   vis.poll_events()
  #  vis.update_renderer()
   # vis.capture_screen_image("out.png")

#vis.destroy_window()







#print(mes.triangles[0].vertices)
#mesh=stl.stlmesh("Bearded guy.ply")
#meshSlicer= sl.slicer(mesh.triangles,None,1,False)
#meshSlicer.incremental_slicing()
#print(np.asarray(meshSlicer.planes[0][0].vertices[0].coord))
