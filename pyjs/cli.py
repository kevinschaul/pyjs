#!/usr/bin/env python

import argparse

class CLI(object):
    """
    Handles command-line interface options
    """

    def parse_arguments(self, args=None):
        """
        Implement command-line arguments
        """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('infile', help='The JavaScript file to\
                execute.')
        return self.parser.parse_args(args)

