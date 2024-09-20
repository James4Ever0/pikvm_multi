sudo docker run --rm -it \
    --device /dev/v4l/by-id/usb-Actions_Micro_Display_capture-UVC05_-1877650130-video-index0:/dev/kvmd-video \
    --device /dev/ttyCH341USB0:/dev/kvmd-hid \
    -p 8080:8080 -p 4430:4430 -p 5900:5900 -p 623:623 \
    registry.cn-hangzhou.aliyuncs.com/silentwind/kvmd:dev  ustreamer --device=/dev/kvmd-video --host=0.0.0.0 --port=8081 --resolution 1920x1080 --desired-fps=30 --format=MJPEG --drop-same-frames=30 --debug
