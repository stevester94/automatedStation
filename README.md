# What it does
Listens to audio-in (Microphone / aux), and past a hardcoded threshold will play a pre-generated SSTV wav file

# System Dependencies
Requires libportaudio2

# Preparing
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt

# Running
./station.py
