import os
import random
from __init__ import FireLemon
from rgbprint import gradient_print, Color, gradient_scroll, gradient_change

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
    4. Smurf(Unavailable)      :: sending ARP packets                           
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

header_1 ="""
˚   ⋆⁺₊✦⁺₊     ˚  .˚  .   ☁.  .    ˚   ⁺⋆₊   .˚  .   . ✦⋆⁺₊      ˚   . ☁ ˚   .˚     ✩₊˚.   ☾      ⋆      ⁺₊✧         ˚   ⁺₊ .     ˚   .      ⁺₊✦₊       ☁  
   ⁺₊✧ .      ˚  ⁺₊ .     ˚  . ☾        ✦₊    ☁      ˚   ⁺⋆₊   .˚  .   . ✦⋆⁺           ˚   . ☁ ˚   .˚     ✩₊˚.   ☾      ⋆  ☁   .    ˚  ⁺⋆₊  
                     .    ˚  ⁺⋆₊   .˚  .  . ✦⋆⁺₊     ˚   . ☁ ˚   .˚     ˚   .˚     ✩₊˚.       ⁺₊✧        ˚  ⁺₊ .      ˚   .      ⁺₊✦⁺₊  ⁺₊✦₊
         ˚   ˚  .˚  .  ☁.  .            .˚  .  . ✦⋆.   ☾        ˚   ⁺₊ .     ˚   .      ⁺₊✦₊       ☁ .     ˚   .      ⁺₊✦     ˚   .       ☁        ☁
  ˚ ˚  .˚  .   ☁.  .   ☾       .  . ✦⋆⁺₊     ˚   . ☁ ˚   .˚     ✩₊˚.   ☾      ⋆      ⁺₊✧         ˚   ⁺₊ .     ˚   .      ⁺₊✦₊       ☁
       .˚  .   ☁.   .   ˚           .˚  .  . ☁ ☁    ⁺₊✧       ˚   ⁺₊   ☾     ⋆   ⁺₊✧      ˚   ⁺₊ .     ˚   .      ⁺₊✦₊       ☁ ☁ ˚   .˚     ✩₊˚.   ☾      ⋆ 
           .  . ✦⋆.   ☾        ˚   ⁺₊ .     ˚   .         ₊     ˚   . ☁ ˚   .˚     ✩₊˚.    ˚   ⁺₊ .     ˚ .˚         ⋆      ⁺₊✧       ✩₊˚.   ☾    
 ☁.  .   ☾       .  . ✦⋆⁺₊     ˚   . ☁ ˚    .  . ✦⋆.   ☾        ˚   ⁺₊ .     ˚   .        ✩₊˚.   . ✦⋆⁺₊      ˚ ☁        ☁⁺₊ .     ˚   .         ˚  ⁺₊
"""
def Gra_print(text):
    # Logger(__file__)
    gradient_print(
        text, 
        start_color=Color.yellow,    
        end_color=Color.orange, 
    )

def center(text):
    # Logger(__file__)
    Terminal_size = os.get_terminal_size()
    lines = text.split("\n")
    f_text = """"""
    for line in lines:
        l = f"{line.center(Terminal_size.columns)}"
        f_text += l
        f_text += "\n"
    return f_text

class Banner:

    def print_banner(self):
        # Logger(__file__)
        if random.randint(0,1):
            Gra_print(center(header_1))   
        Gra_print(center(banner))
        Gra_print(center(Title))

    def options(self):
        # Logger(__file__)
        Gra_print(center(options))

    def attacks(self):
        # Logger(__file__)
        Gra_print(center(attacks))
