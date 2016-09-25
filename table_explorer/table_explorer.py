#!/usr/bin/env python3

import sys
import logging

from .cell import Cell


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)  # uncomment to debug



class TableExplorer:
    def __init__(self, table):
        self.table = table

        self.width = self.__find_table_width()
        self.height = self.__find_table_height()

        logger.debug('width = %s, height = %s' % (self.width, self.height))

        self.cells = {}

        self.__create_cells()
        self.__create_links_between_cells()


    def __create_cells(self):
        for j,row in enumerate(self.table.find_all('tr')):
            cols = row.find_all('td')

            i = 0
            for item in cols:
                if item.has_attr('colspan'):
                    width_ = int(item['colspan'])
                else:
                    width_ = 1

                if item.has_attr('rowspan'):
                    height_ = int(item['rowspan'])
                else:
                    height_ = 1

                logger.debug('found cell, width = %s, height = %s' % (width_, height_))

                i_effective = i
                while True:
                    idx = '%s.%s' % (i_effective,j)
                    # check if space already occupied by a cell with rowspan > 1 or colspan > 1
                    if idx in self.cells:
                        i_effective += 1
                    else:
                        break

                indexes = []
                for k in range(i_effective, i_effective+width_):
                    for l in range(j, j+height_):
                        logger.debug("k = %s, l = %s" % (k, l))
                        indexes.append((k,l))

                cell = Cell(indexes, next(item.children), item.get_text(), width_, height_, i_effective, j)
                logger.debug('adding cell which occupies %s' % str(indexes))

                for index in indexes:
                    index_s = "%s.%s" % index
                    self.cells[index_s] = cell

                logger.debug("%s %s -> %s || " % (i, j, item.get_text().strip()))

                i += width_

            logger.debug("-"*50)

        logger.debug("="*50)


    def __create_links_between_cells(self):
        # we create the links between cells
        for i in range(self.width):
            for j in range(self.height):
                cell = self.cells['%s.%s' % (i,j)]

                # adding link to top cell
                if j is not 0:
                    top_cell = self.cells['%s.%s' % (i,j-1)]
                    if top_cell not in cell.top_cells:
                        cell.top_cells.append(top_cell)

                # adding link to right cell
                if i is not (self.width-1):
                    right_cell = self.cells['%s.%s' % (i+1,j)]
                    if right_cell not in cell.right_cells:
                        cell.right_cells.append(right_cell)

                # adding link to bottom cell
                if j is not (self.height-1):
                    bottom_cell = self.cells['%s.%s' % (i,j+1)]
                    if bottom_cell not in cell.bottom_cells:
                        cell.bottom_cells.append(bottom_cell)

                # adding link to left cell
                if i is not 0:
                    left_cell = self.cells['%s.%s' % (i-1,j)]
                    if left_cell not in cell.left_cells:
                        cell.left_cells.append(left_cell)


    # Compute table width, taking into account the 'colspan' attributes
    def __find_table_width(self):
        width = 0

        row = self.table.find_all('tr')[0]
        for cell in row.find_all('td'):
            if cell.has_attr('colspan'):
                width += int(cell['colspan'])
            else:
                width += 1

        return width


    # Compute table height, taking into account the 'rowspan' attributes
    def __find_table_height(self):
        height = 0

        row_to_ignore = 0
        for row in self.table.find_all('tr'):
            if row_to_ignore > 0:
                row_to_ignore -= 1
                continue

            cell = row.find_all('td')[0]
            if cell.has_attr('rowspan'):
                height += int(cell['rowspan'])
                row_to_ignore = int(cell['rowspan']) - 1
            else:
                height += 1

        return height


    # Get the cell at position (x,y)
    def at(self, x, y):
        if not ((0 <= x < self.width) and (0 <= y < self.height)):
            raise ValueError('Error: position (%s,%s) does not exist.' % (x,y))

        index = '%s.%s' % (x,y)
        return self.cells[index]


    # Return all cells.
    def all(self):
        cells = []

        for j in range(self.height):
            for i in range(self.width):
                cell = self.at(i,j)
                if cell not in cells:
                    cells.append(cell)

        return cells


    # Return all cells in column at index 'x'
    def col(self, x):
        if not (0 <= x < self.width):
            raise ValueError('Column %s not in table (width = %s).' % (x, self.width))

        cells = []
        for y in range(self.height):
            cell = self.at(x,y)
            if cell not in cells:
                cells.append(cell)

        return cells


    # Return all cells in row at index 'y'
    def row(self, y):
        if not (0 <= y < self.height):
            raise ValueError('Row %s not in table (height = %s).' % (y, self.height))

        cells = []
        for x in range(self.width):
            cell = self.at(x,y)
            if cell not in cells:
                cells.append(cell)

        return cells


