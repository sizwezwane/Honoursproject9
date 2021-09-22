import PySimpleGUI as sg
import os
from PIL import Image
import io
from GroundPlans import groundPlans
from Elevations import elevations
from SectionView import sectionViews

sg.theme("DarkTeal2")
layout = [[sg.Image(key="-IMAGE-")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        filename=values["-IN-"]
        if os.path.exists(filename):
            groundPlans(filename)
            elevations(filename)
            sectionViews(filename)

            bio=io.BytesIO()
            image.save(bio,format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())

window.close()