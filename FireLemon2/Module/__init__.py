import os
import importlib.util
from colorama import Fore

class Loader:
    def __init__(self, modules_dir: str = "scripts"):
        self.modules_dir = modules_dir
        self.modules = {}
        self._load_modules()

    def _load_modules(self):
        for root, dirs, files in os.walk(self.modules_dir):
            for dir in dirs:
                for filename in os.listdir(os.path.join(self.modules_dir, dir)):
                    if filename.startswith("__") or not filename.endswith(".py"):
                        continue

                    module_name = filename.rstrip(".py")
                    module_path = os.path.join(os.path.join(self.modules_dir, dir), filename)
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    module_class = getattr(module, "Main")
                    self.modules[module_name] = module_class

        for filename in os.listdir(self.modules_dir):
            if filename.startswith("__") or not filename.endswith(".py"):
                continue

            module_name = filename.rstrip(".py")
            module_path = os.path.join(self.modules_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module_class = getattr(module, "Main")
            self.modules[module_name] = module_class

    def run_module(self, module_name: str) -> object:
        module = self.modules.get(module_name)
        if module is None:
            raise Exception("Module does not exist.")
        
        module_obj = module()
        module_obj.run()

    def print_tree(self):
        startpath = self.modules_dir
        count = 0
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            basename = os.path.basename(root)
            if basename.startswith("__"):
                continue

            if basename == startpath:
                print('{}/'.format(basename))

            else:
                print('{}└─{}{}{}'.format(indent, Fore.RED, basename, Fore.WHITE))

            subindent = ' ' * 4 * (level + 1)

            for f in files:
                if f.startswith("__"):
                    continue

                print('{}├─{}'.format(subindent, f))
                count += 1

        print(count, Fore.RED + "Modules")
