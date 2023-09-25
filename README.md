# weighbridge-simulator

![license](https://img.shields.io/github/license/garrett-he/weighbridge-simulator)
![status](https://img.shields.io/pypi/status/weighbridge-simulator)
![build](https://img.shields.io/github/actions/workflow/status/garrett-he/weighbridge-simulator/ubuntu-jammy.yml)
![version](https://img.shields.io/pypi/v/weighbridge-simulator)
![python](https://img.shields.io/pypi/pyversions/weighbridge-simulator)

A command line tool continuously send data to a serial port to simulate
weighbridge communicating.

## Install

You can install this tool by the following methods:

1. Install `weighbridge-simulator` by `pip`:
   ```
   pip install git+ssh://git@github.com/garrett-he/weighbridge-simulator.git
   ```

2. Download compiled binary files from [Repository Releases][1].

## Quickstart

1. Prepare a file contains weight list in format:

   ```
   000.000
   000.020
   000.160
   000.420
   000.780
   005.660
   005.800
   006.040
   006.120
   006.100
   006.080
   ...
   ```

2. Run `wb-simulator` to start simulation:

    ```
    wb-simulator --data-file FILE
    ```

Then you can receive the weight values from the created port `/dev/pts/N` in *
*raw** data format.

> `weighbridge-simulator` will convert the input data into **raw**
> weighbridge format before sending it to a serial port, like:
>
> `012.345` will be converted to `543.210=`

## Usage

```
Usage: wb-simulator [OPTIONS]

  A command line tool continuously send data to a serial port to simulate
  weighbridge communicating.

Options:
  -p, --port NAME       Name of serial port.
  -d, --data-file PATH  Path of data file.  [required]
  -l, --loops N         Loops of sending data set, zero means endless.
  -i, --interval SECS   Interval of each data.
  --version             Show the version and exit.
  --help                Show this message and exit.
```

## License

Copyright (C) 2023 Garrett HE <garrett.he@hotmail.com>

The BSD 3-Clause License, see [LICENSE](./LICENSE).

[1]: https://github.com/garrett-he/weighbridge-simulator/releases
