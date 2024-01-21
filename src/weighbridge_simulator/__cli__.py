import click

from weighbridge_simulator import __version__

def print_version(ctx: click.Context, _, value: str):
    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()


@click.command()
@click.option('--version', help='Show version information.', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def main():
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""
