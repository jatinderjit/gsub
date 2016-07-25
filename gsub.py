import click
import os
import glob


def locate_git():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    if glob.glob('.git'):
        while True:
            os.path.join('cur_dir')


@click.command()
@click.option('--show', is_flag=True)
@click.option('--check', is_flag=True)
def git_dep(show, check):
    print(show)
    print(check)
    locate_git()


if __name__ == '__main__':
    git_dep()