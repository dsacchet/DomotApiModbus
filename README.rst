DomotApiModbus
=========================

DomotApiModbus provide a simple interface to get and set value on a modbus device.

It is composed of a generic modbus class, and specific device class.

In the current version, class for Unelvent Ideo 450 is implemented

Build instructions
------------------

::

  (git repo root) $ virtualenv venv
  (git repo root) $ source venv/bin/activate``
  (git repo root) $ pip install twine``
  (git repo root) $ python setup.py sdist bdist_wheel``
  (git repo root) $ python setup.py install``


The library is available for test in venv

To upload to pypi and then build a .deb package to have a distribution wide setup :

::

  (git repo root) $ ./venv/bin/twine upload dist/*
  (git repo root) $ pypi-install --keep DomotApiModbus