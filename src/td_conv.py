
import scipy.io.wavfile as wav
import numpy as np
import time

fs, x = wav.read('wav/garganta.wav')
fs, y = wav.read('wav/ir2_dc.wav')

t0 = time.time()
z = np.convolve(x, y)
t1 = time.time()

print "Time for time-domain convolution: ", t1-t0

