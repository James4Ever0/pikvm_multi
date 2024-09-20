lsof -i TCP:8790 | grep -v COMMAND | awk '{print $2}' | xargs -Iabc kill -s KILL abc
rmmod uvcvideo
modprobe uvcvideo nodrop=1 timeout=5000
docker stop kvmd
docker rm -f kvmd
/usr/bin/python3 reset_usb.py
docker compose -f onekvm.yaml -p onekvm up 
