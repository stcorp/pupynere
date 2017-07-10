import string

from paver.easy import *
from paver.setuputils import setup, find_packages, find_package_data
import paver.doctools
import paver.virtual
from paver.release import setup_meta

options = environment.options
setup(**setup_meta)

options(
    setup=Bunch(
        name='Pupynere',
        version='1.1.0',
        description='Pure Python NetCDF reader and writer.',
        long_description='''
Pupynere is an implementation of the NetCDF library, written from scratch
in Python. It uses ``mmap()`` in order to read the data lazily, without
needing to load everything into memory. It depends only on Numpy, so you
don't need to install the NetCDF library from Unidata.
        ''',
        keywords='netcdf data science climate oceanography meteorology',
        classifiers=filter(None, map(string.strip, '''
            Development Status :: 5 - Production/Stable
            Environment :: Console
            Intended Audience :: Developers
            Intended Audience :: Science/Research
            License :: OSI Approved :: MIT License
            Operating System :: OS Independent
            Programming Language :: Python
            Topic :: Scientific/Engineering
            Topic :: Software Development :: Libraries :: Python Modules
        '''.split('\n'))),
        author='Roberto De Almeida',
        author_email='roberto@dealmeida.net',
        url='http://pupynere.org/',
        license='MIT',

        py_modules=['pupynere'],
        include_package_data=True,
        zip_safe=True,

        test_suite='nose.collector',

        dependency_links=[],
        install_requires=[
            'numpy',
        ],
        extras_require={
            'test': ['nose'],
            'docs': ['Paver', 'Sphinx', 'Pygments'],
        },
    ),
    minilib=Bunch(
        extra_files=['doctools', 'virtual']
    ), 
    virtualenv=Bunch(
        packages_to_install=['Pupynere'],
        script_name='bootstrap.py',
        paver_command_line=None,
        install_paver=True
    ),
    sphinx=Bunch(
        builddir='_build',
    ),
    cog=Bunch(
        includedir='.',
    ),
    deploy=Bunch(
        htmldir = path('pupynere.org'),
        bucket = 'pupynere.org',
    ),
)


if paver.doctools.has_sphinx:
    @task
    @needs(['cog', 'paver.doctools.html'])
    def html():
        """Build the docs and put them into our package."""
        destdir = path('pupynere.org')
        destdir.rmtree()
        builtdocs = path("docs") / options.builddir / "html"
        builtdocs.move(destdir)

    @task
    @needs(['cog', 'paver.doctools.doctest'])
    def doctest():
        pass


if paver.virtual.has_virtualenv:
    @task
    def bootstrap():
        """Build a virtualenv bootstrap for developing paver."""
        paver.virtual._create_bootstrap(options.script_name,
                options.packages_to_install,
                options.paver_command_line,
                options.install_paver)


@task
@needs(['generate_setup', 'minilib', 'setuptools.command.sdist'])
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass


@task
def deploy():
    """Deploy the HTML to the server."""
    import os
    from boto.s3.connection import S3Connection
    from boto.s3.key import Key

    conn = S3Connection()
    bucket = conn.create_bucket(options.bucket)
    bucket.set_acl('public-read')

    for root, dirs, files in os.walk(options.htmldir):
        for file in files:
            path = os.path.join(root, file)
            k = Key(bucket)
            k.key = path[len(options.htmldir)+1:]  # strip pupynere.org/
            k.set_contents_from_filename(path)
            k.set_acl('public-read')
