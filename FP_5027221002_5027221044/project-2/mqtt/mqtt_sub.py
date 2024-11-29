import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and$

def on_connect(client, userdata, flags, rc):
    client.subscribe("/kel14/room/led")

def on_message(client, userdata, message):
    if str(message.payload.decode("utf-8"))=="On":
        GPIO.output(12, GPIO.HIGH) # Turn on
    else:
        GPIO.output(12, GPIO.LOW) # Turn Off
    print("message received " ,str(message.payload.decode("utf-8")))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="",password="")
client.connect("167.172.87.186", 1883, 60)
client.loop_forever()

