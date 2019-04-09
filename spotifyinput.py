# https://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from clients import client_credentials_manager, username

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
