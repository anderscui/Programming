# coding=utf-8

# Token types
# EOF token is used to indicate that there is no more input left for lexical
# analysis
from operator import add, sub
import re

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'
RE_WS = re.compile('\s+', re.U)
OP_FUNCS = {PLUS: add, MINUS: sub}


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


class Interpreter(object):
    def __init__(self, text):
        self.text = self.preprocess_text(text)
        self.pos = 0
        self.current_token = None

    def preprocess_text(self, text):
        return RE_WS.sub('', text)

    def error(self):
        raise ValueError('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        cur_char = text[self.pos]
        if cur_char.isdigit():
            next_pos = self.pos + 1
            while next_pos < len(text) and text[next_pos].isdigit():
                next_pos += 1
            token = Token(INTEGER, int(text[self.pos: next_pos]))
            self.pos = next_pos
            return token

        if cur_char == '+':
            token = Token(PLUS, cur_char)
            self.pos += 1
            return token
        elif cur_char == '-':
            token = Token(MINUS, cur_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, expected_type):
        """ Compare the current token type with the passed token
            type and if they match then "eat" the current token
            and assign the next token to the self.current_token,
            otherwise raise an exception.
        :param expected_type:
        :return:
        """
        if self.current_token.type == expected_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        # expect a int token
        left = self.current_token
        self.eat(INTEGER)

        # expect a op token
        op = self.current_token
        op_func = None
        if op.type in OP_FUNCS:
            self.eat(op.type)
            op_func = OP_FUNCS[op.type]

        # expect another int token
        right = self.current_token
        self.eat(INTEGER)

        return op_func(left.value, right.value)


if __name__ == '__main__':
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text:
            continue

        text = text.strip()
        inter = Interpreter(text)
        result = inter.expr()
        print(result)
