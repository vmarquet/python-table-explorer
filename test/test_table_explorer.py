#!/usr/bin/env python3

import unittest

from bs4 import BeautifulSoup
from table_explorer.table_explorer import TableExplorer
from table_explorer.cell import Cell


class TestTableExplorer(unittest.TestCase):
    def setUp(self):
        with open('test/test_files/test_one_cell.html','r') as f:
            self.table_one_cell = BeautifulSoup(f.read(), 'html.parser').find('table')

        with open('test/test_files/test_simple.html','r') as f:
            self.table_simple = BeautifulSoup(f.read(), 'html.parser').find('table')

        with open('test/test_files/test_rowspan_colspan.html','r') as f:
            self.table_rowspan_colspan = BeautifulSoup(f.read(), 'html.parser').find('table')

        with open('test/test_files/test_one_cell_rowspan_colspan.html','r') as f:
            self.table_one_cell_rowspan_colspan = BeautifulSoup(f.read(), 'html.parser').find('table')

        with open('test/test_files/test_one_column.html','r') as f:
            self.table_one_column = BeautifulSoup(f.read(), 'html.parser').find('table')

        with open('test/test_files/test_one_row.html','r') as f:
            self.table_one_row = BeautifulSoup(f.read(), 'html.parser').find('table')


    def test_width(self):
        table = TableExplorer(self.table_one_cell)
        self.assertEqual(table.width, 1)

        table = TableExplorer(self.table_simple)
        self.assertEqual(table.width, 3)

        table = TableExplorer(self.table_rowspan_colspan)
        self.assertEqual(table.width, 4)

        table = TableExplorer(self.table_one_cell_rowspan_colspan)
        self.assertEqual(table.width, 2)

        table = TableExplorer(self.table_one_column)
        self.assertEqual(table.width, 1)

        table = TableExplorer(self.table_one_row)
        self.assertEqual(table.width, 4)


    def test_height(self):
        table = TableExplorer(self.table_one_cell)
        self.assertEqual(table.height, 1)

        table = TableExplorer(self.table_simple)
        self.assertEqual(table.height, 3)

        table = TableExplorer(self.table_rowspan_colspan)
        self.assertEqual(table.height, 5)

        table = TableExplorer(self.table_one_cell_rowspan_colspan)
        self.assertEqual(table.height, 2)

        table = TableExplorer(self.table_one_column)
        self.assertEqual(table.height, 4)

        table = TableExplorer(self.table_one_row)
        self.assertEqual(table.height, 1)



    def test_number_of_cells(self):
        table = TableExplorer(self.table_one_cell)
        self.assertEqual(len(table.all()), 1)

        table = TableExplorer(self.table_simple)
        self.assertEqual(len(table.all()), 9)

        table = TableExplorer(self.table_rowspan_colspan)
        self.assertEqual(len(table.all()), 11)

        table = TableExplorer(self.table_one_cell_rowspan_colspan)
        self.assertEqual(len(table.all()), 1)

        table = TableExplorer(self.table_one_column)
        self.assertEqual(len(table.all()), 4)

        table = TableExplorer(self.table_one_row)
        self.assertEqual(len(table.all()), 4)

