import fastapi
import os

app = fastapi.FastAPI()



def toggle():
    toggle_only()
    reset_hid_usb()
    reset_usb()
    reset_hid()

def reset_hid_usb():
    os.system('/usr/bin/python3 reset_hid_usb.py')

def reset_usb():
    os.system('/usr/bin/python3 reset_usb.py')

def reset_hid():
    os.system('/usr/bin/python3 reset_hid.py')

def toggle_only():
    os.system("bash toggle_usbrelay.sh")

app.get("/toggle")(toggle)
app.get("/toggle_only")(toggle_only)
app.get("/reset_hid_usb")(reset_hid_usb)
app.get("/reset_usb")(reset_usb)
app.get("/reset_hid")(reset_hid)

