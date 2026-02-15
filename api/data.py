import json

DATA_PATH = "data.json"

def readJson(path : str):
    data = ""
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def writeJson(path :str, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def createNewPlaylist(name : str, spotifyId : str, ytMusicId : str):
    return {"name" : name, "spotifyId" : spotifyId, "ytMusicId" : ytMusicId, "tracks":[]}

def createTrack(title : str, artist : str, ytId : str):
    return {"title" : title, "artist" : artist, "ytId" : ytId}

def addPlaylist(name : str, spotifyId : str, ytMusicId : str):
    data = readJson(DATA_PATH)
    
    if 'playlists' not in data:
        data['playlists'] = []
    
    newPlaylist = createNewPlaylist(name, spotifyId, ytMusicId)
    
    data['playlists'].append(newPlaylist)
    
    writeJson(DATA_PATH, data)

def addTrackToPlaylist(playlistId : str, title : str, artist : str, ytId):
    data = readJson(DATA_PATH)
    
    for playlist in data['playlists']:
        if playlist["ytMusicId"] == playlistId:
            playlist["tracks"].append(createTrack(title, artist, ytId))
    
    writeJson(DATA_PATH, data)
    
def isTrackPresent(playlistId : str, trackId : str) -> bool:
    data = readJson(DATA_PATH)
    
    for playlist in data['playlists']:
        if playlist["ytMusicId"] == playlistId:
            for track in playlist["tracks"]:
                if track["ytId"] == trackId:
                    return True
    
    return False

if __name__ == "__main__":
    addPlaylist("coucou")