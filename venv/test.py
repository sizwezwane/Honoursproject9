import open3d as op
import numpy as np



mes=op.io.read_triangle_mesh("Chapel_of_Nossa_Senhora_de_Baluarte - Copy3.ply")



l= np.asarray(mes.vertices)
print(l)
t=np.asarray(mes.triangles)
xmi=0
xma=0
ymi=0
yma=0
zmi=0
zma=0

for i in l:
    xmi=min(xmi,i[0])
    xma=max(xma,i[0])
    ymi=min(ymi,i[1])
    yma=max(yma,i[1])
    zmi=min(zmi,i[2])
    zma=max(zma,i[2])

xav=(xmi+xma)/2
yav=(ymi+yma)/2
zav=(zmi+zma)/2

for i in range(len(l)):
    l[i][0]=l[i][0]-xav
    l[i][1] = l[i][1] - yav
    l[i][2] = l[i][2] - zav

r=mes.get_rotation_matrix_from_xyz((-np.pi/2,0,0))
mes.rotate(r,center=(0,0,0))


print("xvals",xmi,xma,xav)
print("yvals",ymi,yma,yav)
print("zvals",zmi,zma,zav)


vis=op.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mes)
ctr=vis.get_view_control()
ctr.change_field_of_view(step=-90.0)

for i in range(100):
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image("out.png")
vis.destroy_window()




r = mes.get_rotation_matrix_from_xyz((0, -np.pi / 2, 0))
mes.rotate(r, center=(0, 0, 0))

sis=op.visualization.Visualizer()
sis.create_window()
sis.add_geometry(mes)
zctr=sis.get_view_control()
zctr.change_field_of_view(step=-90.0)
print(l)

for i in range(100):
    sis.poll_events()
    sis.update_renderer()
    sis.capture_screen_image("out2.png")
sis.destroy_window()




#op.visualization.draw_geometries([mes],width=1000)




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
