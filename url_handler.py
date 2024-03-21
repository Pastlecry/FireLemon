from debug import Debug
from port_scanner1 import PortScanner
from logger import Logger

NOTE = Debug.NOTE()
WARN = Debug.WARN()
ERROR = Debug.ERROR()

class UrlHandler(PortScanner):
    def __init__(self, url):

        self.banned_domains = [".gov", ".gob", ".edu"]
        self.url = url
        PortScanner(url)

    def url_handler(self):
        Logger()

        if ".gov" in self.url or ".edu" in self.url or ".gob" in self.url:#(domain in self.url for domain in self.banned_domains):
            print(ERROR)
            print("cannot use .gov or .gob or .edu in the URL!")
            exit()

        else:

            if self.url.startswith("http://") or self.url.startswith("https://"):
                return self.url
            
            else:        
                open_ports = self.port_scanner()

                if 443 in open_ports:
                    self.url = "https://" + self.url
                
                else:
                    self.url = "http://" + self.url

            return self.url