import spotipy
import spotipy.util as util
from clients import client_id, client_secret, username, redirect_uri

print(spotipy.VERSION)

scope = 'user-read-currently-playing'

token = util.prompt_for_user_token( username,
                                    scope,
                                    client_id = client_id,
                                    client_secret = client_secret,
                                    redirect_uri = redirect_uri)

sp = spotipy.Spotify(auth=token)
current_track_info = sp.current_user_playing_track()

print(current_track_info)
