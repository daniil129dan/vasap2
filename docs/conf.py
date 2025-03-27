# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys



sys.path.insert(0, os.path.abspath(os.path.join('..', 'djangotutorial')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

project = 'djangotutor'
copyright = '2025, daniil'
author = 'daniil'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',  # для автогенерации подсказок типов
    'sphinxcontrib_django',  # для поддержки Django
]
autodoc_member_order = 'bysource'  # Порядок следования членов по исходному коду
autodoc_default_options = {
    'members': True,  # Включает все члены класса
    'undoc-members': True,  # Включает даже не задокументированные члены
    'show-inheritance': True,  # Показывает наследование классов
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
