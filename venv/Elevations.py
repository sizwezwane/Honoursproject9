import open3d as op
import numpy as np

mes=op.io.read_triangle_mesh("Chapel_of_Nossa_Senhora_de_Baluarte - Copy3.ply")

pol=op.visualization.SelectionPolygonVolume()

mi=mes.get_min_bound()
ma=mes.get_max_bound()

xav=(mi[0]+ma[0])/2
yav=(mi[1]+ma[1])/2
zav=(mi[2]+ma[2])/2

print("xvals",mi[0],ma[0],xav)
print("yvals",mi[1],ma[1],yav)
print("zvals",mi[2],ma[2],zav)

P5=[mi[0],mi[1],mi[2]]
P6=[ma[0],mi[1],ma[2]]
P7=[mi[0],ma[1],mi[2]]
P8=[ma[0],ma[1],ma[2]]

bp=np.array([P5,P6,P8,P7])
bp=bp.astype("float64")
pol.orthogonal_axis="XY"
pol.axis_max=np.max(bp[:,2])
pol.axis_min=np.min(bp[:,2])
bp[:,2]=0

pol.bounding_polygon=op.utility.Vector3dVector(bp)

mes=pol.crop_triangle_mesh(mes)
l= np.asarray(mes.vertices)
mes.compute_vertex_normals()


vis=op.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mes)
ctr=vis.get_view_control()
ctr.change_field_of_view(step=-90.0)
ctr.set_zoom(0.35)

for i in range(100):
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image("elevation.png")
vis.destroy_window()




r = mes.get_rotation_matrix_from_xyz((-np.pi / 2,0, 0))
mes.rotate(r, center=(0, 0, 0))

sis=op.visualization.Visualizer()
sis.create_window()
sis.add_geometry(mes)
zctr=sis.get_view_control()
zctr.change_field_of_view(step=-90.0)
zctr.set_zoom(0.35)

for i in range(100):
    sis.poll_events()
    sis.update_renderer()
    sis.capture_screen_image("elevation2.png")
sis.destroy_window()


r = mes.get_rotation_matrix_from_xyz((0, -np.pi / 2, 0))
mes.rotate(r, center=(0, 0, 0))

tis=op.visualization.Visualizer()
tis.create_window()
tis.add_geometry(mes)
fctr=tis.get_view_control()
fctr.change_field_of_view(step=-90.0)
fctr.set_zoom(0.35)


for i in range(100):
    tis.poll_events()
    tis.update_renderer()
    tis.capture_screen_image("elevation3.png")
tis.destroy_window()


r = mes.get_rotation_matrix_from_xyz((0, -np.pi / 2, 0))
mes.rotate(r, center=(0, 0, 0))

uis=op.visualization.Visualizer()
uis.create_window()
uis.add_geometry(mes)
pctr=uis.get_view_control()
pctr.change_field_of_view(step=-90.0)
pctr.set_zoom(0.35)

for i in range(100):
    uis.poll_events()
    uis.update_renderer()
    uis.capture_screen_image("elevation4.png")
uis.destroy_window()

r = mes.get_rotation_matrix_from_xyz((0, -np.pi / 2, 0))
mes.rotate(r, center=(0, 0, 0))

wis=op.visualization.Visualizer()
wis.create_window()
wis.add_geometry(mes)
lctr=wis.get_view_control()
lctr.change_field_of_view(step=-90.0)
lctr.set_zoom(0.35)

for i in range(100):
    wis.poll_events()
    wis.update_renderer()
    wis.capture_screen_image("elevation5.png")
wis.destroy_window()



#op.visualization.draw_geometries([mes],width=1000)




#vis=op.visualization.ViewControl()
#vis.convert_to_pinhole_camera_parameters()
#vis=op.visualization.Visualizer( )

#vis.create_window()
#vis.add_geometry(mes)

#for i in range(2):

 #   vis.poll_events()
  #  vis.update_renderer()
   # vis.capture_screen_image("elevation.png")

#vis.destroy_window()







#print(mes.triangles[0].vertices)
#mesh=stl.stlmesh("Bearded guy.ply")
#meshSlicer= sl.slicer(mesh.triangles,None,1,False)
#meshSlicer.incremental_slicing()
#print(np.asarray(meshSlicer.planes[0][0].vertices[0].coord))
