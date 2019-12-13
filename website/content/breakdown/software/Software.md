---
title: 'Software Breakdown'
---

Github: [https://github.com/naviatolin/The-Wanderer](https://github.com/naviatolin/The-Wanderer)
<!--more-->

### Communication between Raspberry Pi and Arduino

Initially, we were going to use some form of serial communication to exchange information between the Raspberry Pi and Arduino. We successfully prototyped this but eventually scrapped it in favor of simple digital pin indicators, even though this meant some extra hardware. The Raspberry Pi sends a digital signal to the Arduino to indicate the presence of a person, at which point the Arduino stops the motors. The Raspberry Pi is 3.3V logic level, so the Arduino measures this digital signal on an analog pin. In the final product, we set the Arduino to test the battery level and relay whether it is below a set level or not to the Raspberry Pi via a digital pin. 

### Arduino "Wheelrun" Code

The Arduino's main function is to control the movement of the robot. The proxPin reads analog voltage from the IR sensor and at a certain threshold the code has the robot turn (one wheel going forward, the other backward) in order to avoid obstacles. The Arduino also monitors the battery level through the battInputPin and converts the signal to a High or Low out of the battOutputPin to communicate low battery to the Raspi. From the Raspi, the cameraPin tells the Arduino to stop when the Raspi sees a person.

### Raspberry Pi "I2C_demo" Code

For part of our prototyping process, we explored having the Raspberry Pi and Arduino communicate with I2C. Although we used digital pins in the end, we did successfully exchange information between them using I2C. In I2C_demo we have the Raspberry Pi look for people through the Raspi camera, then tell the Arduino if it sees them through the pin 36. The Raspi also handles the speaker for the robot. If it receives a low battery signal from the Arduino through pin 40, it outputs a "low battery" sound. When the camera sees a person it outputs a "hello" noise and after 8 seconds, roughly the time it takes to process that a person would no longer be there, it outputs a "goodbye" noise.

### Computer Vision Code

Using OpenCV for Python, we used an implementation of the YOLO-COCO algorithm from a previous software project. This is the most computationally intense part of the project and is why we added the Raspberry Pi to the Wanderer. YOLO-COCO breaks in image down into an array of variously sized pieces (called a blob) and treats each with a large (300MB) weights file to detect a wide range of objects. To minimize computation time and increase robot responsiveness, we reduced the blob size to a minimum, sacrificing some detection ability. In the future, we would probably switch to a more specialized version of YOLO-COCO to reduce computational load.