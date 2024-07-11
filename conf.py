# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'QM Pipeline'
copyright = '2024, QCMX, Laboratoire PMC, Ecole Polytechnique'
author = 'QCMX, Laboratoire PMC, Ecole Polytechnique'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autoapi.extension',
    'sphinx_math_dollar',
    'sphinx.ext.mathjax',
    #'sphinx.ext.napoleon',
]

# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html
autoapi_dirs = ['../']
autoapi_type = "python"
autoapi_ignore = ["*sphinx-doc-test*"]
autoapi_keep_files = False

napoleon_google_docstring = False
napoleon_use_param = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
