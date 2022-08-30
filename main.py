import spotipy
import csv
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

auth_manager = SpotifyClientCredentials(client_id='88bdee511a5f42759c27f2b9075fa728',
                                        client_secret='6a3b0a7af04e48c4a297a184f5fb7f9d')
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_link = "https://open.spotify.com/playlist/662hCEwDvWgxOtQxzx732X?si=0bb949f58a41406e"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
header = ['track_name', 'artist_name', 'artist_pop', 'album', 'track_pop', 'danceability', 'energy', 'loudness', 'mode',
          'key', 'speechiness', 'acousticness', 'instrumentalness',
          'liveness', 'valence', 'tempo', 'time_signature', 'duration_ms']


def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


tracks_p = get_playlist_tracks(playlist_URI)
with open('TikTok_songs_2021_otherone.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    count = 0

    for track in tracks_p:
        count += 1
        # URI
        track_uri = track["track"]["uri"]

        # Track name
        track_name = track["track"]["name"]

        # Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)

        # Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]

        # Album
        album = track["track"]["album"]["name"]

        # Popularity of the track
        track_pop = track["track"]["popularity"]
        # Audio features of the track
        audio_features = sp.audio_features(track_uri)[0]
        danceability = audio_features['danceability']
        energy = audio_features['energy']
        key = audio_features['key']
        loudness = audio_features['loudness']
        mode = audio_features['mode']
        speechiness = audio_features['speechiness']
        acousticness = audio_features['acousticness']
        instrumentalness = audio_features['instrumentalness']
        liveness = audio_features['liveness']
        valence = audio_features['valence']
        tempo = audio_features['tempo']
        time_signature = audio_features['time_signature']
        duration_ms = audio_features['duration_ms']
        # print(danceability)

        data = [track_name, artist_name, artist_pop, album, track_pop, danceability, energy, loudness, mode, key,
                speechiness, acousticness, instrumentalness,
                liveness, valence, tempo, time_signature, duration_ms]
        writer.writerow(data)

print(count)
