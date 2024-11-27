import pyaudio
import librosa
import wave
import random
import time
import os
import asyncio
from statistics import mean

CHUNK = 2**11
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100


def callback(in_data, frame_count, time_info, flag):
    if flag:
        print("Playback Error: %i" % flag)

    file_name = f'temp{random.randint(1, 100)}.wav'
    file = wave.open(file_name, 'wb')
    file.setnchannels(CHANNELS)
    file.setsampwidth(FORMAT)
    file.setframerate(RATE)

    file.writeframes(in_data)
    file.close()

    y, sr = librosa.load(file_name)
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    val_harmonic = int(abs(y_harmonic[0]) * 70)
    val_16000 = val_harmonic + random.randint(1, 3) if val_harmonic != 0 else 0
    val_4000 = val_harmonic + random.randint(0, 2) if val_harmonic != 0 else 0
    val_8000 = val_4000 + random.randint(0, 1) if val_4000 != 0 else 0
    val_percussive = int(abs(y_percussive[0]) * 270)
    val_125 = val_percussive - random.randint(0, 2) if val_percussive != 0 else 0
    val_63 = val_percussive - random.randint(0, 1) if val_percussive != 0 else 0
    val_32 = val_63 - random.randint(0, 2) if val_63 != 0 else 0
    val_1000 = int(mean([val_harmonic, val_percussive])) + random.randint(-2, 2) if val_percussive != 0 and val_harmonic != 0 else 0
    val_500 = int(mean([val_harmonic, val_percussive])) + random.randint(-2, 2) if val_percussive != 0 and val_harmonic != 0 else 0

    vals = [val_32, val_63, val_125, val_percussive, val_500, val_1000, val_harmonic, val_4000, val_8000, val_16000]

    for i in range(20):
        res = ''
        for k in vals:
            if k >= 20 - i:
                res += '=== '
            else:
                res += '    '
        print(res)
    print(''.join([str(i) + ' ' * (4 - len(str(i))) for i in vals]))
    os.remove(file_name)
    return in_data, pyaudio.paContinue

async def equalizer(x):
    time.sleep(x)
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)

    while stream.is_active():
        pass

    stream.close()
    p.terminate()

async def main():
    task = asyncio.create_task(equalizer(0))
    task2 = asyncio.create_task(equalizer(0.2))
    await asyncio.gather(task, task2)

asyncio.run(main())
