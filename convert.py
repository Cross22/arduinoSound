import wave, struct, sys

data = []

# Input file needs to be 8 or 16 bit mono PCM at 11kHz
waveFile = wave.open('input.wav', 'r')

length = waveFile.getnframes()
minval= 32767
maxval= -32767

for i in range(0,length):
    waveData = waveFile.readframes(1)
    aSample = int( struct.unpack("<h", waveData)[0] )
    data.append( aSample )
    if  aSample< minval :
      minval= aSample
    if  aSample> maxval :
      maxval= aSample

diff = maxval - minval
morphed = [(sample - minval) * 255 / diff for sample in data]

#test data
#morphed = [0 if (sample % 4)<2 else 255  for sample in range(0,16)]

bitdata = []

for i in xrange(0, (len(morphed)/8)*8,8):
  abyte=0
  for bitpos in range(0,8):
    value = morphed[i+bitpos]
    if value > 127:
      value = 1
    else:
       value = 0
    # add new value as LSB
    abyte = abyte << 1
    abyte = abyte | value

  bitdata.append(abyte)

totalLength = len(bitdata)

# Output header file storing 1-bit samples in PROGMEM

print "#include <avr/pgmspace.h>"
print "const int sndLen =", totalLength, ";"
print "const char sndData[] PROGMEM={"

for i in range(0,totalLength-1):
  print format(bitdata[i], '#04x') + ',',

print format(bitdata[totalLength-1], '#04x') + '};'
