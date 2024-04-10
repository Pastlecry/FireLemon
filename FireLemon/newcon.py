from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from banner import Banner
from Module import Loader
import os
import sys
import json

with open('FireLemon/commands.json', 'r') as commands_config:
    commands = json.load(commands_config)

modules = Loader().modules

styles = {
    '': '#ffffff',
    'name': '#Fffb00',
    'pound': '#2596be', 
    'lbracket': '#2596be',
    'rbracket': '#2596be',
    'option': '#Ff00fd',
    'method': '#Ff00fd',
}

style = Style.from_dict(styles)

def shell(*args, **kwargs):

    session = PromptSession()

    option =  session.prompt(*args, **kwargs, style=style, complete_in_thread=True, auto_suggest=AutoSuggestFromHistory())

    return option.strip().split()

def use(module_path):

    if os.path.isfile(f"./{module_path}.py"):
        write_config({'module': f'./{module_path}'}, "w")

        module = modules[module_path.split("/")[1]]()

        return module, module_path
    
    else:
        return False
    
def options(module : object):
    return module.metadata['options']

def set(module : object):
    pass

def run(module : object):
    pass

def write_config(config : dict, w_method : str):
    config = json.dumps(config, indent=4)

    with open("FireLemon/config.json", w_method) as outfile:
        outfile.write(config)

def read_config():
    with open('FireLemon/config.json', 'r') as config_file:
        config = json.load(config_file)

    return config

def reset():
    write_config({'module': ''}, "w")

def console():
    cmd = ""
    args = []
    message = None
    config = read_config()
    module : object = None

    if message is None:
        message = [
            ('class:name', 'FireLemon'),
            ('class:pound', '# '),
        ]
    
    while True:

        # completer = NestedCompleter.from_nested_dict(complete_words)

        try:

            output = shell(message)#, completer=completer)

            if output and output[0] != "":
                cmd = output[0]
                if len(output) >= 2:
                    args = output[1:]

        except KeyboardInterrupt:
            print("exiting...")
            reset()
            sys.exit(0)

        if cmd == "":
            continue

        elif cmd != "":

            if cmd == 'exit' or cmd == 'quit':
                print("exiting..")
                sys.exit(0)

            elif cmd in commands:

                if cmd == "use":
                    if len(args) == 1:
                        # write_config({'command' : cmd}, "w")
                        module, module_path = use(args[0])
                        if module_path is not False:
                            message = [
                                ('class:name', 'FireLemon'),
                                ('class:lbracket', '('),
                                ('class:option', module_path),
                                ('class:rbracket', ')'),
                                ('class:pound', '# '), 
                            ]

                        else:
                            print(f"module '{args[0]}' doesn't exists.")

                    elif len(args) < 1:

                        print("please select a module to 'use'")

                elif cmd == "options":
                    if module:
                        print(options(module))

                    else:
                        print("no module specified to initialize")
                        continue


                elif cmd == "run":
                    if config['module'] != "":
                        pass

                    else:
                        print("no module specified to run")
                        continue

                elif cmd == "set":
                    if config['module'] != "":
                        if len(args) == 2:
                            if args[0] in options():
                                pass

                    else:
                        print("no module specified to run")
                        continue 

                elif cmd == "help":
                    Banner().options()
        
            else:
                print("command not valid")

            # print("command:", cmd, "args:", args)
            
Banner().print_banner()

console()
