import paho.mqtt.client as paho
import random

##  pin 18

class BrokerClient:
    def __init__(self,BROKER_ADDRESS,BROKER_PORT):
        self.BROKER_ADDRESS = BROKER_PORT
        self.BROKER_PORT = BROKER_PORT

        self.client = paho.Client("wwd-client-"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
        self.client.connect(BROKER_ADDRESS,BROKER_PORT)
        
    def publish(self,TOPIC,DATA):
        self.client.publish(TOPIC,DATA)
        
