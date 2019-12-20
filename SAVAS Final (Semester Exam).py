# Code created/revised by Jordan King, Robert Smith
# and Arthur Ethan Thomas Valdez III
# Last edited 12/19/19

# The MQ-2 sensor has to be connected to pin 1 for power (VCC), pin 6 for
# ground (GND) and pin 3 for signal (Do).

import RPi.GPIO as GPIO
from time import sleep
import sys
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pin for MQ-2
GPIO.setup(40, GPIO.OUT, initial = GPIO.HIGH) # pin for red LED
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW) # pin for green LED
GPIO.setup(32, GPIO.OUT, initial = GPIO.LOW) # pin for buzzer

GPIO.add_event_detect(3, GPIO.RISING) # detects sudden changes in sensor input

try:
    while True:
        if GPIO.event_detected(3): # if sudden change, then smoke detected
            GPIO.output(40, GPIO.LOW)  # red
            GPIO.output(22, GPIO.HIGH) # green
            GPIO.output(32, GPIO.HIGH) # buzzer
            print("\n=================")
            print("SMOKE DETECTED!!!")
            print("=================\n")
            sleep(3)
        else:
            GPIO.output(40, GPIO.HIGH) # red
            GPIO.output(22, GPIO.LOW)  # green
            GPIO.output(32, GPIO.LOW)  # buzzer
            print("Searching for smoke...")
            sleep(0.5)
except KeyboardInterrupt: # press Ctrl+C to end program
    GPIO.cleanup()
    sys.exit()
