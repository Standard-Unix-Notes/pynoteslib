==========
PYNOTESLIB
==========

**PyNoteslib** is a library of functions and classes to assist in building apps to
manage GPG encrypted notes.

It is based upon an earlier project of mine *Standard unix Notes* which was a set of bourne shell scripts that implemented an easy way to manage gpg encrypted notes.

Pynoteslib follows the same structure


Overview
--------


.. start-badges

.. list-table::
    :widths: 33 67
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pynoteslib/badge/?style=flat
    :target: https://pynoteslib.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/Standard-Unix-Notes/pynoteslib.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/Standard-Unix-Notes/pynoteslib

.. |version| image:: https://img.shields.io/pypi/v/pynoteslib.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pynoteslib

.. |wheel| image:: https://img.shields.io/pypi/wheel/pynoteslib.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pynoteslib

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pynoteslib.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pynoteslib

.. |commits-since| image:: https://img.shields.io/github/commits-since/Standard-Unix-Notes/pynoteslib/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/Standard-Unix-Notes/pynoteslib/compare/v0.0.1...master



.. end-badges

Encrypted Library

* Free software: MIT license

Installation
------------

::

    pip install pynoteslib

You can also install the in-development version with::

    pip install https://github.com/Standard-Unix-Notes/pynoteslib/archive/master.zip


Documentation
-------------


The documentation for the library is hosted on ReadTheDocs.io at `<https://pynoteslib.readthedocs.io/>`_


Development
-----------

Contributions and pull requests are welcome: see the `documentation <https://pynoteslib.readthedocs.io/en/latest/contributing.html>`_ for details.

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            Currently not available for Windows

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

