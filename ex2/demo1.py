import time
import paho.mqtt.client as paho
#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1106
import time
import config
import traceback

from PIL import Image,ImageDraw,ImageFont

broker="10.8.0.1"

try:
    disp = SH1106.SH1106()

    print("\r\1.3inch OLED")
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font = ImageFont.truetype('Font.ttf', 20)
    font10 = ImageFont.truetype('Font.ttf',13)

# Define callback
def on_message(client, userdata, message):
    time.sleep(1)
    try:
    
        disp = SH1106.SH1106()
        
         print("\r\1.3inch OLED")
        # Initialize library.
        disp.Init()
        # Clear display.
        disp.clear()
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")

        draw.text((28,20),str(message.payload.decode("utf-8")), font = font, fill = 0)
    except IOError as e:
        print(e)

client= paho.Client("client-006") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

# Bind function to callback
client.on_message=on_message

# Set username and password
client.username_pw_set(username = "iot_module", password = "parool")

print("connecting to broker ",broker)
client.connect(broker)   # connect
client.loop_start()      # start loop to process received messages
print("subscribing ")
client.subscribe("class/iot06") #subscribe
time.sleep(2)

try:
        while True:
                    time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect() #disconnect
    client.loop_stop() #stop loop

