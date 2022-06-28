import RPi.GPIO as GPIO
import time
from distance_sensor import DistanceSensor
from temperature_sensor import TemperatureSensor
from broker_client import BrokerClient

try:
    GPIO.setmode(GPIO.BOARD)
    
    client = BrokerClient("broker.emqx.io",1883)
    
    distanceSensor = DistanceSensor(7,11)
    temperatureSensor = TemperatureSensor(18)
    
    repetitions = 5
    last_iteraction = time.time() - 8
    
    while repetitions>0:
        if(time.time() - last_iteraction >= 8):
            last_iteraction = time.time()
            repetitions-=1
            
            distance = distanceSensor.readSensor()
            client.publish("arkaisho_iot_project_proximity",distance)
            
            temp,umid = temperatureSensor.readSensor()
            if(not (type(temp) == bool)):
                client.publish("arkaisho_iot_project_temperature",temp)
                client.publish("arkaisho_iot_project_umidity",umid)
            else:
                client.publish("arkaisho_iot_project_temperature_failure",0)
                client.publish("arkaisho_iot_project_umidity_failure",0)

finally:
    GPIO.cleanup()


