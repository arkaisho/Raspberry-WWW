# WWW-raspberry

## summary

this project is a wheater watcher that uses raspberry pi, dht-11 and hc-sr04 sensors to mointor an environment

- the hc-sr04 can be used to get the actual status of a door or a window
- the dht-11 is used to monitor the temperature and the umidity of the environment

## setup

1. assembly the sensors on the raspberry correctly and change the code on the main.py to use the corrects GPIO pins to control the sensors
2. also in the main.py file change the broker credentials to acess your broker
3. go to the broker_client.py file and change the topics used on the project to post on twitter based on the subscribed topics
4. go to the twitter_client.py file and change the twitter_auth_keys variable to have your twitter credentials
5. also changes the distance_sensor.py hc-sr04 topic
6. deploy an node-red serve anywhere and use the flows.json file to import some processment nodes to your archtecture
7. create an accoount on [adafruit.io platform](https://io.adafruit.com/) and create the necessary feeds and your desired dashboard
8. configure your node-red server to watch the correct broker, topics and to send the correct data to adafruit feeds
