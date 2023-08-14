import time
from typing import TextIO

import click
from serial import Serial


@click.command()
@click.option('-p', '--port', help='Name of serial port.', metavar='NAME', type=str, required=True)
@click.option('-d', '--data-file', help='Path of data file.', metavar='PATH', type=click.File('r', encoding='ascii'),
              required=True)
@click.option('-l', '--loops', help='Loops of sending data set, zero means endless.', metavar='N', type=int, default=1)
@click.version_option(message='%(version)s')
def cli(port: str, data_file: TextIO, loops: int):
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""

    ser = Serial(port)
    i = 0

    while loops == 0 or i < loops:
        with click.progressbar(data_file.readlines(), label=f'[{i}/{loops}] Sending data set to port: {port}') as lines:
            for line in lines:
                ser.write(line.strip()[::-1].encode('ascii') + b'=')
                time.sleep(0.2)

        i += 1

    ser.close()


if __name__ == '__main__':  # pragma: no cover
    cli()  # pylint: disable=no-value-for-parameter
