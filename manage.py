import click

from ckuhl import application


@click.group()
def cli():
    """The CLI object"""
    pass


@cli.command('run', help='Run the server in production mode')
def run_prod():
    app = application.create_app()
    app.run()


@cli.command('debug', help='Run the server in debug mode')
def run_debug():
    app = application.create_app(debug=True)
    app.run()


if __name__ == '__main__':
    cli()
