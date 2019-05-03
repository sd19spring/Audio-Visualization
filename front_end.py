import tkinter
#from spotify_data.py import *


window = tkinter.Tk()
window.title("Vizify")

lbl = tkinter.Label(window, text = "Create Visualizations for my music")
playbtn = tkinter.Button(window, text = "play")
pausebtn = tkinter.Button(window, text = "pause")

lbl.pack()
playbtn.pack()
pausebtn.pack()
window.mainloop()
