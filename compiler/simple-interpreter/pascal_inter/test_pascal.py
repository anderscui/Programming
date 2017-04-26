# coding=utf-8
import unittest
from unittest import TestCase

from pascal_inter.pascal import Parser, Lexer, Interpreter, SymbolTableBuilder


class TestPascal(TestCase):

    def get_ast(self, filepath):
        text = open(filepath, 'r').read()
        lexer = Lexer(text)
        parser = Parser(lexer)
        return parser

    def test_interpreter(self):
        parser = self.get_ast('test2.pas')
        tree = parser.parse()
        inter = Interpreter(tree)
        result = inter.interpret()
        print(result)
        print(inter.GLOBAL_SCOPE)

    def test_procedure_decl(self):
        parser = self.get_ast('procedures.pas')
        tree = parser.parse()
        inter = Interpreter(tree)
        result = inter.interpret()
        print(result)
        print(inter.GLOBAL_SCOPE)

    @unittest.skip("skip errors")
    def test_symbol_table_error(self):
        parser = self.get_ast('name_error.pas')
        tree = parser.parse()
        builder = SymbolTableBuilder()
        builder.visit(tree)

    def test_symbol_table(self):
        parser = self.get_ast('test2.pas')
        tree = parser.parse()
        builder = SymbolTableBuilder()
        builder.visit(tree)

        print('')
        print('Symbol Table Contents:')
        print(builder.symtab)

        interpreter = Interpreter(tree)
        result = interpreter.interpret()

        print('')
        print('Runtime GLOBAL_MEMORY contents:')
        for k, v in sorted(interpreter.GLOBAL_SCOPE.items()):
            print('%s = %s' % (k, v))
