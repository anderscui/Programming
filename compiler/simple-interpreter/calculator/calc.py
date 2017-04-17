# coding=utf-8

from operator import add, sub, mul, ifloordiv, mod

# Token types
# EOF token is used to indicate that there is no more input left for
# lexical analysis
INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, MUL, DIV, MOD = 'PLUS', 'MINUS', 'MULTI', 'DIV', 'MOD'

CHAR_OPS = {'+': PLUS, '-': MINUS, '*': MUL, '/': DIV, '%': MOD}
OP_FUNCS = {PLUS: add, MINUS: sub, MUL: mul, DIV: ifloordiv, MOD: mod}


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of a token instance.

        Examples:
            Token(INTEGER, 1)
            Token(PLUS, '+')
        :return: str repr of a token.
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


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

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char in CHAR_OPS:
                token = Token(CHAR_OPS[self.current_char], self.current_char)
                self.advance()
                return token

            self.error()

        return Token(EOF, None)


class Interpreter(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, msg='Invalid syntax'):
        raise ValueError(msg)

    def eat(self, expected_type):
        """ Compare the current token type with the passed token
            type and if they match then "eat" the current token
            and assign the next token to the self.current_token,
            otherwise raise an exception.
        :param expected_type:
        :return:
        """
        if self.current_token.type == expected_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def get_next_term(self):
        # expect a op token
        op = self.current_token
        if op.type in OP_FUNCS:
            self.eat(op.type)
        else:
            self.error('operator expected')

        # expect another int token
        next_term = self.term()

        return op, next_term

    def factor(self):
        """factor: INTEGER"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """term: factor ((MUL | DIV) factor)*"""
        result = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()
        return result

    def expr(self):
        """Arithmetic exp parser / interpreter

        expr: term ((PLUS | MINUS) term)*
        term: factor ((MUL | DIV) factor)*
        factor: INTEGER
        """
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result


if __name__ == '__main__':
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text:
            continue

        text = text.strip()
        lexer = Lexer(text)
        inter = Interpreter(lexer)
        result = inter.expr()
        print(result)
