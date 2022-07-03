import RPi.GPIO as GPIO
import time
from distance_sensor import DistanceSensor
from temperature_sensor import TemperatureSensor
from rain_sensor import RainSensor
from broker_client import BrokerClient

try:
    GPIO.setmode(GPIO.BCM)
    
    client = BrokerClient("broker.emqx.io",1883)
    
    distanceSensor = DistanceSensor(26,22) #trigger pin, echo pin
    temperatureSensor = TemperatureSensor(21) 
    rainSensor = RainSensor(20)
    
    last_iteraction = time.time() - 8
    
    while True:
        if(time.time() - last_iteraction >= 0.3):
            last_iteraction = time.time()

            distanceSensor.readAndPost(client)
            temperatureSensor.readAndPost(client)
            rainSensor.readAndPost(client)
            
finally:
    GPIO.cleanup()


