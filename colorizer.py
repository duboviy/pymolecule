from random import random


class Colorizer(object):
    _PREDEFINED_COLORS = {
        'O3': (1.0, 0.0, 0.0),
        'HO': (1.0, 0.5, 0.5),
        'Car': (0.1, 0.1, 0.1),
        'C3': (0.1, 0.1, 0.1),
        'H': (0.0, 0.5, 0.5),
    }

    @classmethod
    def get_color(self, name):
        if name not in self._PREDEFINED_COLORS:
            self._PREDEFINED_COLORS[name] = (random(), random(), random())
        return self._PREDEFINED_COLORS[name]
