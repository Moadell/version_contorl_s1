#this comment was added by ym
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

try:
    while True: # Run forever
        GPIO.output(8, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(8, GPIO.LOW) # Turn off
        sleep(1) # Sleep for 1 second\

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print('Exit')
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print ("Other error or exception occurred!" )
    # this is a new comment
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  

