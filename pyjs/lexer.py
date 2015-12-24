import ply.lex as lex

class Lexer(object):
    """
    Logic to create a lexicon analyzer
    """
    tokens = (
        'NUMBER',
        'STRING',
        'TEXT',
    )

    t_ignore = ' '

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self, data):
        self.lexer.input(data)
        ret = []
        while True:
            token = self.lexer.token()
            if not token:
                break
            print token
            ret.append(token)
        return ret

    def t_NUMBER(self, t):
        r'-?[0-9]+(?:\.[0-9]+)*'
        t.value = float(t.value)
        return t

    def t_STRING(self, t):
        r'"[^ ]+"'
        t.value = t.value[1:-1]
        return t

    def t_TEXT(self, t):
        r'[^ ]+'
        return t

    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
