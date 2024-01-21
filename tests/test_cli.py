from click.testing import CliRunner
from weighbridge_simulator import __version__
from weighbridge_simulator.__cli__ import main


def test_cli_version(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ['--version'])

    assert not result.exception
    assert result.output.strip() == __version__
