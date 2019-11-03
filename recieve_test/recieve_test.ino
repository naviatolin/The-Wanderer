//Arduino code to receive I2C communication from Raspberry Pi
 
#include <Wire.h>;
 
// Define the slave address of this device.
#define SLAVE_ADDRESS 0x04
// #define SLAVE_ADDRESS 0x05
// #define SLAVE_ADDRESS 0x06
 
// string to store what the RPi sends
String str_recieved_from_RPi = "";
 
void setup() {
 
  // setup the LED
  pinMode(LED_BUILTIN, OUTPUT);
 
  // begin running as an I2C slave on the specified address
  Wire.begin(SLAVE_ADDRESS);
 
  // create event for receiving data
  Wire.onReceive(receiveData);
}
 
void loop() {
  // nothing needed here since we're doing event based code
}
 
void receiveData(int byteCount) {
 
  while ( Wire.available()) {
    str_recieved_from_RPi += (char)Wire.read();
  }
 
  // turn on or off the LED
  if (str_recieved_from_RPi == "on") {
    digitalWrite(LED_BUILTIN, HIGH); 
  }
  if (str_recieved_from_RPi == "off") {
    digitalWrite(LED_BUILTIN, LOW);
  }
 
  str_recieved_from_RPi = "";
 
}
