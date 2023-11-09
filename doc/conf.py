# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UPRI EarthquakeHub'
copyright = '2023, UPRI'
author = 'UPRI'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinxcontrib.redoc']
redoc = [
    {
        'name': 'UPRI EarthquakeHub APIs',
        'page': 'api',
        'spec': 'ehub-backend/api-docs/ehub-backend-api-docs.json',  # Specify the path to your OpenAPI JSON file
        'embed': True,
        'opts': {
            'hide-loading': True,
            'theme': 'dark',
            # Add other ReDoc options as needed
        },
    },
]








templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

