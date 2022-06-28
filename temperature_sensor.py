import RPi.GPIO as GPIO
import Adafruit_DHT
import time

##  pin 18

class TemperatureSensor:
    def __init__(self,PIN_TEMPERATURE):
        self.PIN_TEMPERATURE = PIN_TEMPERATURE
        self.sensor = Adafruit_DHT.DHT11
        
    def readSensor(self):
        umid, temp = Adafruit_DHT.read_retry(self.sensor, self.PIN_TEMPERATURE);
        if umid is not None and temp is not None:
            return temp, umid
        else:
            return False, 0

