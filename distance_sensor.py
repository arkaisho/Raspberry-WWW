import RPi.GPIO as GPIO
import time

##  trigger 7
##  echo 11

class DistanceSensor:
    def __init__(self,PIN_DISTANCE_TRIGGER,PIN_DISTANCE_ECHO):

        self.PIN_DISTANCE_TRIGGER = PIN_DISTANCE_TRIGGER
        self.PIN_DISTANCE_ECHO = PIN_DISTANCE_ECHO

        GPIO.setup(PIN_DISTANCE_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_DISTANCE_ECHO, GPIO.IN)
        GPIO.output(PIN_DISTANCE_TRIGGER, GPIO.LOW)
        
    def readSensor(self):
        GPIO.output(self.PIN_DISTANCE_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.PIN_DISTANCE_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_DISTANCE_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(self.PIN_DISTANCE_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        return round(pulse_duration * 17150, 2)
