from colorama import *

class Debug:

    def NOTE():
        return Fore.BLUE + "[NOTE] " + Fore.WHITE

    def WARN():
        return Fore.YELLOW + "[WARN] " + Fore.WHITE

    def ERROR():
        return Fore.RED + "[error] " + Fore.WHITE