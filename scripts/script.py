# from FireLemon.module import Module
# import FireLemon

class Main:

    def __init__(self):
        self.metadata = {
            'name': 'script',
            'date': '2015-10-10',
            'options': {
                'HOST': "",
                'PORT': "",
            }
        }

    def run(self):
        print(self.metadata['options'])


# FireLemon(script.metadata, script.run)