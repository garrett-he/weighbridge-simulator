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
@click.option('-p', '--port', help='Name of serial port.', metavar='NAME', type=str, required=True)
@click.option('-d', '--data-file', help='Path of data file.', metavar='PATH', type=click.File('r', encoding='ascii'), required=True)
@click.option('-l', '--loops', help='Loops of sending data set, zero means endless.', metavar='N', type=int, default=1)
def main(port: str, data_file: TextIO, loops: int):
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""

    ser = Serial(port)

    i = 0

    lines = data_file.readlines()
    while loops == 0 or i < loops:
        with click.progressbar(lines, label=f'[{i}/{loops}] Sending data set to port: {port}') as items:
            for item in items:
                ser.write(item.strip()[::-1].encode('ascii') + b'=')
                time.sleep(0.2)

        i += 1

    ser.close()
