import click

from app import create_app, db

@click.command()
def cli():
    """
    Run the application
    """
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run()