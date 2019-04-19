import spotipy
import spotipy.util as util
from config import *

scope = 'user-read-currently-playing'

token = util.prompt_for_user_token( username,
                                    scope,
                                    client_id = client_id,
                                    client_secret = client_secret,
                                    redirect_uri = redirect_uri)

sp = spotipy.Spotify(auth=token)
current_track_info = sp.current_user_playing_track()

if current_track_info['currently_playing_type'] == 'track':
    current_track_id = current_track_info['item']['id']
    current_track_name = current_track_info['item']['name']

    #see https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/
    track_analysis = spotify.audio_analysis(current_track_id)
    beats = track_analysis['beats']
    bars = track_analysis['bars']
    #sections contains things like loudness and tempo
    sections = track_analysis['sections']
else:
    raise Exception('The audio currently playing is not a track')


print(current_track_name)
print(beats, bars)
