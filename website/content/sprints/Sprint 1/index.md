---
title: 'Sprint 1'
---

## Goals:

- Make a robot that walks around and can sense walls
- Show proof-of-concept for components
    - Computer vision demonstration
    - Walking mechanism


## Progress:

- Robot walks and can sense walls. It is able to turn before the wall
    - Computer vision can recognize people
    - Basic walking mechanism
<!--more-->
## Mechanical

- Create a rectangular chassis to mount motors, wheels, IR sensor, and Arduino
    - There are three wheels, one on front two on back
    - Moves forward with 2 legs driven by motors. The legs spin around with the foot facing downward, dragging it forward
    - Mount IR sensor on the front to sense walls


{{< figure src="sprint1pic1.jpg" width="400px">}}
{{< figure src="first_proto.png" width="400px">}}


## Software

- Code that turns robot before wall, and runs legs

## Design

- Robot wobbles and walks slowly