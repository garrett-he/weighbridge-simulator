# weighbridge-simulator

A command line tool continuously send data to a serial port to simulate
weighbridge communicating.

## Quickstart

1. Start a pair of serial ports:

   ```
   socat -d -d pty,raw,echo=0 pty,raw,echo=0
   ```

2. Prepare a file contains weight list in format:

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

3. Run `wb-simulator` to start simulation:

    ```
    wb-simulator --data-file FILE --port /dev/pts/N
    ```

Then you can receive the weight values from another port in **raw** data format.

## License

Copyright (C) 2024 Garrett HE <garrett.he@outlook.com>

The GNU General Public License (GPL) version 3, see [COPYING](./COPYING).
