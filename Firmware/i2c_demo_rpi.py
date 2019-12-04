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
    previous = 0
    while True:
        gpio.setmode(gpio.BOARD) #gpio.BCM
        gpio.setup(36, gpio.OUT) # to communicate to Arduino if person is seen
        gpio.setup(40, gpio.IN, pull_up_down=gpio.PUD_DOWN) # battery power voltage reading
        status = False
        status = engine.person_detected()
        
        #if not gpio.input(40): #battery is low
            #talk("batt") #communicate that its low
         #   print("batt low")
                                                                                        
        if status and previous:
            gpio.output(36, gpio.HIGH) #person seen, robot stops moving
            #time.sleep(2) # wait 2 seconds for the arduino to stop completely

            # say hi
            talk("hi")
            print("hi")

            # say bye and don't move while you are speaking
            time.sleep(14)
            print("bye")
            talk("bye")
            previous = 0
        else:
            gpio.output(36, gpio.LOW)
            previous = 1
        gpio.cleanup()

if __name__ == '__main__':
    try:
        #previous=1
        print('running')
        main()
        #gpio.cleanup()

    except KeyboardInterrupt:
        print ("Interrupted")
        gpio.cleanup()
        sys.exit(0)
