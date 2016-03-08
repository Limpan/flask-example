import click


@click.group()
def db():
    pass

@db.command()
def init():
    """Initialize database."""
    pass

@db.command()
def drop():
    """Drop entire database."""
    pass
