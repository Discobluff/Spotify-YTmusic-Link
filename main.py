import api.data as dt
import api.spotify as spt
import api.yt_music as yt

def main():
    data = dt.readJson(dt.DATA_PATH)
    
    for playlist in data["playlists"]:
        tracks = yt.getTracksInPlaylist(playlist["ytMusicId"])
        for track in tracks:
            trackData = track["snippet"]
            title = trackData["title"]
            artist = trackData["videoOwnerChannelTitle"]
            ytId = trackData["resourceId"]["videoId"]
            if not dt.isTrackPresent(playlist["ytMusicId"], ytId):
                dt.addTrackToPlaylist(playlist["ytMusicId"], title, artist, ytId)
                spotifyTrackId = spt.getTrackIdByName(title, artist)
                spt.addTrackToPlaylist(playlist["spotifyId"], spotifyTrackId)
                print(spotifyTrackId)
                print("New Track Added")

if __name__ == "__main__":
    main()