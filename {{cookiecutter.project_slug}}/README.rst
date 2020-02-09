{{cookiecutter.project_name}}
=============================


``{{cookiecutter.project_name}}`` is a simple script with parameterized to show Hello message.
The focus of this project is to show how to create a package for PyPi.
You can download the package and study it. :)

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
------------

Latest PyPI stable release
~~~~~~~~~~~~~~~~~~~~~~~~~~

|PyPI-Status| |PyPI-Download-Day|

.. code:: sh

    pip install {{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}


Usage
-----

.. code:: sh

    $ {{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}

...with parameter:

.. code:: sh

    $ {{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }} -n MyName

To know help use:

.. code:: sh

    $ {{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }} -h

Latest development release on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GitHub-Status| |GitHub-Stars| |GitHub-Commits| |GitHub-Forks| |GitHub-Last-Commit-Branch| |GitHub-Download-Total|

Pull and install in the current directory:

.. code:: sh

    pip install -e git+https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.git@master#egg={{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}

Changelog
---------

The list of all changes is available either on GitHub's Releases:
|GitHub-Status|, on the
`website <https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}>`__.


LICENCE
-------

Open Source: |LICENCE|


Authors
-------

The main developer are:

- William Canin (`{{cookiecutter.github_username}} <https://github.com/{{cookiecutter.github_username}}>`__)

.. |LICENCE| image:: https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square
   :target: https://raw.githubusercontent.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/master/LICENSE
.. |GitHub-Status| image:: https://img.shields.io/github/tag/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square
   :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/releases
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=social
   :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/stargazers
.. |GitHub-Commits| image:: https://img.shields.io/github/commit-activity/y/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square
   :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/graphs/commit-activity
.. |GitHub-Last-Commit-Branch| image:: https://img.shields.io/github/last-commit/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/master.svg?style=flat-square 
    :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/commits/master
.. |GitHub-Forks| image:: https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square
   :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/network
.. |GitHub-Download-Total| image:: https://img.shields.io/github/downloads/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/total.svg?style=flat-square
   :target: https://github.com/{{cookiecutter.github_username}}/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}/pulse
.. |PyPI-Status| image:: https://img.shields.io/pypi/status/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square
   :target: https://pypi.org/project/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}
.. |PyPI-Download-Day| image:: https://img.shields.io/pypi/dd/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}.svg?style=flat-square 
   :target: https://pypi.org/project/{{ cookiecutter.project_name.lower().replace(' ', '-').replace('_', '-') }}

   