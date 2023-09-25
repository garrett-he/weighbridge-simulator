from click.testing import CliRunner

from weighbridge_simulator import __version__
from weighbridge_simulator.__main__ import cli


def test_cli_version():
    result = CliRunner().invoke(cli, ['--version'])

    assert not result.exception
    assert result.output.strip() == __version__
