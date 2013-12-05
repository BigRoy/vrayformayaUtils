Installation
============

This is a brief 3-step overview of how you could install the vrayformayaUtils package and get started right away!


1. Get the package from the repository
--------------------------------------

**Download via browser**

If you're unfamiliar with the ins and outs of GitHub the easiest way to install the package is to go to the
`vrayformayaUtils GitHub repository <https://github.com/BigRoy/vrayformayaUtils>`_
and click on `**Download ZIP** <https://github.com/BigRoy/vrayformayaUtils/archive/master.zip>`_.

Unpack the downloaded *.zip* file to a location of your choice (see installing the package below for the next steps).


**Checkout via git version control**

If you're somewhat familiar with git then checkout the repository's git and pull all the files locally.


2. Installing the package
-------------------------

Now you should have the files that are in the repository. Between those files should be a directory called
``vrayformayaUtils``, that should be the *PACKAGE*  we need to install. (Note that it's not the root of the repository but
the vrayformayaUtils directory that is inside of it.

The *PACKAGE* is the ``vrayformayaUtils`` directory that directly contain a ``__init__.py`` file.
The easiest way to install is to copy the *PACKAGE* into your maya scripts folder.

    For **windows** the maya scripts folder is something like:

    ``users/*user*/Documents/maya/maya/*version*/scripts``

    For **mac**  the maya scripts folder is something like:

    ``/users/*user*/Library/Preferences/Autodesk/maya/*version*/scripts``

    Where:

    *user*: The user account that has Maya installed on the computer

    *version*: The version of Maya you want to install the scripts for, e.g. *2014-x64*


Note that all that is required for the ``vrayformayaUtils`` package to work is to place it in a position that is in
sys.path for Python.
If your studio uses Maya.env or any other way to add scripts folder to Maya feel free to position the package in there.


3. Testing the installation
---------------------------
If the following code runs in a Python tab in your Autodesk Maya script editor the V-ray for Maya Utils package should
be installed correctly.

.. code-block:: python

    import vrayformayaUtils as vfm


Everything should be ready to go.
Next up: :doc:`getting_started`