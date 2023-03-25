#! /usr/bin/env python3

import sounddevice as sd
import soundfile as sf

filename = 'output.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs, blocking=True)
status = sd.wait()  # Wait until file is done playing
