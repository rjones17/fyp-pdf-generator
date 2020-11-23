"""The build configuration file

This python file contains the configuration needed
to customise Sphinx behaviour

https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

import os
import sys

import django

sys.path.insert(0, os.path.abspath("/app"))
os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

# -- Project information -----------------------------------------------------

project: str = "pdfgen"
copyright: str = """2020, jonesrm2"""
author: str = "jonesrm2"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]


# -- Options for HTML output -------------------------------------------------

html_theme: str = "classic"
