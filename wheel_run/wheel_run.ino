//import libraries
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

//create instances of motor class
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *leftMotor = AFMS.getMotor(4);
Adafruit_DCMotor *rightMotor = AFMS.getMotor(3);

//variables for motor speed and sensors
int reflectPinLeft = A2; //IR sensors
int reflectPinRight = A3;
int generalSpeed = 20; //starting speed for motors

//for inputing speeds later
String incomingVal = "";
int s = 0;

void setup() {
  AFMS.begin();
  pinMode(reflectPinLeft, INPUT);
  pinMode(reflectPinRight, INPUT);
  Serial.begin(9600);
}

void loop() {
  //allows us to change default speed of robot without recompiling code
  if (Serial.available() > 0) { //if there's bytes available
    incomingVal = Serial.readString(); //read the incoming byte
    s = (incomingVal.toInt()); //convert it to an int
    generalSpeed = s + generalSpeed; //change speed based on input
  }

  //prints sensor values and current speeds
  Serial.print(String(analogRead(reflectPinLeft)));
  Serial.print(", ");
  Serial.print(String(analogRead(reflectPinRight)));
  Serial.print(", ");
  Serial.print(String(generalSpeed + 5));
  Serial.print(", ");
  Serial.println(String(generalSpeed));

  //robot's normal forward speed
  rightMotor->run(FORWARD); //direction of motors
  leftMotor->run(FORWARD);
  leftMotor ->setSpeed(generalSpeed + 5); //left motor is slightly slower than right
  rightMotor ->setSpeed(generalSpeed);

  // if right sensor detects line, robot turns left
  if (analogRead(reflectPinRight) > 200) {
    leftMotor->run(FORWARD);
    leftMotor->setSpeed(generalSpeed + 15); //the left motor runs forward faster
    rightMotor->run(BACKWARD);
    rightMotor->setSpeed(generalSpeed - 5); //the right motor runs backwards briefly
    delay(15);

    //print out sensor and speed values during turn
    Serial.print(String(analogRead(reflectPinLeft)));
    Serial.print(", ");
    Serial.print(String(analogRead(reflectPinRight)));
    Serial.print(", ");
    Serial.print(String(generalSpeed + 15));
    Serial.print(", ");
    Serial.println(String(generalSpeed - 5));
  }
  //if left sensor detects line, robot turns right
  if (analogRead(reflectPinLeft) > 300) {
    rightMotor->run(FORWARD);
    rightMotor->setSpeed(generalSpeed + 15); //the right motor runs forward faster
    leftMotor->run(BACKWARD);
    leftMotor->setSpeed(generalSpeed - 5); //left motor runs backwards briefly
    delay(15);

    //print out sensor and speed values during turn
    Serial.print(String(analogRead(reflectPinLeft)));
    Serial.print(", ");
    Serial.print(String(analogRead(reflectPinRight)));
    Serial.print(", ");
    Serial.print(String(generalSpeed - 5));
    Serial.print(", ");
    Serial.println(String(generalSpeed + 15));

  }

}
