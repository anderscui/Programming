# coding=utf-8
import ply.lex as lex

# list of token names, always required.
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# reg exp rules for 'simple' tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# a reg exp rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# a rule for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# a string containing ignored chars(space and tabs)
t_ignore = ' \t'


# error handling rule
def t_error(t):
    # t.value contains the rest of the input string that has not been tokenized.
    print("Illegal char '%s'" % t.value[0])
    t.lexer.skip(1)


# build the lexer using py reflection to read the rules
lexer = lex.lex(debug=1)


if __name__ == '__main__':
    data = '''3 + 4 * 10 ^
        + -20 * 2
    '''

    lexer.input(data)
    # while True:
    #     token = lexer.token()
    #     if not token:
    #         break
    #     print(token)

    for token in lexer:
        # print(token)
        # token is an instance of type `LexToken`
        print(f'{token.type}, {token.value}, {token.lineno}, {token.lexpos}')
