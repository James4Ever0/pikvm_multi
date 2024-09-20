import pexpect
import threading
import subprocess
import time
import pexpect
import sys
import os

def execute_command(command:str):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"[*] Command output:\n{stdout.decode()}")
    print(f"[*] Command errors:\n{stderr.decode()}")


class ProcessReader:
    def __init__(self, cmd:str, detected_cmd:str, keyword_list:list[str], loop_interval:int=1, backoff_interval:int=30):
        self.cmd = cmd
        self.detected_cmd = detected_cmd
        self.loop_interval = loop_interval
        self.backoff_interval = backoff_interval
        self.process = pexpect.spawn(cmd, timeout=None)
        self.keyword_detected = False
        self.keyword_list = [it.encode() for it in keyword_list]

    def execute_command_and_reset_detection_flag(self, command:str):
        execute_command(command)
        self.keyword_detected = False

    def on_detected(self):
        print('[*] Executing command on keyword detection:', self.detected_cmd)
        thread = threading.Thread(target=self.execute_command_and_reset_detection_flag, args=(self.detected_cmd,), daemon=True)
        thread.start()

    def check_for_keyword(self, line:bytes):
        for it in self.keyword_list:
            if it in line:
                self.keyword_detected = True
                break

    def read_stdout(self):
        while True:
            line = self.process.readline()  # Read a line from stdout
            if not line:
                print('[*] Empty line from process.')
                print('[-] Exiting reading thread.')
                break
            print("STDOUT: ",end="")
            sys.stdout.buffer.write(line)
            sys.stdout.flush()
            self.check_for_keyword(line)

    def start_reading(self):
        thread_stdout = threading.Thread(target=self.read_stdout, daemon=True)
        thread_stdout.start()

    def main(self):
        self.start_reading()
        while True:
            if self.keyword_detected:
                self.on_detected()
                time.sleep(self.backoff_interval)
            time.sleep(self.loop_interval)

def start_uvicorn_relay_server():
    cmd = "/home/jamesbrown/mambaforge/bin/conda run --no-capture-output -n litellm uvicorn --port 8790 switch_server:app"
    threading.Thread(target=lambda: os.system(cmd), daemon=True).start()

def main():
    start_uvicorn_relay_server()
    cmd = 'bash start_onekvm_service.sh'
    detected_cmd = 'bash reset_devices.sh'
    #detected_cmd = f'{sys.executable} reset_usb.py'
    #keyword_list = ['CAP: Device select() timeout']
    keyword_list = ['CAP: Device select() timeout', '响应时间太短，HID 可能已断开','HID 循环中出现意外错误']
    reader = ProcessReader(cmd, detected_cmd, keyword_list)
    reader.main()


if __name__ == "__main__":
    main()
