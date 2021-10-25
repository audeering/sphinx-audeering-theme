Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_,
and this project adheres to `Semantic Versioning`_.


Version 1.1.1 (2021-10-25)
--------------------------

* Fixed: bottom margin of paragraphs in API


Version 1.1.0 (2021-10-25)
--------------------------

* Changed: use new logo, favicon and colors from audEERING homepage
* Changed: link only to root of repo in Github/Gitlab links in the page header
* Changed: ``pygments`` style to ``friendly``
* Changed: remove border around code blocks
* Changed: inline code has no longer a background color or border
* Changed: let example section in API docs appear like other sections
* Changed: remove bullet points in API listings
* Changed: use only red or grey for admonitions
* Fixed: bottom margin for table headers


Version 1.0.14 (2021-07-27)
---------------------------

* Fixed: reduce bottom margin for tables in docstring


Version 1.0.13 (2021-07-20)
---------------------------

* Fixed: pin ``docutils<0.17`` to avoid formatting errors


Version 1.0.12 (2021-05-03)
---------------------------

* Fixed: Javascript error in search for ``sphinx>=3.4.0``


Version 1.0.11 (2021-02-10)
---------------------------

* Fixed: pin ``sphinx-rtd-theme`` to version 0.4.3
  to avoid CSS and font incompatibilities


Version 1.0.10 (2021-01-26)
---------------------------

* Added: link to internal models page in footer


Version 1.0.9 (2020-12-09)
--------------------------

* Fixed: code example on the documentation page for wide pages


Version 1.0.8 (2020-11-24)
--------------------------

* Changed: switch PNG version of audEERING logo for SVG logo
* Fixed: included missing JS file for search


Version 1.0.7 (2020-10-27)
--------------------------

* Added: long-description to ``setup.cfg``,
  which will be shown on pypi.org
* Added: links to usage and installation documentation to README
* Fixed: multi-line statements in Github release changelog


Version 1.0.6 (2020-10-22)
--------------------------

* Fixed: release instructions for Github


Version 1.0.5 (2020-10-22)
--------------------------

* Changed: show only bullet points in Github release
* Fixed: support multi-line changelog entries in Github release
* Fixed: replaces missing 1.0.4 version


Version 1.0.4 (2020-10-22)
--------------------------

* Changed: show only bullet points in Github release
* Fixed: support multi-line changelog entries in Github release


Version 1.0.3 (2020-10-22)
--------------------------

* Added: create automatic releases on Github
* Changed: switch to Github pages for documentation


Version 1.0.2 (2020-10-21)
--------------------------

* Added: support for "Edit on Github" links


Version 1.0.1 (2020-10-20)
--------------------------

* Added: badges to :file:`README.rst`
* Added: list theme features in :file:`README.rst`


Version 1.0.0 (2020-10-20)
--------------------------

* Added: test for broken links in docs


Version 1.0.0-rc2 (2020-10-19)
------------------------------

* Fixed: removed long description from package


Version 1.0.0-rc1 (2020-10-19)
------------------------------

* Added: first public release on Github


Version 0.9.1 (2020-09-29)
--------------------------

* Added: link to documentation to :file:`setup.cfg`


Version 0.9.0 (2020-09-25)
--------------------------

* Added: links to main documentation pages in footer,
  can be disabled by the theme option ``footer_links``
* Added: date the documentation was built to footer


Version 0.8.0 (2020-09-17)
--------------------------

* Added: style jupyter-sphinx plugin by overwriting it's CSS file
  using ``!important``


Version 0.7.2 (2020-08-25)
--------------------------

* Fixed: use 0.4.3 RTD CSS file to fix CSS issues


Version 0.7.1 (2020-06-15)
--------------------------

* Fixed: include missing favicon into wheel package


Version 0.7.0 (2020-06-12)
--------------------------

* Added: :file:`setup.cfg` to define metadata of package
* Changed: switch from MIT to audEERING license
  as we use official logos


Version 0.6.1 (2020-03-24)
--------------------------

* Changed: use safer name ``audeering-wide.css`` for CSS for wide pages


Version 0.6.0 (2020-03-24)
--------------------------

* Added: ``wide_pages`` theme option
* Added: support for Python 3.8
* Added: automatic Python package publishing


Version 0.5.6 (2019-11-18)
--------------------------

* Removed: Python 2.7 support
* Fixed: "Edit on Gitlab" link on Gitlab CI


Version 0.5.5 (2019-11-15)
--------------------------

* Added: test for "Edit on Gitlab" URL extraction
* Fixed: "Edit on Gitlab" link for projects


Version 0.5.4 (2019-11-15)
--------------------------

* Fixed: "Edit on Gitlab" link for sub-projects


Version 0.5.3 (2019-10-16)
--------------------------

* Fixed: make table captions equal to figure captions
* Fixed: figure captions for singlehtml pages


Version 0.5.2 (2019-10-11)
--------------------------

* Changed: switch Sphinx URL in footer to internal doc


Version 0.5.1 (2019-10-09)
--------------------------

* Fixed: automatic branch name on Gitlab CI


Version 0.5.0 (2019-10-09)
--------------------------

* Added: "Edit on Gitlab" link


Version 0.4.0 (2019-10-02)
--------------------------

* Changed: remove Sphinx related documentation
* Fixed: Gitlab and Artifactory URLs


Version 0.3.6 (2019-09-13)
--------------------------

* Fixed: add space for download symbol for notebooks


Version 0.3.5 (2019-09-13)
--------------------------

* Fixed: download symbol for Jupyter notebooks


Version 0.3.4 (2019-09-03)
--------------------------

* Added: documentation examples for tables
* Fixed: several CSS flaws for tables


Version 0.3.3 (2019-08-16)
--------------------------

* Changed: deploy documentation as Gitlab pages
* Fixed: footer link to theme


Version 0.3.2 (2019-07-15)
--------------------------

* Added: support for Python 2.7
* Fixed: links to internal Gitlab server in docs


Version 0.3.1 (2019-07-09)
--------------------------

* Added: Gitlab CI tests
* Changed: switch to `Keep a Changelog`_ format
* Changed: documentation to internal PyPI server


Version 0.3.0 (2019-02-27)
--------------------------

* Changed: switch to PNG logo
* Changed: update red and black color


Version 0.2.1 (2019-02-27)
--------------------------

* Fixed: heading colors in left menu


Version 0.2.0 (2019-02-04)
--------------------------

* Added: Jupyter notebook line


Version 0.1.1 (2019-01-08)
--------------------------

* Changed: adjust red background color
* Changed: adjust a:hover color


Version 0.1.0 (2019-01-08)
--------------------------

* Added: initial release


.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

