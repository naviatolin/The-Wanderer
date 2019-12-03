import RPi.GPIO as gpio
import smbus
import time
import sys

#bus = smbus.SMBus(1)
#address = 0x04

def main():
    gpio.setmode(gpio.BOARD) #gpio.BCM
    gpio.setup(36, gpio.OUT)
    status = False
    gpio.output(36, gpio.HIGH) #17, status
    time.sleep(1)
    #gpio.output(36, gpio.LOW)
    gpio.cleanup()

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        print ("Interrupted")
        gpio.cleanup()
        sys.exit(0)

