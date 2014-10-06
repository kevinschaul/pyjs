#!/usr/bin/env python

import os
import sys

import cli

import lexer

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

    def main(self):
        """
        TODO
        """
        self.lexer.tokenize('"stuff" 23 007 1 0.234 -23')

def launch_new_instance():
    """
    Launch an instance of PyJS.

    This is the entry function of the command-line tool `pyjs`.
    """
    pyjs = PyJS()
    pyjs.main()

if __name__ == '__main__':
    launch_new_instance()

