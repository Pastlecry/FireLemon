import json
import requests
from socket import *
from core.logger import Logger
from core.thread import Thread

class PortScanner:

    def __init__(self, url):

        self.url = url

    def port_scanner(self):
        Logger(__file__)

        url = f"https://internetdb.shodan.io/{self.get_ip()}"

        try:

            result = requests.get(url).content
            list = json.loads(result.decode('utf-8'))["ports"]

            return list

        except requests.exceptions.ConnectionError:

            print("can't reach the host on your pc!\ncheck your connection or use a vpn or proxy.") 
            exit(0)
    
    def get_ip(self):
        Logger(__file__)

        return gethostbyname(self.url)