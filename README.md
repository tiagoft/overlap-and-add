# overlap-and-add
Overlap-and-add convolution in Python

## Overview

This module was built aiming at applying reverberation on audio signals. It
contains several files related to speed improvement requirements. If you are
looking for a quick result, then you should use function `convolve` in file
`ola3.py`:

`import ola3`

`ola3.convolve(x, y, hop_size)`

## Underlying theory

When sound is produced within a room, it propagates towards the listener. This
is called *direct sound*. However, sound also propagates towards the wall, then
it reflects and propagates towards both the listener and the other walls. This
results in a series of *reflections*, which essentially depend on the room
shape, size and material.

A room, in regular conditions, can be considered a linear system, which means
that if two sources produce sound within the room then the listener will hear
the sum of the individual sounds. This is similar to playing two instruments
together and, if you like other forms of art, it is also similar to overlaying
semi-transparent photographs. Because of the linear property, the sum of the
direct sound with the reflections - that is, the reverberated sound - is equal
to the convolution between the original sound signal and the room's *impulse
response*, which is literaly the sound that is heard when an impulse is produced
within the room.

The convolution is an operation that is very costly to calculate directly - its
complexity is O(N^2), which makes it very slow, even for offline applications.
However (and you might want to refer to a good DSP book for this demonstration),
the convolution in the time domain corresponds to a multiplication (which is
O(N)) in the frequency domain. Hence, using the FFT (O(N logN)) and its inverse,
we can transform our time-domain signals into the frequency domain, multiply
them and then transform them back to the time domain, which is much faster than
the direct, time-domain operation.

One disadvantage of the frequency-domain convolution is that it requires the
whole audio signal to be known before yielding the results. This prevents the
convolution to be performed in real-time. The solution for this is to divide the
input signal into blocks of known length and then calculating the convolution in
each of the blocks. The convolution is a linear operation, hence the sum of the
blockwise convolutions is equal to the convolution of the sum of all blocks.

Doing this with a very long impulse response signal requires a large FFT to be
computed, which is problematic because it requires a lot of memory. Hence, we
can also divide the impulse response into blocks and use these blocks to compute
the convolution with each block of the input signal.

This package contains some code to perform blockwise convolutions and some code
to measure performance of each variation, which are shown below.

## Performance measurements

* Time-domain convolution
* Frequency-domain convolution (no blocks)
* Frequency-domain convolution (only input uses blocks)
* Frequency-domain convolution (both input and impulse response use blocks)

