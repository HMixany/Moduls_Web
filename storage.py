import json
import jaml


class Storage:                        # Інтерфейс, Абстракція
    def get_value(self, key):
        raise NotImplementedError


class JsonStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fh:
            data = json.load(fh)
            return data.get(key, None)


class JamlStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fh:
            data = jaml.load(fh, Loader=jaml.Fullloader)
