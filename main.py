from subprocess import call

from time import sleep

import urllib3

import RPi.GPIO as GPIO

import picamera

http = urllib3.PoolManager()
print str(request)


camera = picamera.PiCamera();

camera.capture('img01.jpg')
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

call(["MP4Box", "-add", "video.h264", "video.mp4"])
request = http.request('POST', 'https://api.mogreet.com/cm/media.upload?client_id=7225&token=2449acf48398a0887e21d96de8369911&url=./video.mp4&type=video&name=securityVideo')
contentID = request.headers.['content_id']
messageString = "https://api.mogreet.com/moms/transaction.send?client_id=7225&token=2449acf48398a0887e21d96de8369911&"+contentID+"&to=+13176051723&campaign_id=123086&message=Intruder%20alert%21"
messageRequest = http.request('GET', messageString)


