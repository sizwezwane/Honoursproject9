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
P6=[ma[0],mi[1],zav]
P7=[mi[0],ma[1],mi[2]]
P8=[ma[0],ma[1],zav]

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
    vis.capture_screen_image("GroundPlan.png")
vis.destroy_window()