import importlib.metadata

from click.testing import CliRunner
from weighbridge_simulator.__main__ import cli


def test_cli_version():

    result = CliRunner().invoke(cli, ['--version'])

    assert not result.exception
    assert result.output.strip() == importlib.metadata.version('weighbridge_simulator')
