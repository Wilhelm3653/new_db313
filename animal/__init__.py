import importlib

class _LazyModule:
    def __init__(self, module_name: str):
        self._module_name = module_name
        self._module = None

    def _load(self):
        if self._module is None:
            self._module = importlib.import_module(self._module_name)
            print(type(self._module))
        return self._module

    def __getattr__(self, name):
        print("__getattr__",name)
        module = self._load()
        return getattr(module, name)
    

dog = _LazyModule("animal.dog")
cat = _LazyModule("animal.cat")
print(type(dog),dog.__dict__)