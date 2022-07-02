import paho.mqtt.client as paho
import random
from twitter_client import TwitterClient
import json

##  pin 18

class BrokerClient:
    def __init__(self,BROKER_ADDRESS,BROKER_PORT):
        self.BROKER_ADDRESS = BROKER_PORT
        self.BROKER_PORT = BROKER_PORT

        self.client = paho.Client(self.generateRandomName())
        self.client.connect(BROKER_ADDRESS,BROKER_PORT)
        
        self.client.subscribe("arkaisho_iot_project_temperature_processed")
        self.client.subscribe("arkaisho_iot_project_umidity_processed")
        
        self.setCallback()
        self.client.loop_start()
        
    def publish(self,topic,data):
        self.client.publish(topic,data)
        
    def subscribe(self,topic):
        self.client.subscribe(topic)
        
    def setCallback(self):
        def on_message(client,userdata,msg):
            twitterCLient = TwitterClient()
            print("received "+str(json.loads(msg.payload.decode()))+" on topic "+ msg.topic)
            if (msg.topic == "arkaisho_iot_project_temperature_processed"):
                twitterCLient.post("The temperature now is "+str(json.loads(msg.payload.decode()))+" ºC")
                print("posted temperature on twitter")
            if (msg.topic == "arkaisho_iot_project_umidity_processed"):
                twitterCLient.post("The umidity now is "+str(json.loads(msg.payload.decode()))+"%")
                print("posted umidity on twitter")
        self.client.on_message = on_message
        
    def generateRandomName(self):
        return "wwd-client-"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
