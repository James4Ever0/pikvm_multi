import os

assert os.getuid() == 0, "You must be root to run this script."

SERIAL_DEVICE = "/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0"

RESET_BYTES = [0x57, 0xAB,0x00,0x0F,0x00]
CHECKSUM_BYTE = sum(RESET_BYTES)%256
RESET_BYTES_WITH_CHECKSUM = [*RESET_BYTES, CHECKSUM_BYTE]

RESET_PACKET = bytes(RESET_BYTES_WITH_CHECKSUM)

import serial

# Define the serial port and baud rate
ser = serial.Serial(SERIAL_DEVICE, baudrate=9600, timeout=1)

#ser.close()
# Open the serial port
#ser.open()
# port is already open.

# Check if the port is open
if ser.is_open:
    print("Serial port is open.")

    # Data to be sent over the serial port
    hex_string = "57 AB 00 02 08 02 00 04 00 00 00 00 00 12"
    data_to_send = bytes.fromhex(hex_string.replace(' ', ''))
    # Send data over the serial port
    ser.write(data_to_send)

    print("Data sent:", data_to_send.hex())
    reply = ser.read()
    print("Data read:", reply.hex())

    # Close the serial port
    ser.close()
    print("Serial port is closed.")
else:
    print("Failed to open serial port.")

