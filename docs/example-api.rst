Example: API
============

You can include automatically generated API documentation
from the doctsrings of your modules and functions.
To provide this functionality
you have to add the `sphinx.ext.autodoc`_ to your ``docs/conf.py`` file:

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
    ]

With `sphinx.ext.autodoc`_
you can automatically include the docstring of a module
and all its members with the automodule directive, e.g.

.. code-block:: rst

    .. automodule:: sphinx.theming
        :members:

If you prefer to include only parts of that module
and add headers yourself you could use:

.. code-block:: rst

    Theme
    -----

    .. autoclass:: sphinx.theming.Theme
        :members:

    extract_zip
    -----------

    .. autofunction:: sphinx.theming.extract_zip


Which results in:

Theme
-----

.. autoclass:: sphinx.theming.Theme
    :members:

extract_zip
-----------

.. autofunction:: sphinx.theming.extract_zip

.. _sphinx.ext.autodoc:
    http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _sphinx.ext.napoleon:
    https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _sphinx.ext.viewcode:
    https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
.. _sphinx.ext.intersphinx:
    http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
