import pytest

from click.testing import CliRunner


@pytest.fixture(scope='module')
def cli_runner() -> CliRunner:
    return CliRunner()
