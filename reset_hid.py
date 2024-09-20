import os
import time
import traceback
import serial

assert os.getuid() == 0, "You must be root to run this script."

SERIAL_DEVICE = "/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0"

RESET_BYTES = [0x57, 0xAB,0x00,0x0F,0x00]
CHECKSUM_BYTE = sum(RESET_BYTES)%256
RESET_BYTES_WITH_CHECKSUM = [*RESET_BYTES, CHECKSUM_BYTE]

RESET_PACKET = bytes(RESET_BYTES_WITH_CHECKSUM)


def reset_once():
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
        data_to_send = RESET_PACKET
        # Send data over the serial port
        ser.write(data_to_send)

        print("Data sent:", data_to_send.hex())
        reply = ser.read(100)
        print("Data read:", reply.hex())

        # Close the serial port
        ser.close()
        print("Serial port is closed.")
    else:
        print("Failed to open serial port.")

def reset_multiple(times=2):
    for index in range(times):
        print(f"[*] Round #{index+1}")
        try:
            reset_once()
        except:
            traceback.print_exc()
            print("[-] Failed to reset")
        finally:
            time.sleep(2)

if __name__ == "__main__":
    reset_multiple()
