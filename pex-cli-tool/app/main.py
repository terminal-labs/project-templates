import click

import cli_passthrough.passthrough as passthrough

@click.group()
def cli():
    pass

@cli.command()
def df():
    exit_status = passthrough.passthrough('df -h')

if __name__ == '__main__':
    df()
