from tkinter import *
from spotify_data import *
from visualizer import *
from shape_classes import *

#function that button calls
def execute():
    """
    Executes the visualizer when the button is pressed
    """
    songtitle = songentry.get()
    artistname = artistentry.get()
    if not songtitle:
        run_visualizer()
    else:
        run_visualizer(songtitle, artistname)


color = 'SlateGray2' #sets the background color for everything to use

#create tkinter master window
window = Tk()
frame = Frame(window, bg = color)
frame.pack(expand = 'true')
window.title("Vizify")

#Define frame for use by Vizify title text
titleframe = Frame(window, bg = color)
titleframe.pack(expand = 'true',side = TOP, fill = 'both')
title = Label(titleframe,bg = color, text = "VIZIFY", font = ('DINOT', 128, 'bold'))
title.pack(expand = 'true', fill = 'both', side = TOP)

# Define frame for use by instructions and description text
infoframe = Frame(window, bg = color)
infoframe.pack(expand = 'true', fill = 'both', side = TOP)
searchlabel = Label(infoframe, bg = color, text = "Enter the song you want to Visualize below,\n or leave them blank to visualize the currently playing song.",
font = ('DINOT', 18, 'bold')) #Creates a label entity with instructions
searchlabel.pack(expand = 'true', fill = 'both', side = TOP)


songentry = Entry(infoframe) #creates a text entry widget that stores the name of the song
songentry.pack( expand = 'true', side = LEFT)



bylabel = Label(infoframe, bg = color, text = "by", font = ('DINOT', 18, 'bold'))
bylabel.pack(padx = 0, side = LEFT)


artistentry = Entry(infoframe) #creates a text entry widget for artist name
artistentry.pack( expand = 'true', side = LEFT)

#Define frame for use by button
play_frame = Frame(window, bg = color)
play_frame.pack(expand = 'true', fill = 'both', side = TOP)
playbtn = Button(play_frame, text = "play", command = execute)
playbtn.pack(expand = 'true', side = TOP)

"""
I think we need multiprocessing to allow this to work

stop_frame = Frame(window, bg = color)
stop_frame.pack(expand = 'true', fill = 'both', side = TOP)
stopbtn = Button(stop_frame, text = "stop", command = kill)
stopbtn.pack(expand = 'true', side = TOP)

kill function would quit pygame
"""

exitinstructions = Label(play_frame, bg = color, text = "press the escape key to quit at any time")
exitinstructions.pack(expand = 'true', fill = 'both', side = TOP)

# make Esc exit the program
window.bind('<Escape>', lambda e: window.destroy())

window.mainloop()
