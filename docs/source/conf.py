# -- Path setup --------------------------------------------------------------

from sys import path
from os.path import abspath
path.insert(0, abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'randword'
copyright = '2020, Artyom Bezmenov'
author = 'Artyom Bezmenov'

release = '2.7.5'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage'
]

master_doc = 'index'

templates_path = ['_templates']

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']
