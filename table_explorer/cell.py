#!/usr/bin/env python3


class Cell:
    # we define aliases for attribute names, for convenience purposes
    aliases = {
        'width': 'colspan',
        'height': 'rowspan',
    }

    def __init__(self, ids):
        self.ids = ids

        self.rowspan = None
        self.colspan = None

        self.x_offset = None
        self.y_offset = None

        self.top_cells    = []
        self.right_cells  = []
        self.bottom_cells = []
        self.left_cells   = []

    # we need to override __setattr__() to support aliases
    def __setattr__(self, name, value):
        name = self.aliases.get(name, name)
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        if name == "aliases":
            raise AttributeError  # avoir recursion
        name = self.aliases.get(name, name)
        return object.__getattribute__(self, name)


