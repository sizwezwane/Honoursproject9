import open3d as op
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar
import datetime
from PIL import Image
import time

def sectionViews(meshFileName):

    initTime = time.time()

    #input mesh
    mes = op.io.read_triangle_mesh(meshFileName)

    r = mes.get_rotation_matrix_from_xyz((-np.pi / 2, 0, 0))
    mes.rotate(r, center=(0, 0, 0))


    # boundary coordinates
    mi = mes.get_min_bound()
    ma = mes.get_max_bound()

    # midpoints of boundaries
    xav = (mi[0] + ma[0]) / 2
    yav = (mi[1] + ma[1]) / 2
    zav = (mi[2] + ma[2]) / 2

    # crop volume coordinates
    P5 = [mi[0], mi[1], mi[2]]
    P6 = [ma[0], mi[1], zav + 5]
    P7 = [mi[0], ma[1], mi[2]]
    P8 = [ma[0], ma[1], zav + 5]

    # clipping plane processing
    pol = op.visualization.SelectionPolygonVolume()
    bp = np.array([P5, P6, P8, P7])
    bp = bp.astype("float64")
    pol.orthogonal_axis = "XY"
    pol.axis_max = np.max(bp[:, 2])
    pol.axis_min = np.min(bp[:, 2])
    bp[:, 2] = 0
    pol.bounding_polygon = op.utility.Vector3dVector(bp)

    # remesh after clipping
    mes = pol.crop_triangle_mesh(mes)
    l = np.asarray(mes.vertices)
    mes.compute_vertex_normals()

    # visualiser for S1
    vis = op.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mes)
    ctr = vis.get_view_control()
    ctr.change_field_of_view(step=-90.0)
    ctr.set_zoom(0.35)
    imageS1 = "SectionView1.png"

    for i in range(100):
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(imageS1)
    vis.destroy_window()

    plt.figure()
    image1 = plt.imread(imageS1)
    plt.imshow(image1)
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    plt.title("Section View S1")
    d = datetime.date.today().strftime("%Y-%m-%d")
    plt.text(xmin - 200, ymax - 90, d, size="smaller")
    plt.xlim([xmin - 200, xmax + 200])
    plt.ylim([ymin + 150, ymax - 150])
    scalebar = ScaleBar(1 / 260, location="lower right")  # 1 pixel = 0.2 meter
    plt.gca().add_artist(scalebar)
    plt.savefig("preSectionViewS1.tif", format="tif", dpi=300)

    im1 = Image.open(r"preSectionViewS1.tif")
    width, height = im1.size
    left = int(0.1 * width)
    right = int(0.92 * width)
    top = int(0.15 * height)
    bot = int(0.85 * height)
    im42 = im1.crop((left, top, right, bot))
    im42.save("sectionViewS1.tif")



    mes = op.io.read_triangle_mesh(meshFileName)

    r = mes.get_rotation_matrix_from_xyz((-np.pi / 2, 0, -np.pi / 2))
    mes.rotate(r, center=(0, 0, 0))

    pol = op.visualization.SelectionPolygonVolume()

    mi = mes.get_min_bound()
    ma = mes.get_max_bound()

    xav = (mi[0] + ma[0]) / 2
    yav = (mi[1] + ma[1]) / 2
    zav = (mi[2] + ma[2]) / 2



    P5 = [mi[0], mi[1], mi[2]]
    P6 = [ma[0], mi[1], zav]
    P7 = [mi[0], ma[1], mi[2]]
    P8 = [ma[0], ma[1], zav]

    bp = np.array([P5, P6, P8, P7])
    bp = bp.astype("float64")
    pol.orthogonal_axis = "XY"
    pol.axis_max = np.max(bp[:, 2])
    pol.axis_min = np.min(bp[:, 2])
    bp[:, 2] = 0
    pol.bounding_polygon = op.utility.Vector3dVector(bp)

    mes = pol.crop_triangle_mesh(mes)
    l = np.asarray(mes.vertices)
    mes.compute_vertex_normals()

    # visualiser for S2
    wis = op.visualization.Visualizer()
    wis.create_window()
    wis.add_geometry(mes)
    lctr = wis.get_view_control()
    lctr.change_field_of_view(step=-90.0)
    lctr.set_zoom(0.35)
    imageE4 = "sectionViewS2.png"
    for i in range(100):
        wis.poll_events()
        wis.update_renderer()
        wis.capture_screen_image(imageE4)
    wis.destroy_window()

    plt.figure()
    image4 = plt.imread(imageE4)
    plt.imshow(image4)
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    plt.title("Section View S2")
    d = datetime.date.today().strftime("%Y-%m-%d")
    plt.text(xmin - 200, ymax - 90, d, size="smaller")
    plt.xlim([xmin - 200, xmax + 200])
    plt.ylim([ymin + 150, ymax - 150])
    scalebar = ScaleBar(1 / 260, location="lower right")  # 1 pixel = 0.2 meter
    plt.gca().add_artist(scalebar)
    plt.savefig("preSectionViewS2.tif", format="tif", dpi=300)

    im4 = Image.open(r"preSectionViewS2.tif")
    width, height = im4.size
    left = int(0.1 * width)
    right = int(0.92 * width)
    top = int(0.15 * height)
    bot = int(0.85 * height)
    im42 = im4.crop((left, top, right, bot))
    im42.save("SectionViewS2.tif")

    endTime = time.time()
    print("The runtime for section views is: ", endTime - initTime, "sec")
