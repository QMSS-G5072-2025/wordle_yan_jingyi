autoapi_type = 'python'
import os, sys
sys.path.insert(0, os.path.abspath('../src'))
extensions = ['sphinx.ext.autodoc','sphinx.ext.viewcode','myst_parser','sphinx_autodoc_typehints']
html_theme = 'sphinx_rtd_theme'
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = u"wordle_jy3482"
copyright = u"2025, Jingyi Yan"
author = u"Jingyi Yan"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Do not execute notebooks during doc build
nb_execution_mode = 'off'
