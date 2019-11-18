//import libraries
#include <Servo.h>
#include <Wire.h>
//#include "utility/Adafruit_MS_PWMServoDriver.h"

//create instances of Servo class for legs
Servo leftLeg;
Servo rightLeg;
//variables for motor speed and sensors
int generalSpeed = 180; //starting speed for motors

//prox sensor
#define prox_sensor A0
int distance = 5000; //large distance so it doesn't set off stop yet

//String incomingVal = "";
//int s = 0;

//Raspi communication
int cameraPin = A0; //11
int stopPin = A1;

void setup() {
  leftLeg.attach(9);
  rightLeg.attach(10);
  pinMode(cameraPin, OUTPUT);
  pinMode(stopPin, OUTPUT);
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
  

  if (analogRead(cameraPin)>=170){
    //Serial.println("person seen");
    leftLeg.write(0);
    rightLeg.write(0);   
  }
  distance = analogRead(prox_sensor);
  //Serial.print("Distance: ");
  //Serial.println(distance);
  
  if (analogRead(stopPin)>= 170){ //don't move robot when speaker is being used
    leftLeg.write(0);
    rightLeg.write(0);
  }
  else if (distance > 400) {
    //Serial.println("Turning, distance > 400");
    leftLeg.write(generalSpeed+20);
    rightLeg.write(0);
  }
  else{
    leftLeg.write(generalSpeed);
    rightLeg.write(generalSpeed);
    //Serial.println("Both running");
    //Serial.println(generalSpeed);
  }

}
