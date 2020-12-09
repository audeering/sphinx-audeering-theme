.. _sec-wide-page:

Example: wide pages
===================

This is a wide page, specified in :file:`docs/conf.py` by:

.. code-block:: python

   html_theme_options = {
       'wide_pages': ['example-wide-pages'],
   }

.. csv-table:: A wide table
    :header: Label,Parameter1,Parameter2,Parameter3,Parameter4,Measure1,Measure2,Measure3

    Some fancy name1,mega linear classifier,flying,denoised,emotional,0.9,0.6,3.12
    Some fancy name2,giga linear classifier,driving,noisy,emotional,0.8,0.6,4.23

This is useful if you have large tables,
but otherwise you shouldn't use it.
