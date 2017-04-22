# coding=utf-8
"""SPI - Simple Pascal Interpreter"""

from operator import add, sub, mul, ifloordiv, pow
from operator import pos, neg

INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, MUL, DIV, POW = 'PLUS', 'MINUS', 'MULTI', 'DIV', 'POW'
BEGIN, END, DOT, ASSIGN, SEMI, LPAREN, RPAREN = 'BEGIN', 'END', '.', ':=', ';', '(', ')'
ID = 'ID'

CHAR_OPS = {'+': PLUS, '-': MINUS, '*': MUL, '/': DIV, '^': POW}
BOP_FUNCS = {PLUS: add, MINUS: sub, MUL: mul, DIV: ifloordiv, POW: pow}
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

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

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

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

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

            self.error()

        return Token(EOF, None)


# PARSER #


class AST(object):
    pass


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
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
                    | variable"""
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            return UnaryOp(token, self.factor())
        elif token.type == MINUS:
            self.eat(MINUS)
            return UnaryOp(token, self.factor())
        elif token.type == INTEGER:
            self.eat(INTEGER)
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
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

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

    def program(self):
        """program : compound_statement DOT"""
        node = self.compound_statement()
        self.eat(DOT)
        return node

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


class Interpreter(NodeVisitor):

    GLOBAL_SCOPE = {}

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        op_func = BOP_FUNCS[node.op.type]
        return op_func(self.visit(node.left), self.visit(node.right))

    def visit_UnaryOp(self, node):
        return UOP_FUNCS[node.op.type](self.visit(node.expr))

    def visit_Num(self, node):
        return node.value

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
            raise NameError(repr(var_name))
        else:
            return val

    def visit_NoOp(self, node):
        pass

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ''
        else:
            return self.visit(tree)


class RpnTranslator(NodeVisitor):
    """Print the postfix notation(Reverse Polish Notation) of an arithmetic
    expression"""

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        op = OP_CHARS[node.op.type]
        return '{} {} {}'.format(self.visit(node.left),
                                 self.visit(node.right),
                                 op)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)


class LispTranslator(NodeVisitor):
    """Print the LISP style notation of an arithmetic expression"""

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        op = OP_CHARS[node.op.type]
        return '({} {} {})'.format(op,
                                   self.visit(node.left),
                                   self.visit(node.right))

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
