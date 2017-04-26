# coding=utf-8
"""SPI - Simple Pascal Interpreter"""
from collections import OrderedDict
from operator import add, sub, mul, floordiv, truediv, pow
from operator import pos, neg

# structures
PROGRAM, VAR, PROCEDURE, BEGIN, END = 'PROGRAM', 'VAR', 'PROCEDURE', 'BEGIN', 'END'
# types
INTEGER, REAL = 'INTEGER', 'REAL'
# literals
INTEGER_CONST, REAL_CONST = 'INTEGER_CONST', 'REAL_CONST'
# operators
PLUS, MINUS, MUL, INTEGER_DIV, FLOAT_DIV, POW = 'PLUS', 'MINUS', 'MULTI', \
                                      'INTEGER_DIV', 'FLOAT_DIV', 'POW'
# delimiters
DOT, ASSIGN, SEMI, COLON, COMMA = '.', ':=', ';', ':', ','
LPAREN, RPAREN = '(', ')'

ID = 'ID'
EOF = 'EOF'

CHAR_OPS = {'+': PLUS, '-': MINUS, '*': MUL, '/': FLOAT_DIV,
            'DIV': INTEGER_DIV, '^': POW}
BOP_FUNCS = {PLUS: add, MINUS: sub, MUL: mul, INTEGER_DIV: floordiv,
             FLOAT_DIV: truediv, POW: pow}
UOP_FUNCS = {PLUS: pos, MINUS: neg}
OP_CHARS = {v: k for k, v in CHAR_OPS.items()}

# TODO: support chinese identifier.
# TODO: split to multiple modules: lexer, parser, interpreter?
# TODO: use regex for lexer
# TODO: support floats

# LEXER #


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of a token instance.

        Examples:
            Token(INTEGER, 1)
            Token(PLUS, '+')
            Token(BEGIN, 'BEGIN')
        :return: str repr of a token.
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


RESERVED_KEYWORDS = {
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR'),
    'PROCEDURE': Token('PROCEDURE', 'PROCEDURE'),
    'DIV': Token(INTEGER_DIV, 'DIV'),
    'INTEGER': Token('INTEGER', 'INTEGER'),
    'REAL': Token('REAL', 'REAL'),
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END')
}


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self, msg='Invalid character'):
        raise ValueError(msg)

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # indicates the EOF
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        """Peek into the input buffer without consuming the next char."""
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comments(self):
        while self.current_char != '}':
            self.advance()
        self.advance()  # the closing curly brace

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            token = Token(REAL_CONST, float(result))
        else:
            token = Token(INTEGER_CONST, int(result))

        return token

    def _id(self):
        """Handle identifiers and reserved keywords."""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '{':
                self.advance()
                self.skip_comments()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char.isdigit():
                return self.number()

            # ASSIGN should be scanned before COLON.
            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char in CHAR_OPS:
                token = Token(CHAR_OPS[self.current_char], self.current_char)
                self.advance()
                return token

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            self.error()

        return Token(EOF, None)


# SYMBOLS #


class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type


class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super(BuiltinTypeSymbol, self).__init__(name)

    def __str__(self):
        return self.name

    __repr__ = __str__


class VarSymbol(Symbol):
    def __init__(self, name, type):
        super(VarSymbol, self).__init__(name, type)

    def __str__(self):
        return '<{name}:{type}>'.format(name=self.name, type=self.type)

    __repr__ = __str__


class SymbolTable(object):
    def __init__(self):
        self._symbols = OrderedDict()
        self._init_builtins()

    def __str__(self):
        return 'Symbols: {symbols}'.format(symbols=[val for val in
                                                    self._symbols.values()])

    __repr__ = __str__

    def _init_builtins(self):
        self.define(BuiltinTypeSymbol(INTEGER))
        self.define(BuiltinTypeSymbol(REAL))

    def define(self, symbol):
        print('Define: %s' % symbol)
        self._symbols[symbol.name] = symbol

    def lookup(self, name):
        print('Lookup: %s' % name)
        return self._symbols.get(name)

# PARSER #


class AST(object):
    pass


class Program(AST):
    def __init__(self, name, block):
        self.name = name
        self.block = block


class ProcedureDecl(AST):
    def __init__(self, proc_name, block_node):
        self.proc_name = proc_name
        self.block_node = block_node


class Block(AST):
    def __init__(self, declarations, comp_stats):
        self.declarations = declarations
        self.compound_statements = comp_stats


class VarDecl(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Compound(AST):
    """ 'BEGIN ... END' block """
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    """A variable, constructed out of an ID token"""
    def __init__(self, token):
        self.token = token
        self.value = token.value


class NoOp(AST):
    """An empty statement"""
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ValueError('Invalid syntax')

    def eat(self, token_type):
        """consume the current token of the specific type, and move
        forward to the next token, this method is also used to make sure that
        the current token is of the specific type.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : (PLUS | MINUS) factor | INTEGER_CONST
                    | FLOAT_CONST | LPAREN expr RPAREN
                    | variable"""
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())
        elif token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())
        elif token.type in (INTEGER_CONST, REAL_CONST):
            self.eat(token.type)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def term(self):
        """term : factor ((MUL | INTEGER_DIV | FLOAT_DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (MUL, INTEGER_DIV, FLOAT_DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == INTEGER_DIV:
                self.eat(INTEGER_DIV)
            elif token.type == FLOAT_DIV:
                self.eat(FLOAT_DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def empty(self):
        return NoOp()

    def variable(self):
        """variable: ID"""
        node = Var(self.current_token)
        self.eat(ID)
        return node

    def assign_stat(self):
        """
        assign_stat: variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        return Assign(left, token, right)

    def statement(self):
        """
        statement : compound_statement
                  | assignment_statement
                  | empty
        """
        if self.current_token.type == BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == ID:
            node = self.assign_stat()
        else:
            node = self.empty()
        return node

    def statement_list(self):
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        stat = self.statement()
        results = [stat]
        while self.current_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())
        if self.current_token.type == ID:
            self.error()

        return results

    def compound_statement(self):
        """compound_statement: BEGIN statement_list END"""
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        root = Compound()
        root.children = list(nodes)
        return root

    def type_spec(self):
        """type_spec: INTEGER | REAL"""
        token = self.current_token
        if self.current_token.type == INTEGER:
            self.eat(INTEGER)
        else:
            self.eat(REAL)
        return Type(token)

    def variable_declaration(self):
        var_nodes = [Var(self.current_token)]
        self.eat(ID)

        while self.current_token.type == COMMA:
            self.eat(COMMA)
            var_nodes.append(Var(self.current_token))
            self.eat(ID)
        self.eat(COLON)

        type_node = self.type_spec()
        return [VarDecl(var_node, type_node) for var_node in var_nodes]

    def declarations(self):
        result = []
        if self.current_token.type == VAR:
            self.eat(VAR)
            while self.current_token.type == ID:
                var_decl = self.variable_declaration()
                result.extend(var_decl)
                self.eat(SEMI)

        while self.current_token.type == PROCEDURE:
            self.eat(PROCEDURE)
            proc_name = self.current_token.value
            self.eat(ID)
            self.eat(SEMI)
            block_node = self.block()
            proc_decl = ProcedureDecl(proc_name, block_node)
            result.append(proc_decl)
            self.eat(SEMI)

        return result

    def block(self):
        decl_nodes = self.declarations()
        comp_stat_node = self.compound_statement()
        return Block(decl_nodes, comp_stat_node)

    def program(self):
        """program : PROGRAM variable SEMI block DOT"""
        self.eat(PROGRAM)
        var_node = self.variable()
        prog_name = var_node.value
        self.eat(SEMI)
        block_node = self.block()
        prog_node = Program(prog_name, block_node)
        self.eat(DOT)
        return prog_node

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error()
        return node


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method found'.format(type(node).__name__))


class SymbolTableBuilder(NodeVisitor):
    def __init__(self):
        self.symtab = SymbolTable()

    def visit_Program(self, node):
        self.visit(node.block)

    def visit_ProcedureDecl(self, node):
        pass

    def visit_Block(self, node):
        for decl in node.declarations:
            self.visit(decl)
        self.visit(node.compound_statements)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        self.visit(node.expr)

    def visit_Num(self, node):
        pass

    def visit_NoOp(self, node):
        pass

    def visit_VarDecl(self, node):
        type_name = node.type_node.value
        type_symbol = self.symtab.lookup(type_name)
        var_name = node.var_node.value
        var_symbol = VarSymbol(var_name, type_symbol)
        self.symtab.define(var_symbol)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_symbol = self.symtab.lookup(var_name)
        if var_symbol is None:
            raise NameError('Var "{}" not declared.'.format(var_name))

        self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        var_symbol = self.symtab.lookup(var_name)
        if var_symbol is None:
            raise NameError('Var "{}" not declared.'.format(var_name))


class Interpreter(NodeVisitor):

    GLOBAL_SCOPE = {}

    def __init__(self, tree):
        self.tree = tree

    def visit_BinOp(self, node):
        op_func = BOP_FUNCS[node.op.type]
        return op_func(self.visit(node.left), self.visit(node.right))

    def visit_UnaryOp(self, node):
        return UOP_FUNCS[node.op.type](self.visit(node.expr))

    def visit_Num(self, node):
        return node.value

    def visit_Program(self, node):
        self.visit(node.block)

    def visit_ProcedureDecl(self, node):
        pass

    def visit_Block(self, node):
        for decl in node.declarations:
            self.visit(decl)
        self.visit(node.compound_statements)

    def visit_VarDecl(self, node):
        pass

    def visit_Type(self, node):
        pass

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise NameError("Unresolved ref to '{}'".format(repr(var_name)))
        else:
            return val

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.tree
        if tree is None:
            return ''
        else:
            return self.visit(tree)
