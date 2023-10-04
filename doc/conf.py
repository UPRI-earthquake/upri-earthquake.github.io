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


              # Add the 'sphinxcontrib.httpdomain' extension to your extensions list
extensions = ['myst_parser',
              'sphinxcontrib-swaggerdoc',
              'sphinxcontrib-httpdomain']  # Include the 'sphinxcontrib.httpdomain' extension

# Add the path to your Swagger JSON file as a configuration option
swaggerdoc_api_spec = 'https://github.com/alyssapatricia/ui/blob/main/doc/ehub-backend/api-docs/ehub-backend-api-docs.json'

# Set the base URL for your Swagger documentation (GitHub Pages URL)
swaggerdoc_basepath = '/ui/'  # Replace '<repository-name>' with your GitHub repository name


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
