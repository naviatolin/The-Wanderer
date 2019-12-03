//import libraries
#include <Servo.h>
#include <Wire.h>
//#include "utility/Adafruit_MS_PWMServoDriver.h"

//create instances of Servo class for legs
Servo leftLeg;
Servo rightLeg;
//variables for motor speed and sensors
int leftSpeed = 60; //starting speed for motors, is forward <90, 0 is full speed
int rightSpeed = 180-leftSpeed;

//prox sensor
#define prox_sensor A0
int distance = 5000; //large distance so it doesn't set off stop yet

//String incomingVal = "";
//int s = 0;

//Raspi communication
int cameraPin = A1; //notification from raspi for seeing a person
int battOutputPin = A2; //outputs a battery low signal to raspi 
int battInputPin = A3; //reads the current battery voltage


void setup() {
  leftLeg.attach(9);
  rightLeg.attach(10);
  pinMode(cameraPin, INPUT);
  pinMode(battInputPin, INPUT);
  pinMode(battOutputPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  delay(1000);
  //Serial.print("Seen: ");
  //Serial.println(analogRead(cameraPin)>=170);
  int batt = analogRead(battInputPin); //This looks pretty good
  analogWrite(battOutputPin, batt/12); //isn't working to send to raspi yet
  Serial.print("Battery reading: ");
  Serial.print(batt);
  Serial.print(" -> ");
  Serial.println(batt/12);
  
  distance = analogRead(prox_sensor);
  Serial.print("Distance: ");
  Serial.println(distance);
  
  if (analogRead(cameraPin)>=170){ //don't move robot when speaker is being used
    Serial.println("Stopped while talking");
    leftLeg.write(90);
    rightLeg.write(90);
  }
  else if (distance > 300) {
    Serial.println("Turning, distance > 400");
    leftLeg.write(140);//one of the motors is reverse polarity
    rightLeg.write(140); //
  }
  else if (analogRead(cameraPin)<170){
    Serial.println("Both running");
    leftLeg.write(leftSpeed);
    rightLeg.write(rightSpeed);
    
    //Serial.print("Speed: ");
    //Serial.println(generalSpeed);
  }

}
