from datetime import date

import toml

import audeer


config = toml.load(audeer.path("..", "pyproject.toml"))

# Project -----------------------------------------------------------------
project = config["project"]["name"]
author = ", ".join(author["name"] for author in config["project"]["authors"])
copyright = f"2020-{date.today().year} audEERING GmbH"
version = audeer.git_repo_version()
title = "Documentation"

# General -----------------------------------------------------------------
master_doc = "index"
extensions = []
source_suffix = ".rst"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extensions = [
    "sphinx.ext.autodoc",
]
linkcheck_ignore = [
    "https://sphinx-doc.org",
    "http://devops.pp.audeering.com",
]

# HTML --------------------------------------------------------------------
html_theme = "sphinx_audeering_theme"
html_theme_options = {
    "display_version": True,
    "footer_links": False,
    "logo_only": False,
    "wide_pages": ["example-wide-pages"],
}
html_context = {
    "display_github": True,
}
html_title = title


# LaTeX -------------------------------------------------------------------
latex_elements = {
    "papersize": "a4paper",
}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "sphinx-audeering-theme-{}.tex".format(version),
        title,
        author,
        "manual",
    ),
]
