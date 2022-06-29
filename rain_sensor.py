import RPi.GPIO as GPIO

##  digital pin 16

class RainSensor:
    def __init__(self,digital_pin,):

        self.digital_pin = digital_pin
        GPIO.setup(digital_pin, GPIO.IN)
        
    def readSensor(self):
        return GPIO.input(self.digital_pin)
        

    def readAndPost(self,client):
        distance = self.readSensor()
        client.publish("arkaisho_iot_project_rain",distance)
        print("posted rain:",str(distance))
