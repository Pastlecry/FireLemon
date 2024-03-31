from core.debug import Debug
from core.port_scanner1 import PortScanner
from core.logger import Logger
import requests

NOTE = Debug.NOTE()
WARN = Debug.WARN()
ERROR = Debug.ERROR()

class UrlHandler(PortScanner):
    def __init__(self, url):
        Logger(__file__)

        self.banned_domains = [".gov", ".gob", ".edu"]
        self.url = url

    def url_handler(self):
        Logger(__file__)
         
        PortScanner(self.url)

        if self.url.startswith("http://") or self.url.startswith("https://"):

            is_up = self.is_up()

            if is_up == True:

                print("server is up!")

                return self.url
            
            else:
                print("can't reach the host on your pc!\ncheck your connection or use a vpn or proxy.") 
                exit(0)

            # return self.url
        
        else:
            success = False
            print("trying to resolce correct url!")
            while success == False: 
                print("first try")   
                try:
                    open_ports = self.port_scanner()

                    print("scanned ports!")

                    if 443 in open_ports:
                        self.url = f"https://{self.url}"
                        print(self.url)
                        success = True
                    
                    else:
                        self.url = f"http://{self.url}"
                        print(self.url)
                        success = True

                except:
                    print("scanning ports faild!")
                    success = False
                    continue

            is_up = self.is_up()

            if is_up == True:

                print("server is up!")

                return self.url
            
            else:
                print("can't reach the host on your pc!\ncheck your connection or use a vpn or proxy.") 
                exit(0)

            # return self.url

        # is_up = self.is_up(self.url)

        # if is_up == True:

        #     print("server is up!")

        #     return self.url
        
        # else:
        #     print("can't reach the host on your pc!\ncheck your connection or use a vpn or proxy.") 
        #     exit(0)
        
    def url_validater(self):
        Logger(__file__)
        if ".gov" in self.url or ".edu" in self.url or ".gob" in self.url:#(domain in self.url for domain in self.banned_domains):
            print(False)
            return False
        
        else:
            print(True)
            return True

    def is_up(self):
        print("checking url is up?")
        try:
            requests.get(self.url)
            return True
        except requests.exceptions.ConnectionError:
            return False