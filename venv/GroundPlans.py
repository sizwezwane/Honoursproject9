import PIL.Image
import open3d as op
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib_scalebar.scalebar import ScaleBar
import datetime
from PIL import Image, ImageDraw, ImageFont
import time

def groundPlans(meshFileName):
    initTime = time.time()

    #input mesh
    mes = op.io.read_triangle_mesh(meshFileName)

    #boundary coordinates
    mi = mes.get_min_bound()
    ma = mes.get_max_bound()

    #midpoints of boundaries
    xav = (mi[0] + ma[0]) / 2
    yav = (mi[1] + ma[1]) / 2
    zav = (mi[2] + ma[2]) / 2


    #crop volume coordinates
    P5 = [mi[0], mi[1], mi[2]]
    P6 = [ma[0], mi[1], zav]
    P7 = [mi[0], ma[1], mi[2]]
    P8 = [ma[0], ma[1], zav]

    #clipping plane processing
    pol = op.visualization.SelectionPolygonVolume()
    bp = np.array([P5, P6, P8, P7])
    bp = bp.astype("float64")
    pol.orthogonal_axis = "XY"
    pol.axis_max = np.max(bp[:, 2])
    pol.axis_min = np.min(bp[:, 2])
    bp[:, 2] = 0
    pol.bounding_polygon = op.utility.Vector3dVector(bp)

    #remesh after clipping
    mes = pol.crop_triangle_mesh(mes)
    l = np.asarray(mes.vertices)
    mes.compute_vertex_normals()

    #visualiser
    vis = op.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mes)
    ctr = vis.get_view_control()
    ctr.change_field_of_view(step=-90.0)
    ctr.set_zoom(0.35)
    imaget = "GroundPlan.png"
    for i in range(100):
        vis.poll_events()
        vis.update_renderer()
        vis.capture_screen_image(imaget)
    vis.destroy_window()


    plt.figure()
    image = plt.imread(imaget)
    plt.imshow(image)
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    plt.title("Ground Plan")
    d = datetime.date.today().strftime("%Y-%m-%d")
    plt.text(xmin - 200, ymax - 90, d, size="smaller")

    plt.xlim([xmin - 200, xmax + 200])
    plt.ylim([ymin + 150, ymax - 150])
    scalebar = ScaleBar(1 / 260, location="lower right")  # 1 pixel = 0.2 meter
    plt.gca().add_artist(scalebar)
    plt.savefig("preGroundPlan.tif", format="tif", dpi=300)

    im = Image.open(r"preGroundPlan.tif")

    width, height = im.size
    left = int(0.1 * width)
    right = int(0.92 * width)
    top = int(0.15 * height)
    bot = int(0.85 * height)
    im2 = im.crop((left, top, right, bot))
    fontsize = 30
    font = ImageFont.truetype("arial.ttf", fontsize)

    #elevation e1 line
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((300, 900, 1350, 900), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((300, 900, 312.5, 875), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((325, 900, 312.5, 875), fill=128, width=3)
    drawBot.text((310, 900), "E1", fill=(0, 0, 0), font=font)

    # elevation e2 line
    drawtop = ImageDraw.Draw(im2)
    drawtop.line((300, 150, 1350, 150), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((300, 150, 312.5, 175), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((325, 150, 312.5, 175), fill=128, width=3)
    drawBot.text((300, 120), "E3", fill=(0, 0, 0), font=font)

    # elevation e3 line
    drawleft = ImageDraw.Draw(im2)
    drawleft.line((125, 200, 125, 825), fill=128, width=3)
    drawleft = ImageDraw.Draw(im2)
    drawleft.line((125, 200, 150, 212.5), fill=128, width=3)
    drawleft = ImageDraw.Draw(im2)
    drawleft.line((125, 225, 150, 212.5), fill=128, width=3)
    drawBot.text((85, 200), "E4", fill=(0, 0, 0), font=font)

    # elevation e4 line
    drawright = ImageDraw.Draw(im2)
    drawright.line((1400, 200, 1400, 825), fill=128, width=3)
    drawleft.line((1400, 200, 1375, 212.5), fill=128, width=3)
    drawleft = ImageDraw.Draw(im2)
    drawleft.line((1400, 225, 1375, 212.5), fill=128, width=3)
    drawBot.text((1410, 200), "E2", fill=(0, 0, 0), font=font)

    # s1 line
    drawBot = ImageDraw.Draw(im2)
    relbot = 275
    drawBot.line((300 - 50, 900 - relbot, 1350, 900 - relbot), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((300 - 50, 900 - relbot, 312.5 - 50, 875 - relbot), fill=128, width=3)
    drawBot = ImageDraw.Draw(im2)
    drawBot.line((325 - 50, 900 - relbot, 312.5 - 50, 875 - relbot), fill=128, width=3)
    drawBot.text((300 - 50, 900 - relbot), "S1", fill=(0, 0, 0), font=font)

    #s2 line
    drawright = ImageDraw.Draw(im2)
    relrig = 600
    drawright.line((1400 - relrig, 200, 1400 - relrig, 825), fill=128, width=3)
    drawleft.line((1400 - relrig, 200, 1375 - relrig, 212.5), fill=128, width=3)
    drawleft = ImageDraw.Draw(im2)
    drawleft.line((1400 - relrig, 225, 1375 - relrig, 212.5), fill=128, width=3)
    drawBot.text((1410 - relrig, 200), "S2", fill=(0, 0, 0), font=font)


    im2.save("liner.png")

    im2.save("GroundPlan.tif")

    endTime = time.time()
    print("The runtime for a ground plan is: ", endTime - initTime, "secs")
