import time
from typing import TextIO

import click
from serial import Serial

from weighbridge_simulator import __version__


def print_version(ctx: click.Context, _, value: str):
    if not value or ctx.resilient_parsing:
        return

    click.echo(__version__)
    ctx.exit()


@click.command()
@click.option('--version', help='Show version information.', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.option('-p', '--port', help='Name of serial port.', type=str, required=True)
@click.option('-d', '--data-file', help='Path of data file.', type=click.File('r', encoding='ascii'))
def main(port: str, data_file: TextIO):
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""

    ser = Serial(port)

    for line in data_file.readlines():
        ser.write(line.strip()[::-1].encode('ascii') + b'=')
        time.sleep(0.2)

    ser.close()
