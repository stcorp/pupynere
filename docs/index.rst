.. Pupynere documentation master file, created by
   sphinx-quickstart on Thu Apr 26 14:05:07 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pupynere
====================================

This is a Python implementation of the `NetCDF specification <http://www.unidata.ucar.edu/software/netcdf/docs/netcdf.html#NetCDF-Classic-Format>`_ written from scratch. The name started as a tongue-in-cheek joke, being a contraction of PUre PYthon NEtcdf REader. Since the module is written in pure Python there's no need to compile and link it against Unidata's NetCDF library, so this small module became somewhat popular before a more serious name could be found. The module is now also a NetCDF *writer*, so it can be used to create files.

Pupynere implements the same API as other NetCDF modules such as `Scientific.IO.NetCDF <http://dirac.cnrs-orleans.fr/ScientificPython/ScientificPythonManual/Scientific.IO.NetCDF-module.html>`_, `pynetcdf <http://pypi.python.org/pypi/pynetcdf/>`_, `netCDF4-python <http://code.google.com/p/netcdf4-python/>`_ and `scipy.io.netcdf <http://docs.scipy.org/doc/scipy/reference/generated/scipy.io.netcdf.netcdf_file.html>`_ (which is based on Pupynere). If you want to use a more Pythonic API to create NetCDF files, take a look at `Puppy <http://pypi.python.org/pypi/Puppy/>`_.

Even though it is written in Python, Pupynere can efficiently access large NetCDF files since the header will contain the position of the data in the file. This allows the module too ``mmap()`` the data, creating Numpy arrays mapped directly to the data on disk, so that only the data used is read into memory.

Examples
--------

To create a NetCDF file:

.. doctest::

    >>> from pupynere import netcdf_file
    >>> f = netcdf_file('simple.nc', 'w')
    >>> f.history = 'Created for a test'
    >>> f.location = u'北京'
    >>> f.createDimension('time', 10)
    >>> time = f.createVariable('time', 'i', ('time',))
    >>> time[:] = range(10)
    >>> time.units = u'µs since 2008-01-01'
    >>> f.close()

Note the assignment of ``range(10)`` to ``time[:]``.  Exposing the slice of the time variable allows for the data to be set in the object, rather than letting ``range(10)`` overwrite the ``time`` variable.

To read the NetCDF file we just created:

.. doctest::

    >>> f = netcdf_file('simple.nc', 'r')
    >>> print f.history
    Created for a test
    >>> print f.location
    北京
    >>> time = f.variables['time']
    >>> print time.units
    µs since 2008-01-01
    >>> print time.shape
    (10,)
    >>> print time[-1]
    9
    >>> f.close()

Installation
------------

You can install the latest version (|release|) using `pip <http://pypi.python.org/pypi/pip>`_. After `installing pip <http://www.pip-installer.org/en/latest/installing.html>`_ you can install Pupynere with this command:

.. code-block:: bash

    $ pip install Pupynere

This will install Pupynere together with Numpy.

Help
----

If you need any help with Pupynere, please feel free to send an email to the `mailing list <http://groups.google.com/group/pupynere/>`_. You can also open an issue at the `repository <http://code.dealmeida.net/pupynere>`_.

Documentation
-------------

.. toctree::
   :maxdepth: 2

   Changelog
   license



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

