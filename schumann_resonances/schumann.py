# https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
# https://stackoverflow.com/questions/52477889/how-to-write-pyaudio-output-into-audio-file
import time
import numpy as np
import pyaudio
from scipy.io.wavfile import write

SAMPLE_RATE = 44100  # sampling rate, Hz, must be integer
VOLUME = 0.5  # range [0.0, 1.0]
DURATION = 5.0  # in seconds, may be float
# f = 440.0  # sine frequency, Hz, may be float
FREQ = 7.83  # 7.83 Hz is the Schumann resonance frequency


def play_sound(samples):
    p = pyaudio.PyAudio()
    # per @yahweh comment explicitly convert to bytes sequence
    output_bytes = (VOLUME * samples).tobytes()
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=SAMPLE_RATE, output=True)
    # play. May repeat with different volume values (if done interactively)
    start_time = time.time()
    stream.write(output_bytes)
    print("Played sound for {:.2f} seconds".format(time.time() - start_time))
    stream.stop_stream()
    stream.close()
    p.terminate()


# generate samples, note conversion to float32 array
samples = (
    np.sin(2 * np.pi * np.arange(SAMPLE_RATE * DURATION) * FREQ / SAMPLE_RATE)
).astype(np.float32)
# play_sound(samples)

write("schumann.wav", SAMPLE_RATE, samples)
