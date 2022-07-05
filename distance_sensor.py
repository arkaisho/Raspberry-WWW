import RPi.GPIO as GPIO
import time

##  trigger 7
##  echo 11

class DistanceSensor:
    def __init__(self,trigger_pin,echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.output(trigger_pin, GPIO.LOW)
        time.sleep(2)
        
    def readSensor(self):
        try:
            GPIO.output(self.trigger_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.trigger_pin, GPIO.LOW)
            
            while GPIO.input(self.echo_pin)==0:
                pulse_start_time = time.time()
            while GPIO.input(self.echo_pin)==1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            return round(pulse_duration * 17150, 2)
        
        except:
            return False

    def readAndPost(self,client):
        distance = self.readSensor()
        
        if(not (type(distance) == bool)):
            client.publish("arkaisho_iot_project_proximity",distance)
            print("posted distance:",str(distance))
        else:
            client.publish("arkaisho_iot_project_proximity_failure",0)
            print("posted distance failure")
            