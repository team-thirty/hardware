import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import random
import requests 
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)   # Set pin 5 to be an output pin and set initial value to low (off)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

verylow_pin = 29
low_pin = 31
medium_pin = 33
high_pin = 35
veryhigh_pin = 37
nocharge_pin = 23

sleep_time = 5

#the readings range: (very low, low, medium, high, very high), so that's 5 modes
#plus another one for when nothing is charging

def lights(reading):
    if reading == 1:
        GPIO.output(verylow_pin, GPIO.HIGH) # Turn on
        pass
        """sleep(sleep_time)                  # Sleep for 1 second

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off"""
    elif reading == 2:
        GPIO.output(verylow_pin, GPIO.HIGH) # Turn on
        GPIO.output(low_pin, GPIO.HIGH) # Turn on
        pass
        """sleep(sleep_time)                  # Sleep for 1 second

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
        GPIO.output(low_pin, GPIO.LOW)  # Turn off"""
    elif reading == 3:
        GPIO.output(verylow_pin, GPIO.HIGH) # Turn on
        GPIO.output(low_pin, GPIO.HIGH) # Turn on
        GPIO.output(medium_pin, GPIO.HIGH) # Turn on
        pass
        """sleep(sleep_time)                  # Sleep for 1 second

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
        GPIO.output(low_pin, GPIO.LOW)  # Turn off
        GPIO.output(medium_pin, GPIO.LOW)  # Turn off"""
    elif reading == 4:
        GPIO.output(verylow_pin, GPIO.HIGH) # Turn on
        GPIO.output(low_pin, GPIO.HIGH) # Turn on
        GPIO.output(medium_pin, GPIO.HIGH) # Turn on
        GPIO.output(high_pin, GPIO.HIGH) # Turn on
        pass
        """sleep(sleep_time)                  # Sleep for 1 second

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
        GPIO.output(low_pin, GPIO.LOW)  # Turn off
        GPIO.output(medium_pin, GPIO.LOW)  # Turn off
        GPIO.output(high_pin, GPIO.LOW)  # Turn off"""
    elif reading == 5:
        GPIO.output(verylow_pin, GPIO.HIGH) # Turn on
        GPIO.output(low_pin, GPIO.HIGH) # Turn on
        GPIO.output(medium_pin, GPIO.HIGH) # Turn on
        GPIO.output(high_pin, GPIO.HIGH) # Turn on
        GPIO.output(veryhigh_pin, GPIO.HIGH) # Turn on
        pass
        """sleep(sleep_time)                  # Sleep for 1 second

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
        GPIO.output(low_pin, GPIO.LOW)  # Turn off
        GPIO.output(medium_pin, GPIO.LOW)  # Turn off
        GPIO.output(high_pin, GPIO.LOW)  # Turn off
        GPIO.output(veryhigh_pin, GPIO.LOW)  # Turn off"""
    elif reading == 0:
        GPIO.output(nocharge_pin, GPIO.HIGH) # Turn on
        #sleep(sleep_time)                  # Sleep for 1 second
        #GPIO.output(nocharge_pin, GPIO.LOW)  # Turn off
        pass

    """GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
    GPIO.output(low_pin, GPIO.LOW)  # Turn off
    GPIO.output(medium_pin, GPIO.LOW)  # Turn off
    GPIO.output(high_pin, GPIO.LOW)  # Turn off
    GPIO.output(veryhigh_pin, GPIO.LOW)  # Turn off"""

"""while True:
    reading = random.randint(0,6)
    lights(reading)"""

while True:
    try:
        
        reading = requests.get("https://team30app0.azurewebsites.net/get_charging_state")
        reading = reading.json()["state"]
        reading = int(reading)

        GPIO.output(verylow_pin, GPIO.LOW)  # Turn off
        GPIO.output(low_pin, GPIO.LOW)  # Turn off
        GPIO.output(medium_pin, GPIO.LOW)  # Turn off
        GPIO.output(high_pin, GPIO.LOW)  # Turn off
        GPIO.output(veryhigh_pin, GPIO.LOW)  # Turn off
        GPIO.output(nocharge_pin, GPIO.LOW)  # Turn off
        
        lights(reading)
        sleep(sleep_time)
        
    except:
        sleep(sleep_time)