from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style
from core.scripts.handle_attacks.http_handle import HttpHandle
from core.scripts.handle_attacks.host_handle import HostHandle
from core.logger import Logger
from core.debug import Debug

styles = {
    '':          '#ff0066',
    'url': '#Fffb00', 
    'threads_num': '#Fffb00',
    'sleep_time': '#Fffb00',
    'pound': '#2596be',
    'rprompt': 'bg:#Ff00fd #ffffff',
}

style = Style.from_dict(styles)

class HandleAttacks:

    def __init__(self, method):
        Logger(__file__)

        url = None
        sleep_time = None

        #################

        if method in {
            "http flood",
        }:

            HttpHandle(method)

        elif method in {
            'Lemonsqueezy',
            'ping of death',
            'syn flood',
            'tcp flood',
            'udp flood',
            'minecraft',
            'memcache',
        }:
            
            HostHandle(method)
        