#! /usr/bin/env python3

import sounddevice as sd
import soundfile as sf
import numpy as np

THRESHOLD = 0.0005

def playSstv():
    filename = 'output.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')  
    sd.play(data, fs, blocking=True)
    status = sd.wait()  # Wait until file is done playing   

def playTone():
    dur = 10
    fs = 44100
    f = 1000
    t = np.arange(0,dur,1/fs)
    x = np.sin(2*np.pi*f*t)
    sd.play(x, fs, blocking=True)
    status = sd.wait()  # Wait until file is done playing   

trigger = False
triggerCooldown = 0
while True:
    fs=44100
    duration = 1  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float64')
    print("Recording Audio")
    sd.wait()
    #print("Audio recording complete , Play Audio")
    #sd.play(myrecording, fs)
    #sd.wait()
    #print("Play Audio Complete")
    #print( type(myrecording) )
    avgPower = np.mean(myrecording ** 2)
    print( "Avg Power:", avgPower)

    if triggerCooldown > 0:
        triggerCooldown -= 1
        print( "triggerCooldown at", triggerCooldown )
   
    if not trigger and avgPower > THRESHOLD and triggerCooldown == 0:
        trigger = True
        print( "Arming trigger" )
    elif trigger and avgPower > THRESHOLD and triggerCooldown == 0:
        print( "Waiting for clear channel" )
    elif trigger and avgPower < THRESHOLD:
        trigger = False
        triggerCooldown = 5
        print( "Trigger!" )
        playSstv()
        #playTone()
