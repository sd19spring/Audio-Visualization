#import sounddevice
import pyaudio
import numpy as np

CHUNK = 4096
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels = 1, rate = RATE, input = True,
                frames_per_buffer = CHUNK)

for i in range(30):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(data)

stream.stop_stream()
stream.close()
p.terminate()
