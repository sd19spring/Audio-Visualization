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


def collect_data(current_track_id = None):
    """
    Collects data for song that is currently playing and adds it to a dictionary,
    or returns the data for a song given the id
    """
    sp = setup_credentials()

    if current_track_id is None:
        current_track_info = sp.current_user_playing_track()
        if current_track_info['currently_playing_type'] == 'track':
            #The value in the next line is obtained by searching for the 'item' key within the current_track_info dictionary and then searching for the 'id' key within the 'item' dictionary
            current_track_id = current_track_info['item']['id']
            current_track_name = current_track_info['item']['name']
        else:
            raise Exception('The audio currently playing is not a track')

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

def get_track_id(name, artist=None):
    """
    Finds and returns a song ID given a track name
    """
    sp = setup_credentials()
    #cuts out the leading and ending whitespace
    name.lstrip()
    name.rstrip()
    #sets a query to search with replacing spaces with %20 for the search.
    q = 'track:'+name
    #adds the artist if they want to use it
    if artist is not None:
        artist.lstrip()
        artist.rstrip()
        q += ' AND artist:' + artist
    print(q)
    try:
        results = spotify.search(q,limit=1)
        print(results)
        id = results['tracks']['items'][0]['id']
        return id
    except:
        return "No Search Results"

#beats, bars, danceability, loudness, energy, tempo, mood, duration = collect_data()
#print(beats)
