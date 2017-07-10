Changelog
=========

1.1
---

1.1.0
~~~~~

- Incorporated modifications from scipy.io.netcdf.
- Added int64 to int32 conversion.
- Fixed cursor position under Windows.
- Works with mal-formed unicode.
- Improved type conversion between Numpy and Netcdf.
- Added optional automatic masking and conversion of data.
- Added paging for improved mmap().

1.0
---

1.0.15
~~~~~~
- Added fix for empty attributes.

1.0.14
~~~~~~
- Added support for Unicode attributes.

1.0.13
~~~~~~
- Fixed bug when reading character variables without mmap.

1.0.12
~~~~~~
- Fixed bug.

1.0.11
~~~~~~
- Fixed bug.

1.0.10
~~~~~~
- Fixed bug when packing integer attributes in 64-bit systems.

1.0.9
~~~~~
- Should work with Python 2.3.
- Accepts file objects instead of only filenames.

1.0.8
~~~~~
- Allow writing version 2 files (Large Files).

1.0.7
~~~~~
- Removed reads from asserts to allow PYTHONOPTIMIZE.

1.0.6
~~~~~
- Allows zero-length record variables.

1.0.5
~~~~~
- Added the option to open files without using mmap, since mmap can't handle huge files on Windows.

1.0.4
~~~~~
- Fixed packing of dimensions when writing a file. The order was being read from a dictionary (essentially unordered), instead of from the list with the proper order.

1.0.3
~~~~~
- Fixed bug so that it can write scalar variables.

1.0.2
~~~~~
- Fixed broken 1.0.1, ``var.shape`` was returning the current number of records in the first dimension, breaking the detection of record variables.

1.0.1
~~~~~
- Changed the code to read the variable shape from the underlying data object.

1.0.0
~~~~~
- Initial stable release. Handles record arrays properly (using a single mmap for all record variables) and writes files.
