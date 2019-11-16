import RPi.GPIO as gpio
import smbus
import time
import sys
from cv_person_detection import ProcessingEngine

#bus = smbus.SMBus(1)
#address = 0x04

def main():
    engine = ProcessingEngine(debug=True)
    engine.turn_on()
    while True:
        gpio.setmode(gpio.BOARD) #gpio.BCM
        gpio.setup(36, gpio.OUT)
        gpio.setup(40, gpio.IN, pull_up_down = gpio.PUD_DOWN)
        status = False
        status = engine.person_detected()
        if status:
            print('seen')
            gpio.output(36, gpio.HIGH) #17, status
            am_i_stopped = gpio.input(40)
            if am_i_stopped:
                
        else:
            gpio.output(36, gpio.LOW)
        #bus.write_byte(address, 1 if status else 0)
        #print("Arduino answer to RPI:", bus.read_byte(address))
        time.sleep(1)
        gpio.cleanup()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print ("Interrupted")
        gpio.cleanup()
        sys.exit(0)
