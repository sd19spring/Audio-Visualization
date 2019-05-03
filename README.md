# Audio-Visualization Utilizing Spotify Song Data
Authors: Alex Scott, David Tarazi, Harrison Mintz

### Description:

The purpose of this code is to create engaging visualizations that play
alongside a User's Spotify music.  These visualizations utilize different
numerical elements of a song, such as its tempo, intensity, and danceability,
to ensure the vibe of the visualization matches the vibe of the song.  The
visualizations fall into two general categories.  The first type of 
visualization shows pulsing circles whose color matches the intensity
of a song.  The second type of visualization shows moving rectangles
whose shape and speed is determined by the songs numerical attributes.

### Getting Stared:

To run, you must have Spotipy installed. You can do this with:

$ pip install spotipy

However, the pip install does not create the correct version and despite our
efforts to find a way to install the correct version it was easier to find the
file location of the spotipy install and replace the file, client.py, in that
install location with the client.py file in this repo. You can find where
install location with the client.py file in this repository. You can find where
spotipy is installed with:

$ pip show spotipy

You must also create your own client id and place it in a file called config.py
so that the script can access spotify data. There is a template file named
config_template.py which can be edited once you have your own Spotify web API
client id and username.

To run, you must also have pygame installed.  You can do this with:

$ pip install -U pygame --user

### Usage:
Once you have done the setup, you can begin playing a Spotify song on any player 
and in the terminal from the repository folder, you can run the script with:

$ python visualizer.py

You don't need to pass any arguments; the program reads the song you are currently 
listening to and restarts it to synchronize the visual and audio.

### License:

This project is licensed under the GNU APGLv3 license.
For more details regarding this license, please see the LICENSE.md file

### Tip Jar:

If you love our code SO much, are a big fan of our trippy music visualizations,
or perhaps just want to help out some broke college students then it is your 
lucky day because we accept tips!
You can Venmo any of us at @HarrisonMintz and @David-Tarazi

Thank you :)
