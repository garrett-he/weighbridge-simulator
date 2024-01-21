from pathlib import Path


def get_resource_filepath(filename: str) -> Path:
    return Path(__file__).parent.joinpath(filename)
