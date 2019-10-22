//import libraries
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

//create instances of motor class
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *leftMotor = AFMS.getMotor(4);
Adafruit_DCMotor *rightMotor = AFMS.getMotor(3);

//variables for motor speed and sensors
int generalSpeed = 30; //starting speed for motors
//for inputing speeds later
#define prox_sensor A0;
String incomingVal = "";
int s = 0;

void setup() {
  AFMS.begin();
  Serial.begin(9600);
}

void loop() {
  //allows us to change default speed of robot without recompiling code
  if (Serial.available() > 0) { //if there's bytes available
    incomingVal = Serial.readString(); //read the incoming byte
    s = (incomingVal.toInt()); //convert it to an int
    generalSpeed = s + generalSpeed; //change speed based on input
  }


  Serial.print(String(generalSpeed));
  Serial.print(", ");
  Serial.println(String(generalSpeed));

  //robot's normal forward speed
  rightMotor->run(FORWARD); //direction of motors
  leftMotor->run(FORWARD);
  leftMotor ->setSpeed(generalSpeed); //left motor is slightly slower than right
  rightMotor ->setSpeed(generalSpeed);

  distance = analogRead(prox_sensor)
  if (distance > 350) {
    leftMotor ->setSpeed(0); //left motor is slightly slower than right
    rightMotor ->setSpeed(0);
    rightMotor->run(BACKWARD); //direction of motors
    leftMotor->run(BACKWARD);
    leftMotor ->setSpeed(generalSpeed); //left motor is slightly slower than right
    rightMotor ->setSpeed(generalSpeed);
    rightMotor->run(FORWARD); //direction of motors
    leftMotor->run(BACKWARD);
    leftMotor ->setSpeed(generalSpeed); //left motor is slightly slower than right
    rightMotor ->setSpeed(generalSpeed);
  }

}
