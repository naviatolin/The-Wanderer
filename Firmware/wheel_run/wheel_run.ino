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
int battInputPin = A2; //reads the current battery voltage
int battOutputPin = 11; //outputs a battery low signal to raspi

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

  Serial.print("Battery reading: ");
  Serial.print(analogRead(battInputPin)); //analog voltage is 0-1024 where 1024 is 5V
  //low battery signal is for 4.8V or analog V 985
  if (analogRead(battInputPin)<=985){
    Serial.println(" -> Low Battery");
    digitalWrite(battOutputPin, LOW); //low battery signal to raspi
  }
  else{
    Serial.println(" -> Good Battery");
    digitalWrite(battOutputPin, HIGH);
  }
  
  distance = analogRead(prox_sensor);
  //Serial.print("Distance: ");
  //Serial.println(distance);

  //Serial.print("Seen: ");
  //Serial.println(analogRead(cameraPin)>=170);
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
    Serial.println("Both running");
    leftLeg.write(leftSpeed);
    rightLeg.write(rightSpeed);
    //Serial.print("Speed: ");
    //Serial.println(rightSpeed);
  }

}
