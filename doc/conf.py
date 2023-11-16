# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UPRI EarthquakeHub'
copyright = '2023, UPRI'
author = 'UPRI'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinxcontrib.openapi', 'sphinxcontrib.redoc']
openapi_spec_path = ['doc/ehub-backend/api-docs/ehub-backend-api-docs.json']
redoc_uri = 'https://unpkg.com/redoc@2.0.0-rc.66/bundles/redoc.standalone.js'
redoc = [
    {
        'name': 'UPRI',
        'page': 'ehub-backend/api-docs/index',
        'spec': 'ehub-backend/api-docs/ehub-backend-api-docs.json',
        'embed': True,
    },

]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_css_variables": {
        "color-header-background": "#3a6a50",
        "color-brand-content": "#7C4DFF",
    },
}
