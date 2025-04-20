import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from config import SPOTIFY_URI, SPOTIFY_ID, SPOTIFY_SECRET


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private user-top-read user-library-read",
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=SPOTIFY_URI,
    show_dialog=True,
    cache_path="token.txt"
))

# Recommendation currently Depreciated and not Working:
# https://developer.spotify.com/documentation/web-api/reference/get-recommendations
