// Sound samples are defined in sound.h
#include "sound.h"

// Connect piezo speaker (+) to pin 8 and (-) to GND
// Connect push button to pin 9 and GND

#define outPin 8
#define buttonPin 9

void setup() {
  pinMode(outPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

}

void loop() {
  // Wait for button press
  if (digitalRead(buttonPin)!=LOW)
    return;
  
  // Read 8 bits out of ROM and send to speaker
  for (int i=0; i< sndLen; ++i) {
    uint8_t myChar =  pgm_read_byte_near(sndData + i);
    for (uint8_t bitpos=0; bitpos<8; ++bitpos) {
      uint8_t curr = (myChar & 0x80);
      myChar = myChar << 1;
      
      digitalWrite(outPin, curr ? HIGH : LOW);

      // This delay assumes 11kHz sample rate
      delayMicroseconds(75);        
    }
  }

    // Arbitrary delay
    delayMicroseconds(2000);
}
