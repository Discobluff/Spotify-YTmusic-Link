import requests
from lxml import html
import os
from dotenv import load_dotenv

def getTracksInPlaylist(playlistId :str):
    load_dotenv()
    api_key = os.getenv("YT_KEY")
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlistId}&key={api_key}&maxResults=50"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['items']


if __name__ == "__main__":
    print(getTracksInPlaylist("PL656OcuvU0LJckYdExgBxh4QDyVQ6WZqE")[0]["snippet"])