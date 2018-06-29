import click

@click.group()
def cli():
    pass

@cli.command()
def test():
    click.echo("good")

main = cli
