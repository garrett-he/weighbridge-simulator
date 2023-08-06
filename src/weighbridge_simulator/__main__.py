import click


@click.command()
@click.version_option(message='%(version)s')
def cli():
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""


if __name__ == '__main__':  # pragma: no cover
    cli()
