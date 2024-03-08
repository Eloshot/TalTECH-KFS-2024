import time
import paho.mqtt.client as paho
import SH1106
from PIL import Image, ImageDraw, ImageFont

broker = "10.8.0.1"
disp = SH1106.SH1106()
disp.Init()
disp.clear()
font = ImageFont.truetype('Font.ttf', 20)
font10 = ImageFont.truetype('Font.ttf', 13)
image = Image.new('1', (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(image)

def on_message(client, userdata, message):
    time.sleep(1)
    msg = str(message.payload.decode("utf-8"))
    draw.text((0, 40), msg, font=font10, fill=0)
    disp.ShowImage(disp.getbuffer(image))

client = paho.Client("client-006")
client.username_pw_set(username="iot_module", password="parool")
client.on_message = on_message
client.connect(broker)
client.subscribe("class/iot06")
client.loop_start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()