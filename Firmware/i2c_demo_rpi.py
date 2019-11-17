import RPi.GPIO as gpio
import smbus
import time
import sys
from cv_person_detection import ProcessingEngine
from sound import talk

#bus = smbus.SMBus(1)
#address = 0x04

def main():
    engine = ProcessingEngine(debug=True)
    engine.turn_on()
    while True:
        gpio.setmode(gpio.BOARD) #gpio.BCM
        gpio.setup(36, gpio.OUT) # am I seeing people
        gpio.setup(40, gpio.OUT) # should I stop
        status = False
        status = engine.person_detected()
        if status:
            gpio.output(36, gpio.HIGH)
            time.sleep(2) # wait 2 seconds for the arduino to stop completely

            # say hi and don't move while you are speaking
            done_hi = talk("hi")
            while done_hi is 0:
                gpio.output(40,gpio.HIGH)

            # say bye and don't move while you are speaking
            done_bye = talk("bye")
            while done_bye is 0:
                gpio.output(40,gpio.HIGH)
            
            gpio.output(40, gpio.LOW)
            
        else:
            gpio.output(36, gpio.LOW)
            gpio.output(40, gpio.LOW)

        time.sleep(1)
        gpio.cleanup()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print ("Interrupted")
        gpio.cleanup()
        sys.exit(0)
