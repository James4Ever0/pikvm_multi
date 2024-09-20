rm test.jpeg
fswebcam --no-banner -d /dev/video0 -r 1920x1080 -F 1 test.jpeg
md5sum test.jpeg
