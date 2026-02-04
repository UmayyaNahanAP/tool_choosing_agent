import importlib

class Executor:
    def execute(self, tool, data):
        module = importlib.import_module(tool["module"])
        return module.run(data)
