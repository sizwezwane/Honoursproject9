import PySimpleGUI as sg
import os
from PIL import Image
import io
from GroundPlans import groundPlans
from Elevations import elevations
from SectionView import sectionViews

sg.theme("Black")
layout = [[sg.Image(key="-IMAGE-")], [sg.Text("Choose a mesh file: "), sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Button("Start processing")]]

###Building Window
window = sg.Window('Scan3d tool', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Start processing":
        filename=values["-IN-"]
        if os.path.exists(filename):
            groundPlans(filename)
            elevations(filename)
            sectionViews(filename)

            image=Image.open("liner.png")

            bio=io.BytesIO()
            image.save(bio,format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())

window.close()