class Cacher:
    def __init__(self, fn):
        self.fn = fn
        self.map = {}

    def __call__(self, *args):
        key = hash(args)
        if key not in self.map:
            self.map[key] = self.fn(*args)
        return self.map[key]