import scipy.io.wavfile as wav
import numpy as np
import time

fs, x = wav.read('wav/garganta.wav')
fs, y = wav.read('wav/ir2_dc.wav')

hop_size = 4096*64

print "Entering measurement part"

t0 = time.time()

z = np.zeros(len(x) + len(y) + hop_size) # + hop_size -> avoids a special,
                                         # corner-case scenario

print "Destiny memory allocated"

Y = [np.fft.fft(y[i:i+hop_size], 2*hop_size) for i in xrange(0,\
        len(y)-hop_size, hop_size)]

print "Starting..."

start_x = 0
while start_x + hop_size < len(x):
    start_y = 0
    y_index = 0
    X = np.fft.fft(x[start_x:start_x+hop_size], 2*hop_size) # This can be
                                                            # out of the loop
                                                            # in offline
                                                            # applications -
                                                            # and results can
                                                            # be saved in
                                                            # real-time
                                                            # applications
    while start_y + hop_size < len(y):
        Z = X * Y[y_index]
        z[start_x + start_y:start_x+start_y+2*hop_size] += np.real(np.fft.ifft(Z))
        start_y += hop_size
        y_index += 1

    start_x += hop_size
    print len(x) - start_x

t1 = time.time()

print "Time for ola2-frequency-domain convolution: ", t1-t0

z = 0.5 *  z / np.abs(max(z))
wav.write('ola2.wav', fs, z)
