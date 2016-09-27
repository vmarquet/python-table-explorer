#!/usr/bin/env python3


class Cell:
    # we define aliases for attribute names, for convenience purposes
    aliases = {
        'width': 'colspan',
        'height': 'rowspan',
    }


    def __init__(self, ids, html, text, colspan, rowspan, x_offset, y_offset):
        self.ids = ids

        self.html = html  # HTML content of the cell
        self.text = text  # text content of the cell (all tags stripped)

        self.colspan = colspan
        self.rowspan = rowspan

        self.x_offset = x_offset
        self.y_offset = y_offset

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


    def __repr__(self):
        return '<Cell x_offset=%s y_offset=%s colspan=%s rowspan=%s>' \
            % (self.x_offset, self.y_offset, self.colspan, self.rowspan)


    def __lt__(self, other):
        if self.y_offset != other.y_offset:
            return self.y_offset < other.y_offset
        elif self.x_offset != other.x_offset:
            self.x_offset < other.x_offset
        return False

