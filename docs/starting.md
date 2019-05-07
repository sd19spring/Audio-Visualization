[Home Page](index.md)

### Getting Stared:

To run, you must have Spotipy installed. You can do this with pip:

$ pipenv install git+https://github.com/plamere/spotipy.git#egg=spotipyp

You must also create your own client id and place it in a file called config.py
so that the script can access spotify data. There is a template file named
config_template.py which can be edited once you have your own Spotify web API
client id and username. You can set up your clients by visiting [this page.](https://developer.spotify.com/dashboard/)
Once you are on this page, you can login and click "CREATE A CLIENT ID".

To run, you must also have pygame installed. You can do this with:

$ pip install -U pygame --user

### Usage:
Once you have done the setup, you can begin playing a Spotify song on any player 
and in the terminal from the repository folder, you can run the script with:

$ python vizify.py

You don't need to pass any arguments; this will pull up a GUI explaining how to
interact with the software.
