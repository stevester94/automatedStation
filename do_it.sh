#python -m pysstv --mode Robot36 $1 output.wav
echo "Generating..."
python -m pysstv --mode MartinM1 --rate 48000 $1 output.wav

echo "Generation complete, playing"
./playFile.py output.wav
