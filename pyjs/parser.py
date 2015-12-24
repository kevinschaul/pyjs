import ply.yacc as yacc

class Parser(object):
   def __init__(self):
        self.parser = yacc.yacc(module=self)
