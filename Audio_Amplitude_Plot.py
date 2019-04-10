#Code is influenced by: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1554825538.1988689899444580078125

from scipy import io
from scipy import fftpack
from scipy.io import wavfile
import numpy as np

def read_audio_file(file_name):
    """
    Use .wav file in argument
    """
    sample_rate, data = io.wavfile.read(file_name)
    return 'Sample Rate: {}'.format(sample_rate)

def create_frequency_graph(file_name):
    sampFreq, sample_rate, snd = wavfile.read(file_name)
    #The code below maps the sound pressue values to integer values
    snd = snd / (2.**15)
    snd1 = snd[:,0]
    num_sample_points = snd.shape[0]
    time_array = arrange(0, num_sample_points, 1)
    time_array = (time_array / samp_Freq) * 1000 #The 1000 scales the data to milliseconds
    plot(time_array, snd1)
    ylabel('Amplitude')
    xlabel('Time (ms)')
