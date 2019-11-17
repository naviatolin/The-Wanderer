//import libraries
#include <Servo.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

//create instances of motor class
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *leftMotor = AFMS.getMotor(4);
Adafruit_DCMotor *rightMotor = AFMS.getMotor(3);

//servo
Servo headServo;
int angle = 0;
//variables for motor speed and sensors
int generalSpeed = 50; //starting speed for motors
int distance = 5000; //large distance so it doesn't set off stop
//for inputing speeds later
#define prox_sensor A0
String incomingVal = "";
int s = 0;
//Raspi communication
int raspiPin = A0; //11

void setup() {
  AFMS.begin();
  headServo.attach(9);
  //pinMode(LED_BUILTIN, OUTPUT);
  pinMode(raspiPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  headServo.write(angle);
  //allows us to change default speed of robot without recompiling code
  if (Serial.available() > 0) { //if there's bytes available
    incomingVal = Serial.readString(); //read the incoming byte
    s = (incomingVal.toInt()); //convert it to an int
    angle = s + angle; //change speed based on input
    headServo.write(angle);
    Serial.println(angle);
  }

  if (analogRead(raspiPin)>=170){
    Serial.println("person seen");
    //rightMotor ->setSpeed(0);
    //leftMotor ->setSpeed(0);    
  }
  //blinks on board light if raspi sees a person
  //if (digitalRead(raspiPin) == HIGH){
  //  digitalWrite(LED_BUILTIN, HIGH); 
  //}
  //else {
  //  digitalWrite(LED_BUILTIN, LOW);
  //}

  //Serial.print(String(generalSpeed));
  //Serial.print(", ");
  //Serial.println(String(generalSpeed));

  //robot's normal forward speed
  rightMotor->run(FORWARD); //direction of motors
  leftMotor->run(FORWARD);
  

  distance = analogRead(prox_sensor);
  //Serial.print("Distance: ");
  //Serial.println(distance);
  if (distance > 400) {
    //Serial.println("Turning, distance > 350");
    leftMotor ->setSpeed(generalSpeed+20); //left motor is slightly slower than right
    rightMotor ->setSpeed(0);
  }
  else{
    leftMotor ->setSpeed(generalSpeed+5); //left motor is slightly slower than right
    rightMotor ->setSpeed(generalSpeed);
  }

}
