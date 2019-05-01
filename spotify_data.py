import spotipy
import spotipy.util as util
from config import *

def setup_credentials():
    """
    sets up all the credentials needed for data and to pause/play and returns it
    """
    if 'sp' not in globals():
        scopes = 'user-read-currently-playing user-modify-playback-state'
        token = util.prompt_for_user_token( username,
                                            scopes,
                                            client_id = client_id,
                                            client_secret = client_secret,
                                            redirect_uri = redirect_uri)
        sp = spotipy.Spotify(auth=token)
    return sp


def get_track_uri():
    """
    Returns the currently playing track's uri
    """
    sp = setup_credentials()
    current_track_info = sp.current_user_playing_track()

    return current_track_info['item']['uri']


def collect_data():
    """
    Collects data for song that is currently playing and adds it to a dictionary
    """
    sp = setup_credentials()
    current_track_info = sp.current_user_playing_track()

    #Checks whether a user is in fact listening to a song.  An exception is raised if they are not (i.e. listening to an ad instead)
    if current_track_info['currently_playing_type'] == 'track':
        #The value in the next line is obtained by searching for the 'item' key within the current_track_info dictionary and then searching for the 'id' key within the 'item' dictionary
        current_track_id = current_track_info['item']['id']
        current_track_name = current_track_info['item']['name']

        #See https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/ for more information about the type of data being collected
        track_analysis = spotify.audio_analysis(current_track_id)
        duration = track_analysis['track']['duration']
        beats = track_analysis['beats']
        bars = track_analysis['bars']
        #finding features like danceability, mood, etc.
        track_features = spotify.audio_features(current_track_id)
        danceability = track_features[0]['danceability']
        loudness = track_features[0]['loudness']
        energy = track_features[0]['energy']
        tempo = track_features[0]['tempo']
        mood = track_features[0]['valence']
    else:
        raise Exception('The audio currently playing is not a track')

    return beats, bars, danceability, loudness, energy, tempo, mood, duration

    #to return the id for unpausing the song

def unpause_song():
    """
    unpauses the currently playing song at the beginning
    """
    sp = setup_credentials()
    uri = get_track_uri()
    sp.start_playback(uris = [uri])

def pause_song():
    """
    pauses the currently playing song
    """
    sp = setup_credentials()
    sp.pause_playback()
#beats, bars, danceability, loudness, energy, tempo, mood, duration = collect_data()
#print(beats)
