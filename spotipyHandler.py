import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpCaller:
    def __init__(self):
        scope = 'user-read-playback-state'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='bb16917a2d2540dc89f1684f350dbf95',
                                  client_secret='3b34eff2997b4d57ad8aa4fea8f0e82d',
                                  redirect_uri='https://localhost:80/callback'))
        self.initCache()

    def initCache(self):
        self.sp.current_playback()

    def getTrackInfo(self):
        for i in range(5):
            try:
                result = self.sp.current_user_playing_track()

                resource = requests.get(result["item"]["album"]["images"][1]["url"])
                with open('callback_resources/albumImg.jpg', 'wb') as img:
                    img.write(resource.content)
            except:
                pass
            else:
                return result
        raise Exception()
