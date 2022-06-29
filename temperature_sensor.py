import RPi.GPIO as GPIO
import Adafruit_DHT
import time

##  pin 18

class TemperatureSensor:
    def __init__(self,digital_pin):
        self.digital_pin = digital_pin
        self.sensor = Adafruit_DHT.DHT11
        
    def readSensor(self):
        umid, temp = Adafruit_DHT.read_retry(self.sensor, self.digital_pin);
        if umid is not None and temp is not None:
            return temp, umid
        else:
            return False, 0
    
    def readAndPost(self,client):
        temp,umid = self.readSensor()
        
        if(not (type(temp) == bool)):
            client.publish("arkaisho_iot_project_temperature",temp)
            client.publish("arkaisho_iot_project_umidity",umid)
            print("posted temperature:",str(temp))
            print("posted umidity:",str(umid))
        else:
            client.publish("arkaisho_iot_project_temperature_failure",0)
            client.publish("arkaisho_iot_project_umidity_failure",0)
            print("posted temperature failure")
            print("posted umidity failure")
            
