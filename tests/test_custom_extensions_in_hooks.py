# -*- coding: utf-8 -*-

import os
import codecs

import pytest

from cookiecutter import main


@pytest.fixture
def template():
    return 'tests/test-extensions/custom-extension'


@pytest.fixture
def output_dir(tmpdir):
    return str(tmpdir.mkdir('hello'))


@pytest.fixture(autouse=True)
def modify_syspath(monkeypatch):
    # Make sure that the custom extension can be loaded
    monkeypatch.syspath_prepend(
        'tests/test-extensions/hello_extension'
    )


def test_pre_generate_hook(template, output_dir):
    project_dir = main.cookiecutter(
        template,
        no_input=True,
        output_dir=output_dir,
        extra_context={
            'project_slug': 'foobar',
            'name': 'Cookiemonster',
        },
    )

    readme_file = os.path.join(project_dir, 'README.rst')

    with codecs.open(readme_file, encoding='utf8') as f:
        readme = f.read().strip()

    assert readme == 'Hello Cookiemonster!'
