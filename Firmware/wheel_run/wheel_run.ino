//import libraries
#include <Servo.h>
#include <Wire.h>

//create instances of Servo class for legs
Servo leftLeg;
Servo rightLeg;
//variables for motor speed and sensors
int leftSpeed = 60; //starting speed for motors, is forward <90, 0 is full speed
int rightSpeed = 180-leftSpeed;

//prox sensor
#define prox_sensor A0
int distance = 0;

//Raspi communication
int cameraPin = A1; //notification from raspi for seeing a person 
int battInputPin = A2; //reads the current battery voltage
int battOutputPin = 8; //outputs a battery low signal to raspi
float battVolt = 0;  //to track battery voltage

float getBatteryVoltage(int batteryPin){
  // Convert the analogRead to battery voltage
  // 5V / 1024 to go from Arduino ADC to Measured Voltage
  // *4.34 to go from Measured Voltage to Battery Voltage
  // (Divider divides by 4.34)
  return (float)analogRead(batteryPin) * 5 * 4.34 / 1024;
}

void setup() {
  leftLeg.attach(9);
  rightLeg.attach(10);
  pinMode(battOutputPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  battVolt = getBatteryVoltage(battInputPin); // read battery voltage
  Serial.print("Battery reading: ");
  Serial.println(battVolt);
  digitalWrite(battOutputPin, battVolt < 11.5); //Indicate high if battery voltage is less than 11.5

  //Serial.print("Distance: ");
  //Serial.println(distance);
  distance = analogRead(prox_sensor);

  //Serial.print("Seen: ");
  Serial.println(analogRead(cameraPin)>=170);
  if (analogRead(cameraPin)>=170){ // Robot stops when speaker is being used
    Serial.println("Stopped while talking");
    leftLeg.write(90);
    rightLeg.write(90);
  }
  else if (distance > 300) {
    Serial.println("Turning, distance > 300");
    leftLeg.write(140); // one of the motors is reverse polarity, so one wheel goes backwards
    rightLeg.write(140);
  }
  else if (analogRead(cameraPin)<170){
    Serial.println("Going Forward");
    //Serial.print("Speed: ");
    //Serial.println(rightSpeed);
    leftLeg.write(leftSpeed);
    rightLeg.write(rightSpeed);
  }
}
