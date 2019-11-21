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
int cameraPin = A1; //11
//int stopPin = A2;

void setup() {
  leftLeg.attach(9);
  rightLeg.attach(10);
  pinMode(cameraPin, OUTPUT);
  //pinMode(stopPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //allows us to change default speed of robot without recompiling code
  //if (Serial.available() > 0) { //if there's bytes available
  //  incomingVal = Serial.readString(); //read the incoming byte
  //  s = (incomingVal.toInt()); //convert it to an int
  //  angle = s + angle; //change speed based on input
  //  headServo.write(angle);
  //  Serial.println(angle);
  //}

  //robot's normal forward speed
  delay(1000);
  //Serial.print("Seen: ");
  //Serial.println(analogRead(cameraPin)>=170);
  //Serial.print(", Held: ");
  //Serial.println(analogRead(stopPin));
  
  //if (analogRead(cameraPin)>=170){
  //  Serial.println("Person seen, stopping");
  //  leftLeg.write(90); //90 is stop
  //  rightLeg.write(90);   
  //}
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
    leftLeg.write(140);//leftSpeed-20
    rightLeg.write(140); //rightSpeed+20
  }
  else if (analogRead(cameraPin)<170){
    Serial.println("Both running");
    leftLeg.write(leftSpeed);
    rightLeg.write(rightSpeed);
    //Serial.println(generalSpeed);
  }

}
