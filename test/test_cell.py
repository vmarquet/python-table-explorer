#!/usr/bin/env python3

import unittest

from bs4 import BeautifulSoup
from table_explorer.table_explorer import TableExplorer
from table_explorer.cell import Cell


class TestCell(unittest.TestCase):
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

        with open('test/test_files/test_html_content.html','r') as f:
            self.table_html_content = BeautifulSoup(f.read(), 'html.parser').find('table')


    def test_html(self):
        table = TableExplorer(self.table_html_content)

        cell = table.at(0,0)
        self.assertEqual(str(cell.html), '<u>0,0</u>')

        cell = table.at(1,0)
        self.assertEqual(str(cell.html), '<i>1,0</i>')

        cell = table.at(0,1)
        self.assertEqual(str(cell.html), '<a href="https://github.com/vmarquet/python-table-explorer">0,1</a>')

        cell = table.at(1,1)
        self.assertEqual(str(cell.html), '1,1')


    def test_text(self):
        table = TableExplorer(self.table_one_cell)
        self.assertEqual(table.at(0,0).text, '0,0')

        table = TableExplorer(self.table_simple)
        for x in range(table.width):
            for y in range(table.height):
                self.assertEqual(table.at(x,y).text, '%s,%s' % (x,y))

        table = TableExplorer(self.table_rowspan_colspan)
        self.assertEqual(table.at(0,0).text, '0,0 1,0  0,1 1,1')
        self.assertEqual(table.at(0,1).text, '0,0 1,0  0,1 1,1')
        self.assertEqual(table.at(1,0).text, '0,0 1,0  0,1 1,1')
        self.assertEqual(table.at(1,1).text, '0,0 1,0  0,1 1,1')
        self.assertEqual(table.at(1,2).text, '1,2')
        self.assertEqual(table.at(0,3).text, '0,3')
        self.assertEqual(table.at(3,4).text, '3,4')
        self.assertEqual(table.at(1,3).text, '1,3 2,3  1,4 2,4')
        self.assertEqual(table.at(2,3).text, '1,3 2,3  1,4 2,4')
        self.assertEqual(table.at(1,4).text, '1,3 2,3  1,4 2,4')
        self.assertEqual(table.at(2,4).text, '1,3 2,3  1,4 2,4')


    def test_colspan_rowspan_width_height(self):
        table = TableExplorer(self.table_rowspan_colspan)

        for index in (0,0), (1,0), (0,1), (1,1), (2,1), (3,1), (2,2), (3,2), (1,3), (2,3), (1,4), (2,4):
            self.assertEqual(table.at(index[0],index[1]).colspan, 2)
            self.assertEqual(table.at(index[0],index[1]).rowspan, 2)
            self.assertEqual(table.at(index[0],index[1]).width, 2)
            self.assertEqual(table.at(index[0],index[1]).height, 2)

        for index in (2,0), (3,0), (0,2), (1,2), (0,3), (0,4), (3,3), (3,4):
            self.assertEqual(table.at(index[0],index[1]).colspan, 1)
            self.assertEqual(table.at(index[0],index[1]).rowspan, 1)
            self.assertEqual(table.at(index[0],index[1]).width, 1)
            self.assertEqual(table.at(index[0],index[1]).height, 1)

