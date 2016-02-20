from time import sleep

import RPi.GPIO as GPIO

import picamera

from twilio.rest import TwilioRestClient

account = "AC54f0af10d5a1f55ca9ce2fce1f8c06f0"
token = "701c8da55ae6f912a5815a76d1fb87f6"
client = TwilioRestClient(account, token)

camera = picamera.PiCamera();

camera.capture('img01.jpg')
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

message = client.messages.create(to="+13176051723", from_="+13178303149" body="Hello!")
