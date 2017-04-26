# coding=utf-8
from unittest import TestCase

from calculator.calc import Lexer, Interpreter


class TestCalc(TestCase):

    def test_expr(self, text, expected_value):
        lexer = Lexer(text)
        inter = Interpreter(lexer)
        self.assertEqual(inter.expr(), expected_value)

    def test_interpreter(self):
        self.test_expr('1 + 1', 3)
        self.test_expr('2 + 7 * 4', 30)
        self.test_expr('7 - 6 / 3', 5)
        self.test_expr('14 + 2 * 3 - 6 / 2', 17)
        self.test_expr('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)', 10)

        self.test_expr('2 ^ 3', 8)
        self.test_expr('3 * 2 ^ 3', 24)
        self.test_expr('3 ^ 2 * 2', 18)
        self.test_expr('3^2^2+1', 82)
