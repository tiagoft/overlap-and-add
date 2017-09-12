# overlap-and-add
Overlap-and-add convolution in Python

## Overview

This module was built aiming at applying reverberation on audio signals. It
contains several files related to speed improvement requirements. If you are
looking for a quick result, then you should use function `convolve` in file
`ola3.py`:

`import ola3

 ola3.convolve(x, y, hop_size)
 `

## Underlying theory

### What is a convolution and why is it related to reverberation

### Overlap-and-add

## Performance measurements

* Time-domain convolution
* Frequency-domain convolution
* Frequency-domain convolution with single OLA
* Frequency-domain convolution with double OLA

