NetCDF reader/writer module.
============================

This module implements the Scientific.IO.NetCDF API to read and create NetCDF files. The same API is also used in the PyNIO and pynetcdf modules, allowing these modules to be used interchangebly when working with NetCDF files. The major advantage of ``scipy.io.netcdf`` over other modules is that it doesn't require the code to be linked to the NetCDF libraries as the other modules do.

The code is based on the `NetCDF file format specification <http://www.unidata.ucar.edu/software/netcdf/guide_15.html>`_. A NetCDF file is a self-describing binary format, with a header followed by data. The header contains metadata describing dimensions, variables and the position of the data in the file, so access can be done in an efficient manner without loading unnecessary data into memory. We use the ``mmap`` module to create Numpy arrays mapped to the data on disk, for the same purpose.

The structure of a NetCDF file is as follows::

    C D F <VERSION BYTE> <NUMBER OF RECORDS>
    <DIMENSIONS> <GLOBAL ATTRIBUTES> <VARIABLES METADATA>
    <NON-RECORD DATA> <RECORD DATA>

Record data refers to data where the first axis can be expanded at will. All record variables share a same dimension at the first axis, and they are stored at the end of the file per record, ie

::

    A[0], B[0], ..., A[1], B[1], ..., etc,
    
so that new data can be appended to the file without changing its original structure. Non-record data are padded to a 4n bytes boundary. Record data are also padded, unless there is exactly one record variable in the file, in which case the padding is dropped.  All data is stored in big endian byte order.

The Scientific.IO.NetCDF API allows attributes to be added directly to instances of ``netcdf_file`` and ``netcdf_variable``. To differentiate between user-set attributes and instance attributes, user-set attributes are automatically stored in the ``_attributes`` attribute by overloading ``__setattr__``. This is the reason why the code sometimes uses ``obj.__dict__['key'] = value``, instead of simply ``obj.key = value``; otherwise the key would be inserted into userspace attributes.

To create a NetCDF file::

    >>> f = netcdf_file('simple.nc', 'w')
    >>> f.history = 'Created for a test'
    >>> f.createDimension('time', 10)
    >>> time = f.createVariable('time', 'i', ('time',))
    >>> time[:] = range(10)
    >>> time.units = 'days since 2008-01-01'
    >>> f.close()

To read the NetCDF file we just created::

    >>> f = netcdf_file('simple.nc', 'r')
    >>> print f.history
    Created for a test
    >>> time = f.variables['time']
    >>> print time.units
    days since 2008-01-01
    >>> print time.shape
    (10,)
    >>> print time[-1]
    9
    >>> f.close()
