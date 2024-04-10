from Module import Loader

modules = Loader()

print(modules.modules['script']().metadata['options'])