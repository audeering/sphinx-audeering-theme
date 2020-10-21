from distutils.version import LooseVersion

import pytest
from sphinx import __version__

import sphinx_audeering_theme

SPHINX_LT_17 = LooseVersion(__version__) < LooseVersion('1.7')

if SPHINX_LT_17:
    from sphinx import build_main
else:
    from sphinx.cmd.build import build_main

THEMES = ['sphinx_audeering_theme']


BASIC_CONF = """
source_suffix = '.rst'
master_doc = 'index'
html_theme = '{theme}'
"""

BASIC_INDEX = """
Title
=====

Just a test
"""


@pytest.mark.parametrize('theme', THEMES)
def test_basic(tmpdir, theme):
    # Just make sure the docs build with the specified theme
    # (to make sure e.g. that no templates are missing)

    with open(tmpdir.join('conf.py').strpath, 'w') as f:
        f.write(BASIC_CONF.format(theme=theme))

    with open(tmpdir.join('index.rst').strpath, 'w') as f:
        f.write(BASIC_INDEX.format(theme=theme))

    src_dir = tmpdir.strpath
    html_dir = tmpdir.mkdir('html').strpath

    if SPHINX_LT_17:
        status = build_main(argv=['sphinx-build', '-W', '-b', 'html',
                                  src_dir, html_dir])
    else:
        # As of Sphinx 1.7, the first argument is now no longer ignored
        status = build_main(argv=['-W', '-b', 'html', src_dir, html_dir])

    assert status == 0


@pytest.mark.parametrize('url,expected_user,expected_repo', [
    (
        ('https://gitlab.audeering.com/project/altavista-cc/'
         'data-analysis/analyze-altavistacc-test-set.git'),
        'project/altavista-cc/data-analysis',
        'analyze-altavistacc-test-set',
    ),
    (
        ('https://gitlab.audeering.com/project/altavista-cc/'
         'data-analysis/analyze-altavistacc-test-set'),
        'project/altavista-cc/data-analysis',
        'analyze-altavistacc-test-set',
    ),
    (
        'git@srv-app-01.audeering.local:tools/sphinx-audeering-theme.git',
        'tools',
        'sphinx-audeering-theme',
    ),
    (
        'git@srv-app-01.audeering.local:tools/audata.git',
        'tools',
        'audata',
    ),
    (
        'git@github.com:audeering/audeer.git',
        'audeering',
        'audeer',
    ),
    (
        'https://github.com/audeering/audeer.git',
        'audeering',
        'audeer',
    ),
])
def test_parse_remote_url(url, expected_user, expected_repo):
    user, repo = sphinx_audeering_theme.parse_remote_url(url)
    assert user == expected_user
    assert repo == expected_repo
