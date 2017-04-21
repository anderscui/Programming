# coding=utf-8
from unittest import TestCase

from calculator.spi import Parser, Lexer, Interpreter


class TestSpi(TestCase):

    def test_expr(self, text, expected_value):
        lexer = Lexer(text)
        parser = Parser(lexer)
        inter = Interpreter(parser)
        self.assertEqual(inter.interpret(), expected_value)

    def test_interpreter(self):
        self.test_expr('1 + 1', 2)
        self.test_expr('2 + 7 * 4', 30)
        self.test_expr('7 - 6 / 3', 5)
        self.test_expr('14 + 2 * 3 - 6 / 2', 17)
        self.test_expr('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)', 10)

        # self.test_expr('2 ^ 3', 8)
        # self.test_expr('3 * 2 ^ 3', 24)
        # self.test_expr('3 ^ 2 * 2', 18)
        # self.test_expr('3^2^2+1', 82)
