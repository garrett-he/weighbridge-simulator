import time
from typing import TextIO

import click
from serial import Serial


@click.command()
@click.option('-p', '--port', help='Name of serial port.', type=str, required=True)
@click.option('-d', '--data-file', help='Path of data file.', type=click.File('r', encoding='ascii'))
@click.version_option(message='%(version)s')
def cli(port: str, data_file: TextIO):
    """A command line tool continuously send data to a serial port to simulate weighbridge communicating."""

    ser = Serial(port)
    for line in data_file.readlines():
        ser.write(line.strip()[::-1].encode('ascii') + b'=')
        time.sleep(0.2)

    ser.close()


if __name__ == '__main__':  # pragma: no cover
    cli()  # pylint: disable=no-value-for-parameter
