import threading 
from core.logger import Logger, ThreadLogger, ThreadFailure

class Thread:
    def __init__(self):

        self.threads_num : int = None
        self.threads = []

    def run_in_thread(self, func):
        Logger(__file__)

        def threads(*args, **kwargs):
            Logger(__file__)


            for i in range(0, self.threads_num):

                try:

                    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
                    # self.threads.append(thread)
                    thread.deamon = True
                    thread.start()
                    ThreadLogger(i)

                except Exception as error:

                    ThreadFailure(error)
                    continue
        
        return threads
    