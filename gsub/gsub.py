#!/usr/bin/python

import click
import os
import glob


def locate_git():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    if glob.glob('.git'):
        pass

@click.command()
@click.option('--show', is_flag=True)
def gsub(show):
    print(show)
    locate_git()


if __name__ == '__main__':
    gsub()
