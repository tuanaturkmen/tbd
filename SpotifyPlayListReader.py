import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

class SpotifyPlayListReader:

    username = 'your_username';
    playlist_id = 'your_playlist_id';

    def initialize_spotify_connections(scopeVariabe):    
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=scopeVariabe
        ))
        return sp

    # Function to get playlist tracks
    def get_playlist_tracks(username, playlist_id):
        sp = initialize_spotify_connections("playlist-read-private");
        results = sp.user_playlist_tracks(username, playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    
    # Function to get liked songs
    def get_liked_songs():
       
        sp = initialize_spotify_connections("user-library-read");
        results = sp.current_user_saved_tracks()
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    
    # Write to CSV
    def write_list_to_file(tracks, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Track Name', 'Artist', 'Album'])
            for item in tracks:
                track = item['track']
                writer.writerow([track['name'], track['artists'][0]['name'], track['album']['name']])


    #main flow
    tracks = get_liked_songs();
    write_list_to_file(tracks, "deneme.csv");
