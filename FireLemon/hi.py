import sys

def importing(name):
    global module

    sys.path.insert(0, "scripts")
    module = __import__(f"{name}", fromlist=['Main'])

def hi():
    print(module.Main())

def run():
    while True:
        name_script = input("s name:")
        importing(name_script)
        hi()

run()