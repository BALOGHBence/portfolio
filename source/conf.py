# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Portfolio"
copyright = "2024, Bence Balogh"
author = "Bence Balogh"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

# Add custom CSS file
html_css_files = [
    "custom.css",
]

# -- Options for the used Sphinx theme ----------------------------------------
# https://pradyunsg.me/furo/

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "use_edit_page_button": False,
    "logo": {
        "text": "Home",
    },
    "header_links_before_dropdown": 6,
}

html_sidebars = {"**": []}

# -- Options for bibtex ----------------------------------------
bibtex_bibfiles = ["refs.bib"]
