import os
import importlib.util

class Loader:
    def __init__(self, modules_dir: str = "scripts"):
        self.modules_dir = modules_dir
        self.modules = {}
        self._load_modules()

    def _load_modules(self):
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
