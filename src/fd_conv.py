
import scipy.io.wavfile as wav
import numpy as np
import time

fs, x = wav.read('wav/garganta.wav')
fs, y = wav.read('wav/ir2_dc.wav')

t0 = time.time()
X = np.fft.fft(x, len(x)+len(y)-1)
Y = np.fft.fft(y, len(x)+len(y)-1)
Z = X * Y
z = np.real(np.fft.ifft(Z))
t1 = time.time()

print "Time for frequency-domain convolution: ", t1-t0

z = 0.5 * z / np.abs(np.max(z))
wav.write('fd.wav', fs, z)

