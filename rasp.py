import time, requests
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw 
ss = Seesaw(busio.I2C(SCL, SDA), addr=0x36)

heroku = "" #Enter your heroku app URL here
twitch = "" #Enter your twitch Key here

os.system("raspivid -n -t 0 -w 1920 -h 1080 -fps 30 -b 3500000 -g 60 -o - 
          | ffmpeg -f lavfi -i anullsrc -c:a aac -r 30 -i - -g 60 -strict 
          experimental -threads 4 -vcodec copy -map 0:a -map 1:v -b:v 3500000
          -preset ultrafast -f flv 'rtmp://live-ams02.twitch.tv/app/" + twitch + "'")
while True:
    requests.post(heroku, json={"temp": ss.get_temp(), "moist": ss.moisture_read()})
    time.sleep(1)
