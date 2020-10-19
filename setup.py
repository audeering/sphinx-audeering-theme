from setuptools import setup


setup(
    use_scm_version=True,
    package_data={
        'sphinx_audeering_theme': [
            'theme.conf',
            '*.html',
            'static/css/*.css',
            'static/images/*.*',
            'static/*.png',
        ],
    },
    entry_points={
        'sphinx.html_themes': [
            'sphinx_audeering_theme = sphinx_audeering_theme',
        ],
    },
)
