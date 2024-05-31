import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

class SpotifyPlayListReader:


    def __init__(self, username, playlist_id):
        self.username = username;
        self.playlist_id = playlist_id;


    def initialize_spotify_connections(self, scopeVariabe):    
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=scopeVariabe
        ))
        return sp

    
    def get_playlist_tracks(self, playlist_id):
        """
        Function to get playlist tracks
        """
        sp = initialize_spotify_connections("playlist-read-private");
        results = sp.user_playlist_tracks(self.username, self.playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    


    def get_liked_songs():
        """
        Function to get liked songs
        """
        sp = initialize_spotify_connections("user-library-read");
        results = sp.current_user_saved_tracks()
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    

    def write_list_to_file(self, racks, filename):
        """
         Write to CSV
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Track Name', 'Artist', 'Album'])
            for item in tracks:
                track = item['track']
                writer.writerow([track['name'], track['artists'][0]['name'], track['album']['name']])

