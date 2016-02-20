from time import sleep

import RPi.GPIO as GPIO

import picamera

camera = picamera.PiCamera();

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
