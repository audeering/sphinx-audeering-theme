"""audEERING Sphinx theme."""
import os
import re
import subprocess


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def git_html_context():
    """Extract HTML context settings for Edit on Gitlab link."""
    # Add default values for "Edit on Gitlab"
    branch = _run(r'git branch | grep \* | cut -d " " -f2')
    # Correct branch name on Gitlab CI
    branch = os.getenv('CI_COMMIT_REF_NAME', branch)
    # Correct branch name on Github Actions
    if os.getenv('GITHUB_REF', None) is not None:
        branch = os.getenv('GITHUB_REF').split('/')[-1]
    origin = _run('git config --get remote.origin.url')
    user, repo = parse_remote_url(origin)
    html_context = {
        'display_gitlab': True,
        'gitlab_host': 'gitlab.audeering.com',
        'gitlab_user': user,
        'gitlab_repo': repo,
        'gitlab_version': branch,
        'display_github': False,
        'github_user': user,
        'github_repo': repo,
        'github_version': branch,
        'conf_py_path': '/docs/',
    }
    return html_context


def parse_remote_url(url):
    """Extract user, repo from URL."""
    repo_urls = [
        'https://gitlab.audeering.com/',
        'http://gitlab.audeering.local/',
        'http://gitlab2.audeering.local/',
        'git@srv-app-01.audeering.local:',
        r'^.*@gitlab.audeering.com/',
        'https://github.com/',
        'git@github.com:',
    ]
    for repo_url in repo_urls:
        url = re.sub(repo_url, '', url)
    url_parts = url.split('/')
    repo = url_parts[-1]
    user = '/'.join(url_parts[:-1])
    if repo.endswith('.git'):
        repo = repo[:-4]
    return (user, repo)


# See
# http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
# noqa: E501
def setup(app):
    is_git = _run('if [ -d .git ] || git rev-parse --git-dir; then echo 1; fi')
    if is_git:
        html_context = git_html_context()
    else:
        # Don't show "Edit on Gitlab"
        html_context = {
            'display_gitlab': False,
        }
    # Set default values only if not otherwise specified in conf.py
    for key, value in html_context.items():
        if key not in app.config.html_context:
            app.config.html_context[key] = value

    # Force displaying last build date
    if app.config.html_last_updated_fmt is None:
        app.config['html_last_updated_fmt'] = '%Y/%m/%d'

    app.add_html_theme('sphinx_audeering_theme',
                       os.path.abspath(os.path.dirname(__file__)))


def _run(shell_command):
    """Return the output of a shell command provided as string."""
    process = subprocess.Popen(
        shell_command,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True
    )
    stdout, sterr = process.communicate()
    return stdout.decode('utf-8').rstrip()
