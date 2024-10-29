# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'holdthedoor'
copyright = '2024, HoldTheDoor'
author = 'HoldTheDoor'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']


html_theme_options = {
    "navbar_end": ["search-field", "navbar-icon-links"],
    "github_url": "https://google.com",  # Replace with your GitHub repo
    "twitter_url": "https://x.com/holdthedoor_ca",  # Optional: Twitter profile link
}