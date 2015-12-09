# arduinoSound
Simple converter and example of digital audio playback on Arduino


Usage:
convert.py looks for a file called input.wav - this needs to be 8 or 16 bit PCM Mono at 11kHz.
The output is a C header file with the sample data at 1-bit.

$python convert.py > sound.h

In the arduinoCode folder is the playback code which in turn includes the generated sound.h file and plays it via a piezo speaker connected to Pin 8.
