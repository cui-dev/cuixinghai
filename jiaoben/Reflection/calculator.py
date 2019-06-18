#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def multi(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def aton(sNum):
        if isinstance(sNum, str):
            try:
                return int(sNum)
            except ValueError:
                return float(sNum)
        return sNum
