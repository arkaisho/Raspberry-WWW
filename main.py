import RPi.GPIO as GPIO
import time
from distance_sensor import DistanceSensor
from temperature_sensor import TemperatureSensor
from rain_sensor import RainSensor
from broker_client import BrokerClient

try:
    GPIO.setmode(GPIO.BOARD)
    
    client = BrokerClient("broker.emqx.io",1883)
    
    distanceSensor = DistanceSensor(7,11)
    temperatureSensor = TemperatureSensor(16)
    rainSensor = RainSensor(18)
    
    last_iteraction = time.time() - 8
    
    while True:
        if(time.time() - last_iteraction >= 8):
            last_iteraction = time.time()

            distanceSensor.readAndPost(client)
            temperatureSensor.readAndPost(client)
            rainSensor.readAndPost(client)
            
finally:
    GPIO.cleanup()


