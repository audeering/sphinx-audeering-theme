from subprocess import check_output


# Project -----------------------------------------------------------------
project = 'sphinx-audeering-theme'
author = 'Hagen Wierstorf'
# The x.y.z version read from tags
try:
    version = check_output(['git', 'describe', '--tags', '--always'])
    version = version.decode().strip()
except Exception:
    version = '<unknown>'
title = '{} Documentation'.format(project)

# General -----------------------------------------------------------------
master_doc = 'index'
extensions = []
source_suffix = '.rst'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = [
    'sphinx.ext.autodoc',
]
linkcheck_ignore = [
    'https://sphinx-doc.org',
]

# HTML --------------------------------------------------------------------
html_theme = 'sphinx_audeering_theme'
html_theme_options = {
    'display_version': True,
    'footer_links': False,
    'logo_only': False,
    'wide_pages': ['example-wide-pages'],
}
html_context = {
    'display_github': True,
}
html_title = title


# LaTeX -------------------------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'sphinx-audeering-theme-{}.tex'.format(version),
     title, author, 'manual'),
]
