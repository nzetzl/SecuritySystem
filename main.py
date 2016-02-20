from time import sleep

import urllib3

#import RPi.GPIO as GPIO

#import picamera

http = urllib3.PoolManager()
request = http.request('GET', 


camera = picamera.PiCamera();

camera.capture('img01.jpg')
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

