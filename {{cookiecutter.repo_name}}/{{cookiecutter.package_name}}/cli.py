# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import click


@click.command()
def main():
    print('I am {{cookiecutter.cli_name}}')
