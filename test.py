import requests
import subprocess

subprocess.call(["MP4Box", "-add", "video.h264", "video.mp4"])

r = requests.post('https://api.mogreet.com/cm/media.upload?client_id=7225&token=2449acf48398a0887e21d96de8369911&url=./video.mp4&type=video&name=securityVideo')

print r.status_code
print r.headers

content = r.text
print content
