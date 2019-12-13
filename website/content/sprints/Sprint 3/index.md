---
title: 'Sprint 3'
---
## Goals

- Integrate mechanical electrical and software systems
- Scale up to final size
- Increase mechanical robustness (no hot glue!)
- Run on battery power

## Progress:
- Attached new motor servos
- Added battery and convert its power for other components
- Arduino and Raspi wired to each other on chassis and communicate back and forth, with Arduino controlling movement and the Raspi monitoring computer vision and using the speaker
- Stronger larger design that is wood glued, not hot glued
- Added ribs on chassis over electronics to give round shape to body and fur

<!--more-->

## Mechanical

- Improve walking, by making legs thicker, making a CAD assembly, 3D printing crank part (so its a stronger and spaced right)


![asdf](IMG_3404.jpg)
<img src="/IMG_3404.jpg"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

![asdf](76190045_2382289258698762_1948857834514939904_n.jpg)
<img src="/76190045_2382289258698762_1948857834514939904_n.jpg"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

## Electrical

- Move to battery power
- Wiring to connect Raspi, Arduino, battery, and components

<img src="/Untitled.png"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

## Software

- Add sounds, and change in movement to program interactive behavior
- Add lines of code to .bashrc Raspi file, so that the Raspi runs the computer vision/main code from start-up
- Connect Raspi GPIO pins to Arduino to communicate the "stop" signal when Raspi sees a person and is talking. Arduino should stop moving.

<img src="/stopping_gif.gif"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

<img src="/diagram.png"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

- Get speaker working and saying one sound (a roar) when it sees a person

## Design

<img src="/IMG_3407.jpg"
     alt="Markdown Monster icon"
     style="float: center; margin-right: 150px; margin-left: 150px; width:500px;" />

- Iterate on appearance, creating round hardboard ribs to put fur over parts, putting on fur, putting on eyes, making it more chunky (more towards square wall-e and round ideas)