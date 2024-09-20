import usb.core

from usb.core import find as finddev

devices = [
#        (0x1a86, 0x7523),
        (0x1de1, 0xf105), # video capture card
        ]
for idVendor, idProduct in devices:
    dev = finddev(idVendor=idVendor, idProduct=idProduct)
    dev.reset()
