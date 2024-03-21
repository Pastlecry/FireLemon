import json
import requests
from socket import *
from logger import Logger

class PortScanner:

    def __init__(self, url):

        self.url = url

    def port_scanner(self):
        Logger()

        url = f"https://internetdb.shodan.io/{self.get_ip()}"

        result = requests.get(url).content
        list = json.loads(result.decode('utf-8'))["ports"]

        return list
    
    def get_ip(self):
        Logger()

        return gethostbyname(self.url)