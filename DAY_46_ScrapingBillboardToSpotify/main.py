import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
from dotenv import load_dotenv

CLIENT_ID_SPOTIFY = os.getenv('CLIENT_ID_SPOTIFY')
CLIENT_SECRET_SPOTIFY = os.getenv('CLIENT_SECRET_SPOTIFY')
REDIRECT_URI = os.getenv("REDIRECT_URI")
SPOTIFY_DISPLAY_NAME = os.getenv("SPOTIFY_DISPLAY_NAME")
SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")
PLAYLIST_ID = ""


#date_billboard = input("Which year do you want to travel to? (YYYY-MM-DD): ")
date_billboard = "2021-11-07"
billboard_url = f"https://www.billboard.com/charts/hot-100/{date_billboard}"
#print(billboard_url)

response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

# SCRAPING BILLBOARD
billboard_table = soup.select(selector="div li ul li h3[id='title-of-a-story']")
billboard_songs = [title.getText().strip() for title in billboard_table]
#print(billboard_songs)
#print(len(billboard_songs))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY,
                                               client_secret=CLIENT_SECRET_SPOTIFY,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=SPOTIFY_DISPLAY_NAME))


# print(sp.current_user())
USER_ID = sp.current_user()["id"]
#print(USER_ID)

#Create playlist
def create_playlist():
    playlist_name = f"TOP BILLBOARD {date_billboard}"
    p = sp.user_playlist_create(USER_ID, playlist_name, public=False,
                                description="")
    #print(p)
    global PLAYLIST_ID
    PLAYLIST_ID = p["id"]
    #print(PLAYLIST_ID)

create_playlist()

playlist_songs = []

for song in billboard_songs:
    result = sp.search(q=f"track: {song} year: {date_billboard[:4]}", type='track')
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        playlist_songs.append(uri)
    except IndexError:
        print(f"No song found for {song}. Skipping...")


def add_tracks_to_playlist():
    sp.playlist_add_items(PLAYLIST_ID, playlist_songs)

add_tracks_to_playlist()


