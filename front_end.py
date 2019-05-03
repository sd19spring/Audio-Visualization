from tkinter import *
#from spotify_data.py import *
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

#function that button calls
def execute():
    songtitle = songentry.get()
    artistname = artistentry.get()
    print(songtitle)
    print(artistname)
    return


#Define frame for use by button
interactiveframe = Frame(window, bg = color)
interactiveframe.pack(expand = 'true', fill = 'both', side = TOP)
playbtn = Button(interactiveframe, text = "play", command = execute)
playbtn.pack(expand = 'true', side = TOP)
exitinstructions = Label(interactiveframe, bg = color, text = "press ctrl+c to cancel the visualization at any time")

exitinstructions.pack(expand = 'true', fill = 'both', side = TOP)







window.mainloop()
