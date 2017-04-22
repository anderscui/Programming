# coding=utf-8
from unittest import TestCase

from pascal_inter.pascal import Parser, Lexer, Interpreter


class TestPascal(TestCase):

    def test_interpreter(self):
        filepath = 'test.pas'
        text = open(filepath, 'r').read()
        lexer = Lexer(text)
        parser = Parser(lexer)
        inter = Interpreter(parser)
        result = inter.interpret()
        print(result)
        print(inter.GLOBAL_SCOPE)
