import scipy.io.wavfile as wav
import numpy as np
import time

fs, x = wav.read('wav/garganta.wav')
fs, y = wav.read('wav/ir2_dc.wav')



hop_size = 512

print "Entering measurement part"

t0 = time.time()

z = np.zeros(len(x) + len(y) + hop_size) # + hop_size -> avoids a special,
                                         # corner-case scenario

print "Destiny memory allocated"

Y = np.fft.fft(y, hop_size+len(y)-1)


print "Starting..."
start = 0
while start + hop_size < len(x):
    X = np.fft.fft(x[start:start+hop_size], hop_size+len(y)-1)
    Z = X * Y
    z[start:start+hop_size] += np.fft.ifft(Z)
    start += hop_size
    print len(x) - start

t1 = time.time()

print "Time for ola1-frequency-domain convolution: ", t1-t0

