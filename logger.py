import time
import logging
import datetime
import inspect

class Logger:

    def __init__(self, file_name):

        current = datetime.datetime.now()

        with open("logs.txt", "a") as log_file:

            stack = inspect.stack()
            try:

                class_name = stack[1][0].f_locals["self"].__class__.__name__
                method_name = stack[1][0].f_code.co_name
                log_file.write(f"[{current}] FILE:'{file_name}' FUNC:{class_name}.{method_name}\n")#, ARGS:{args}, KWARGS:{kwargs}\n")

            except:

                method_name = stack[1][0].f_code.co_name

                log_file.write(f"[{current}] FILE:'{file_name}' FUNC:UNKNOWN.{method_name}\n")#, ARGS:{args}, KWARGS:{kwargs}\n")

        # return self.func(self, *args, **kwargs)

class ThreadLogger:
    def __init__(self, id):
        # print("INIT called")

        current = datetime.datetime.now()

        with open("logs.txt", "a") as log_file:

            log_file.write(f"[{current}] NEW Thread:{{id:{id}}}\n")

class ThreadFailure:
    def __init__(self, error):
        current = datetime.datetime.now()

        with open("logs.txt", "a") as log_file:

            log_file.write(f"[{current}] Threading ERROR:{error}\n")

            time.sleep(1)

class requestLogger:
    def __init__(self, contentLen):
        current = datetime.datetime.now()

        with open("logs.txt", "a") as log_file:

            log_file.write(f"[{current}] Request! READ:{contentLen}\n")

            time.sleep(1)

class requestFailure:
    def __init__(self, error):
        current = datetime.datetime.now()

        with open("logs.txt", "a") as log_file:

            log_file.write(f"[{current}] REQUEST ERROR:{error}\n")

            time.sleep(1)