import json
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
        result = self.sp.current_user_playing_track()
        return result


if __name__ == '__main__':
    sp = SpCaller()
    print(sp.initWidgets())
