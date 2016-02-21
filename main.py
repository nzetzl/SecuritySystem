from time import sleep

import urllib3

import RPi.GPIO as GPIO

import picamera

try:
	GPIO.setmode(GPIO.BOARD)
	#Pin 11: Green LED
	#Pin 13: Red LED
	#Pin 15: Blue LED
	#Pin 31: Motion Sensor
	#Pin 33: Speaker
	GPIO.setup(11, GPIO.OUT)	
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(31, GPIO.IN)
	GPIO.setup(33, GPIO.OUT)

	speakerPin = GPIO.PWM(33, 335)

#http = urllib3.PoolManager()


	camera = picamera.PiCamera()

	while True:
		#Pin 11: Green LED
		#Pin 13: Red LED
		#Pin 15: Blue LED
		if GPIO.input(31) == False:
			GPIO.output(11, True)
			GPIO.output(13, False)
			GPIO.output(15, True)

		elif GPIO.input(31) == True:
			GPIO.output(11, True)
			GPIO.output(13, True)
			GPIO.output(15, False)
			speakerPin.start(50.0)
			camera.capture('img01.jpg')
			camera.start_recording('video.h264')
			sleep(5)
			camera.stop_recording()

		speakerPin.stop()
#call(["MP4Box", "-add", "video.h264", "video.mp4"])
#request = http.request('POST', 'https://api.mogreet.com/cm/media.upload?client_id=7225&token=2449acf48398a0887e21d96de8369911&url=./video.mp4&type=video&name=securityVideo')
#contentID = request.headers.['content_id']
#messageString = "https://api.mogreet.com/moms/transaction.send?client_id=7225&token=2449acf48398a0887e21d96de8369911&"+contentID+"&to=+13176051723&campaign_id=123086&message=Intruder%20alert%21"
#messageRequest = http.request('GET', messageString)
except KeyboardInterrupt:
	print "User ended program"
finally:
	GPIO.cleanup()
