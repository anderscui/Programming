# coding=utf-8
from unittest import TestCase

from calculator.spi import Parser, Lexer, Interpreter
from calculator.spi import RpnTranslator, LispTranslator


class TestSpi(TestCase):

    def expr_expected(self, text, expected_value):
        lexer = Lexer(text)
        parser = Parser(lexer)
        inter = Interpreter(parser)
        self.assertEqual(inter.interpret(), expected_value)

    def test_interpreter(self):
        self.expr_expected('3', 3)
        self.expr_expected('1 + 1', 2)
        self.expr_expected('2 + 7 * 4', 30)
        self.expr_expected('7 - 6 / 3', 5)
        self.expr_expected('14 + 2 * 3 - 6 / 2', 17)
        self.expr_expected('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)', 10)

        # TODO: add these operators
        # self.test_expr('2 ^ 3', 8)
        # self.test_expr('3 * 2 ^ 3', 24)
        # self.test_expr('3 ^ 2 * 2', 18)
        # self.test_expr('3^2^2+1', 82)

    def test_interpreter_unary_op(self):
        self.expr_expected('+5', 5)
        self.expr_expected('-5', -5)
        self.expr_expected('5---2', 3)
        self.expr_expected('5 - - - + - 3', 8)
        self.expr_expected('5 - - - + - (3 + 4) - +2', 10)

    def rpn_expected(self, text, expected_value):
        lexer = Lexer(text)
        parser = Parser(lexer)
        inter = RpnTranslator(parser)
        self.assertEqual(inter.interpret(), expected_value)

    def test_rpn_interpreter(self):
        self.rpn_expected('1 + 1', '1 1 +')
        self.rpn_expected('2 + 3 * 5', '2 3 5 * +')
        self.rpn_expected('(5 + 3) * 12 / 3', '5 3 + 12 * 3 /')

    def lisp_expected(self, text, expected_value):
        lexer = Lexer(text)
        parser = Parser(lexer)
        inter = LispTranslator(parser)
        self.assertEqual(inter.interpret(), expected_value)

    def test_lisp_interpreter(self):
        self.lisp_expected('1 + 1', '(+ 1 1)')
        self.lisp_expected('2 + 3 * 5', '(+ 2 (* 3 5))')
        self.lisp_expected('(5 + 3) * 12 / 3', '(/ (* (+ 5 3) 12) 3)')
        self.lisp_expected('(2 + 3 * 5)', '(+ 2 (* 3 5))')
        self.lisp_expected('(2 + 3) * 5)', '(* (+ 2 3) 5)')
