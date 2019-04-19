# Audio-Visualization
# Audio-Visualization Utilizing Spotify Song Data
Harrison-AlexScott-DavidT

The purpose of this code is to create engaging visualizations that play
alongside a User's Spotify music.  These visualizations utilize different
numerical elements of a song, such as its tempo, intensity, and danceability,
to ensure the vibe of the visualization matches the vibe of the song.

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
