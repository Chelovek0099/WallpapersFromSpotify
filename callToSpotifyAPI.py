import json
import time
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import requests
from PIL import Image


class SpCaller:
    def __init__(self):
        scope = 'user-read-playback-state'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='bb16917a2d2540dc89f1684f350dbf95',
                                                       client_secret='3b34eff2997b4d57ad8aa4fea8f0e82d',
                                                       redirect_uri='https://localhost:80/callback'))
        with open(r"C:\Users\user\PycharmProjects\WallpapersFromSpotify\config.json") as config:
            config = json.load(config)
        self.albumImageSize = config["albumImageSize"]


    def initMainWindow(self):
        result = self.sp.current_user_playing_track()
        if result == None:
            return 'Ничего не воспроизводится', ''

        resource = requests.get(result["item"]["album"]["images"][1]["url"])
        print(self.albumImageSize)
        with open('albumImg.jpg', 'wb') as img:
            img.write(resource.content)
        img = Image.open('albumImg.jpg')
        newImg = img.resize((self.albumImageSize, self.albumImageSize))
        newImg.save('albumImg.jpg')
        print('done')
        name = result["item"]["name"]
        artist = ", ".join(artist["name"] for artist in result["item"]["artists"])

        return name, artist

    def getProgressTrack(self):
        result = self.sp.current_user_playing_track()

        if result != None:
            progress = int(result["progress_ms"]/1000)
            duration = int(result["item"]["duration_ms"]/1000)
        else:
            progress = '--:--'
            duration = '--:--'

        return (progress, duration)

    def getTrackUpdate(self):
        lastName = ''
        lastArtists = ''
        while True:
            result = self.sp.current_playback()
            if result == None:
                time.sleep(0.5)
                return self.initMainWindow()

            resource = requests.get(result["item"]["album"]["images"][1]["url"])

            name = result["item"]["name"]
            artist = ", ".join(artist["name"] for artist in result["item"]["artists"])
            if lastName + lastArtists == '':
                lastName = name
                lastArtists = artist
            if lastName + lastArtists != name + artist:
                with open('albumImg.jpg', 'wb') as img:
                    img.write(resource.content)
                img = Image.open('albumImg.jpg')
                newImg = img.resize((self.albumImageSize, self.albumImageSize))
                newImg.save('albumImg.jpg')
                return name, artist
            # print(f'{result["item"]["name"]} - {", ".join(artist["name"] for artist in result["item"]["artists"])}\n   ',
            #       f'{result["progress_ms"]//60000}:{0 if len(str(int(result["progress_ms"]/1000%60))) == 1 else ""}{int(result["progress_ms"]/1000%60)}'
            #       f' / {result["item"]["duration_ms"]//60000}:{0 if len(str(int(result["item"]["duration_ms"]/1000%60))) == 1 else ""}{int(result["item"]["duration_ms"]/1000%60)}')


if __name__ == '__main__':
    spotify = SpCaller()
    spotify.initMainWindow()
