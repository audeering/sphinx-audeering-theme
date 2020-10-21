Usage
=====

To use the Sphinx audEERING theme,
add the following to your :file:`docs/conf.py`:

.. code-block:: python

    html_theme = 'sphinx_audeering_theme'


Copyright
---------

The theme sets the ``copyright`` variable
to ``'audEERING GmbH'``,
and displays it in the footer.
You can overwrite it by setting ``copyright``
yourself in :file:`docs/conf.py`, e.g.

.. code-block:: python

    copyright = f'2018-{date.today().year} audEERING GmbH'


Theme options
-------------

You can influence the appearance
by deciding if your project title
and the version of your project should be shown.
To show both add the following to :file:`conf.py`:

.. code-block:: python

    html_theme_options = { 
        'display_version': True,
        'logo_only': False,
    }

If you have pages in your documentation
that profit from :ref:`larger page width <sec-wide-page>`,
you can list their names under:

.. code-block:: python

    html_themes_options = {
        'wide_pages': ['page-name1', 'page-name2'],
    }

In the footer links to main documentation pages are shown.
You can hide those links with:

.. code-block:: python

    html_themes_options = {
        'footer_links': False,
    }

The ``sphinx-audeering-theme`` inherits from sphinx-rtd-theme_
and can be further modified by applying their `configuration settings`_.


Link to Gitlab or Github
------------------------

The theme adds automatically a link 
to the source file in the Gitlab project at the top right of the page.
The link can be adjusted by:

.. code-block:: python

    html_context = {
        'display_gitlab': True, # Integrate Gitlab
        'gitlab_host': 'gitlab.audeering.com',
        'gitlab_user': 'MyUserName', # Username
        'gitlab_repo': 'MyDoc', # Repo name
        'gitlab_version': 'master', # Branch
        'conf_py_path': '/docs/', # Path in the checkout to the docs root
    }

If you don't specify them,
``display_gitlab``, ``gitlab_user``, ``gitlab_repo``, ``gitlab_version``
are automatically extracted from your git repository.
If you are not inside a git repository, ``display_gitlab`` is set to ``False``.

If you use Github and want to display a link to your Github project use:

.. code-block:: python

    html_context = {
        'display_github': True,
    }

As with Gitlab you can specify
``github_host``, ``github_user``, ``githup_repo``, ``github_version``
if needed.


.. _sphinx-rtd-theme:
    https://sphinx-rtd-theme.readthedocs.io/
.. _configuration settings:
    https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
