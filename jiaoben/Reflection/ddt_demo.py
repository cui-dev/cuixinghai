#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ddt import ddt, data, file_data, unpack
import os
import csv
import unittest

from jiaoben.Reflection.calculator import Calculator as cal


def csv_read(file):
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        reader = csv.reader(f)
        contents = []
        for line in reader:
            elements = []
            for el in line:
                elements.append(cal.aton(el))
            contents.append(elements)
    return contents


@ddt
class CalculatorTest(unittest.TestCase):

    @data([15, 5, 10], [8, 3, 5], [13, 9, 4])
    @unpack
    def test_add(self, expected, num1, num2):
        self.assertEqual(expected, cal.add(num1, num2))

    @data(*csv_read('./data/sub_data.csv'))
    @unpack
    def test_sub(self, expected, num1, num2):
        self.assertEqual(expected, cal.sub(num1, num2))

    @file_data('./data/multi_data.json')
    @unpack
    def test_multi(self, expected, num1, num2):
        self.assertEqual(expected, cal.multi(num1, num2))

    @file_data('./data/div_data.yaml')
    @unpack
    def test_div(self, expected, num1, num2):
        self.assertEqual(expected, cal.div(num1, num2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
