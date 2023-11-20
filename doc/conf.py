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

extensions = ['myst_parser', 'sphinxcontrib.redoc']
redoc_uri = 'https://unpkg.com/redoc@2.0.0-rc.66/bundles/redoc.standalone.js'
redoc = [
    {
        'name': 'UPRI EarthquakeHub API Docs',
        'page': 'ehub-backend/api-docs/index',
        'spec': 'ehub-backend/api-docs/ehub-backend-api-docs.json',
        'embed': True,
    },
    {
        'name': 'UPRI EarthquakeHub API Docs',
        'page': 'sender-backend/api-docs/index',
        'spec': 'sender-backend/api-docs/sender-backend-api-docs.json',
        'embed': True,
    },


]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = "UPRI EarthquakeHub documentation"
html_static_path = ['_static']
html_theme_options = {
    "announcement": "<em> 😋 Important</em> announcement!",
    "light_css_variables": {
        ## Color
        "color-header-background": "#f1f1e8",
        "color-header-text": "#fcfbf3",
        "color-sidebar-link-text--top-level": "#3a6a50",
        "color-background-primary":"#fcfbf3",
        "color-background-secondary":"#f1f1e8",
        "color-link": "#00b0ff",
        "color-sidebar-item-background--current": "#f1f1e8"
    },

    "dark_css_variables": {
        ## Color
        "color-header-background": "#3a6a50",
        "color-header-text": "#fcfbf3",
        "color-sidebar-link-text--top-level": "#f1f1e8",
        "color-link": "#00b0ff",
        "color-background-secondary":"#28292a",
    },
}
html_logo = "_build/html/_static/upri-logo.png"
