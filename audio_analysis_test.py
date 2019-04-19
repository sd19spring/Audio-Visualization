#audio_analysis_test
#Take an Audio file, analyse it, and return a file with useable data, in a useable format

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib tk

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

data = stream.read(CHUNK)
data
