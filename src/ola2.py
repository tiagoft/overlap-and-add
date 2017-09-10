
import numpy as np


def convolve(x, y, hop_size):
    z = np.zeros(len(x) + len(y) + hop_size) # + hop_size -> avoids a special,
                                         # corner-case scenario

    Y = [np.fft.fft(y[i:i+hop_size], 2*hop_size) for i in xrange(0,\
        len(y)-hop_size, hop_size)]
    X = [np.fft.fft(x[i:i+hop_size], 2*hop_size) for i in xrange(0,\
        len(x)-hop_size, hop_size)]

    start_x = 0
    x_index = 0
    while start_x + hop_size < len(x):
        start_y = 0
        y_index = 0
        while start_y + hop_size < len(y):
            Z = X[x_index] * Y[y_index]
            z[start_x + start_y:start_x+start_y+2*hop_size] += np.real(np.fft.ifft(Z))
            start_y += hop_size
            y_index += 1

        start_x += hop_size
        x_index += 1

    return z

if __name__ == "__main__":
    import time
    import scipy.io.wavfile as wav
    import sys

    if len(sys.argv) < 3:
        print "Usage: python ola2.py signal response output"
        exit()

    fs, x = wav.read(sys.argv[1])
    fs, y = wav.read(sys.argv[2])
    hop_size = 4096*64

    t0 = time.time()
    z = convolve(x, y, hop_size)
    t1 = time.time()

    print "Function time(s): ", t1-t0

    z = 0.5 * z / np.max(np.abs(z))
    wav.write(sys.argv[3], fs, z)

