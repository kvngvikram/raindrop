import numpy as np
from scipy.io.wavfile import read

drop = read("drop.wav")
audio = read("audio.wav")

print(drop)

drop = np.asarray(drop[1],dtype=float)
audio = np.asarray(audio[1],dtype=float)
