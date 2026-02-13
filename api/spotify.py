import requests
import os
from dotenv import load_dotenv

# Configuration
load_dotenv()
clientToken = os.getenv("CLIENT_TOKEN")
accessToken = os.getenv("ACCESS_TOKEN")
url = "https://api-partner.spotify.com/pathfinder/v2/query"

def getHeaders():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Authorization": f"Bearer {accessToken}",
    }
    return headers

def addTrackToPlaylist(playlistId : str, trackId : str):
    playlistUri = "spotify:playlist:" + playlistId
    trackUri = "spotify:track:" + trackId
    payload = {
        "variables": {
            "playlistItemUris": [trackUri],
            "playlistUri": playlistUri,
            "newPosition": {
                "moveType": "BOTTOM_OF_PLAYLIST",
                "fromUid": None
            }
        },
        "operationName": "addToPlaylist",
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "47b2a1234b17748d332dd0431534f22450e9ecbb3d5ddcdacbd83368636a0990"
            }
        }
    }

    headers = getHeaders()
    response = requests.post(url, headers=headers, json=payload)

    print("Statut de la réponse :", response.status_code)
    print("Contenu de la réponse :", response.text)

def getTrackIdByName(trackName : str, trackArtist : str):
    searchQuery = trackName + " " + trackArtist
    payload = {
        "variables": {
            "searchTerm": searchQuery,
            "offset": 0,
            "limit": 1,
            "numberOfTopResults": 1,
            "includeAudiobooks": False,
            "includeArtistHasConcertsField": False,
            "includePreReleases": False,
            "includeAuthors": False
        },
        "operationName": "searchDesktop",
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "3c9d3f60dac5dea3876b6db3f534192b1c1d90032c4233c1bbaba526db41eb31"
            }
        }
    }
    
    headers = getHeaders()
    response = requests.post(url, headers=headers, json=payload)

    print("Statut de la réponse :", response.status_code)
    
    trackId = response.json()["data"]["searchV2"]["tracksV2"]["items"][0]["item"]["data"]["id"]
    return trackId
    
if __name__ == "___main__":
    # addTrackToPlaylist("5PwOtSkiMYkAqnDZN45G6S", "2tpWsVSb9UEmDRxAl1zhX1")
    trackId = getTrackIdByName("counting stars", "one republic")