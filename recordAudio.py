#! /usr/bin/env python3

import sounddevice as sd
import soundfile as sf
import numpy as np

while True:
    fs=44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float32')
    print("Recording Audio")
    sd.wait()
    input("Audio recording complete , enter to Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print("Play Audio Complete")
    avgPower = np.mean(myrecording ** 2)
    print( "Avg Power:", avgPower)
