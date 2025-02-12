import os
import pty
import time
import tty
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
@click.option('-p', '--port', help='Name of serial port.', metavar='NAME', type=str, default=None)
@click.option('-d', '--data-file', help='Path of data file.', metavar='PATH', type=click.File('r', encoding='ascii'), required=True)
@click.option('-l', '--loops', help='Loops of sending data set, zero means endless.', metavar='N', type=int, default=1)
@click.option('-i', '--interval', help='Interval of each data.', metavar='SECS', type=float, default=0.2)
def main(port: str, data_file: TextIO, loops: int, interval: float):
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""

    if port is None:
        master, slave = pty.openpty()
        tty.setraw(master)
        os.set_blocking(master, False)
        out = open(master, 'r+b', buffering=0)  # pylint: disable=consider-using-with
        port_name = os.ttyname(slave)

        click.echo(f'Created PTY: {port_name}')
    else:
        out = Serial(port)
        port_name = port

    i = 0

    lines = data_file.readlines()
    while loops == 0 or i < loops:
        with click.progressbar(lines, label=f'[{i}/{loops}] Sending data set to port: {port_name}') as items:
            for item in items:
                out.write(item.strip()[::-1].encode('ascii') + b'=')
                time.sleep(interval)

        i += 1

    out.close()
