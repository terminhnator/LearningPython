from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API deets

CLIENT_ID = "91c95336384c4471abae5a2cc178e4af"
CLIENT_SECRET = "296e4a4b92754c70b67598b70976148a"


# Search top 100 songs on Billboard according to date input

billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{billboard_date}/")

billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
scraped_songs = soup.find_all(name="h3", class_="a-no-trucate")
scraped_artists = soup.find_all(name="span", class_="a-no-trucate")

song_names = [song.getText().strip() for song in scraped_songs]

artist_names = [artist.getText().strip() for artist in scraped_artists]

# Connecting with Spotify through Spotipy

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"

    )
)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_urls = []
for song, artist in zip(song_names, artist_names):
    items = sp.search(q=f"track: {song} artist: {artist}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{billboard_date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)
