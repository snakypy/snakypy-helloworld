#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by: Snakypy Org, 2019.

import json
import os
from snakypy_helloworld import __PKG_NAME__

class SnakypyHelloworld:
    """
        PyHell class where everything will happen.
    """

    config = {
        'appname': 'Snakypy Helloworld',
        'appexec': f'{__PKG_NAME__}',
        'author': {
            'name': 'Snakypy Org',
            'email': 'contact.snakypy@gmail.com',
            'website': 'https://snakypy.github.io',
            'github': 'snakypy'
        }
    }

    def __init__(self, NAME='World!'):
        """
            Constructor method, gets a parameter with default
            value "World!" case user does not specify parameter
            in optional arguments when executing program.
        """
        self.NAME = NAME

    def get_data(self):
        """
            This method is responsible for reading the program configuration
            JSON file. This file contains information that is used.
        """
        _path = os.path.dirname(os.path.realpath(__file__)) + '/'
        with open(os.path.join(_path, 'data/data.json'), 'r') as f:
            data = json.load(f)
        return data

    def menu(self):
        f"""
            This method is responsible for passing an optional parameter
            to display a custom message on the console. In addition, I also
            displayed other functionality, such as showing help. To do this,
            run {__PKG_NAME__} --help" on the console.
        """
        from argparse import ArgumentParser, RawTextHelpFormatter
        try:
            parser = ArgumentParser(prog=self.config['appname'],
                                    usage=f'{self.config["appexec"]} <optional arguments>',
                                    description=f'{self.config["appexec"]} is a simple script ' +
                                                'with parameterized to show Hello message.',
                                    formatter_class=RawTextHelpFormatter,
                                    epilog="See you later!!")
            parser.add_argument('--name', '-n',
                                help='This option shows welcome to someone.')
            args = parser.parse_args()
            return args
        except Exception as err:
            print('Error in passing arguments...', err)

    def message(self):
        """
            Method responsible for constructing the message that will
            be displayed to the user. Depending on the argument passed,
            Hello's message changes.
        """
        try:
            if self.menu().name is None and self.NAME == 'World!':
                return 'Hello, World!'
                print('I was raised with Python. :)')
            elif self.menu().name is not None and self.NAME == 'World!':
                return f'Hello, Mr(s) {self.menu().name.title()}!'
            elif self.menu().name is None and self.NAME != 'World!':
                return f'Hello, Mr(s) {self.NAME.title()}!'
            else:
                return None
        except Exception as err:
            print('There was some error in the parameterization.', err)

    def __str__(self):
        """
            Python's special method for returning a Hello message when
            executing the Snakypy Helloworld class.
        """
        header = self.get_data()['head']
        body = self.message()
        footer = 'I was raised with Python. :)'
        return f'{header}\n{body}\n{footer}'


if __name__ == '__main__':
    print(SnakypyHelloworld())
