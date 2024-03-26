from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from debug import Debug
from logger import Logger
from handle_attacks import HandleAttacks
from banner import Banner
import subprocess
import platform
import time

styles = {
    '': '#ff0066',
    'name': '#Fffb00',
    'pound': '#2596be', 
    'lbracket': '#2596be',
    'rbracket': '#2596be', 
    'option': '#Ff00fd',
    'method': '#Ff00fd',
}
style = Style.from_dict(styles)

message = [
    ('class:name', 'FireLemon'),
    ('class:pound', '# '),
]

# def now_playing():
    
#     return HTML(f'now playing: <b><style bg=>Toolbar</style></b>!')
def right_prompt(text):
    Logger(__file__)
    return text

def shell(*args, **kwargs):
    Logger(__file__)
    session = PromptSession()

    option = session.prompt(*args, **kwargs, complete_in_thread=True, auto_suggest=AutoSuggestFromHistory())

    return option.strip()

def handle_command():
    Logger(__file__)

    completer = NestedCompleter.from_nested_dict({
        'attack' : None,
        'attacks' : None,
        'options' : None,
        'debug' : None,
        'exit': None,
    })

    while True:

        option = shell(message, style = style, completer=completer)

        # print(f"\'{option}\'")

        if option == "":
            continue

        elif option == "attack":
            # print("hi")
            attack()

        elif option == 'attacks':
            Banner().attacks()

        elif option == 'options':
            Banner().options()

        elif option == 'debug':
            print("not debug")

        elif option == 'exit':
            exit(0)

        else:
            print("unknown option!")
            continue

def option_selection(option):
    Logger(__file__)

    postion = message.index(('class:pound', '# '))
    message.insert(postion, (('class:rbracket', ')')))
    message.insert(postion, (('class:option', option)))
    message.insert(postion, (('class:lbracket', '(')))

def layer_selection(layer):
    Logger(__file__)

    postion = message.index(('class:option', attack.__name__))
    message.insert(postion + 1, (('class:lbracket', '\\')))
    message.insert(postion + 2, (('class:option', layer)))

def method_selection(method, layer):
    Logger(__file__)

    postion = message.index(('class:option', layer))
    message.insert(postion + 1, (('class:lbracket', '\\')))
    message.insert(postion + 2, (('class:method', method)))

def layer(layer):
    Logger(__file__)

    if layer == 'layer3':
        completer = NestedCompleter.from_nested_dict({
            'Lemonsqueezy' : None,
            'ping of death' : None,
        })

        while True:

            option = shell(message, style = style, completer=completer)

            if option == "":

                continue

            else:

                method_selection(option, layer)

    elif layer == 'layer4':
        completer = NestedCompleter.from_nested_dict({
            'syn flood' : None,
            'tcp flood' : None,
            'udp flood' : None,
            'minecraft' : None,
        }) 

        while True:

            option = shell(message, style = style, completer=completer)

            if option == "":

                continue

            else:

                method_selection(option, layer)

    elif layer == 'layer5':
        pass

    elif layer == 'layer7':

        completer = NestedCompleter.from_nested_dict({
            'http flood' : None,
            'memcache' : None,
        })

        while True:

            option = shell(message, style = style, completer=completer)

            if option == "":

                continue

            elif option == 'back':
                break

            else:

                print(f"Type 'options to start the {option} attack. ('back to back!)")

                completer = NestedCompleter.from_nested_dict({
                    'options' : None,
                    'back' : None,
                })

                method_selection(option, layer)
                output = shell(message, style = style, completer=completer)

                if output == 'options' or output == 'options'.upper():
                    HandleAttacks(option)

                if output == 'back':
                    break

def attack():
    Logger(__file__)

    layers = {
        'layer3' : None,
        'layer4' : None,
        'layer5' : None,
        'layer7': None,
    }

    methods = {
        'Lemonsqueezy' : None,
        'ping of death' : None,
        'syn flood' : None,
        'tcp flood' : None,
        'udp flood' : None,
        'minecraft' : None,
        'http flood' : None,
        'memcache' : None,
    }

    options = NestedCompleter.from_nested_dict({**layers, **methods})
            
    option_selection(attack.__name__)

    while True:

        option = shell(message, style = style, completer=options)

        if option == "":

            continue

        elif option == "back":

            break

        else:

            for key, value in methods.items():

                if option in key:

                    HandleAttacks(option)

                    while True:
                        
                        time.sleep(1)

                else:

                    layer_selection(option)
                    layer(option)



if platform.system().lower() == "windows":
   subprocess.call("cls", shell=True)

elif platform.system().lower() == "linux":
    subprocess.call("clear", shell=True)

else:
    subprocess.call("clear", shell=True)
    
Banner().print_banner()
handle_command()
