import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(  client_id='your_client_id',
                                                        client_secret='your_secret_client_id')
username = 'username'
