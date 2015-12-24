#!/usr/bin/env python

import os
import sys

import cli

import interpreter
import lexer
import parser

class PyJS(object):
    """
    A horrible JavaScript engine.
    """

    def __init__(self, args=None):
        """
        Get the options from cli.
        """
        self.cli = cli.CLI()
        self.args = self.cli.parse_arguments(args)
        self.lexer = lexer.Lexer()
        #self.parser = parser.Parser()
        #self.interpreter = interpeter.Interpreter()

    def main(self):
        """
        TODO
        """
        text = '"stuff" 23 007 1 0.234 -23'
        tokens = self.lexer.tokenize(text)
        print(tokens)
        #jstree = self.parser.parse(text, lexer=self.lexer)
        #print(jstree)
        #result = self.interpreter.interpret(jstree)
        #print(result)

def launch_new_instance():
    """
    Launch an instance of PyJS.

    This is the entry function of the command-line tool `pyjs`.
    """
    pyjs = PyJS()
    pyjs.main()

if __name__ == '__main__':
    launch_new_instance()

