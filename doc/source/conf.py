# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pathlib
import sys
import os
import django

BASE_DIR = pathlib.Path(__file__).resolve().parents[2].resolve().as_posix()
REPORT = BASE_DIR + '/reports/'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.path.insert(1, "/oc_lettings_site/")
sys.path.insert(1, "/lettings/")
sys.path.insert(1, "/profiles/")
sys.path.insert(1, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('../../'))
sys.path.insert(1, REPORT)

language = 'fr'

# Setup Django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oc_lettings'
copyright = '2023, VisualDev-fr'
author = 'VisualDev-fr'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx.ext.autodoc"]

exclude_patterns = []

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
