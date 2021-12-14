# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re
import datetime
import os
import sys

# -- Project information -----------------------------------------------------
project = 'BioSimulators documentation'
copyright = '{}, BioSimulators Team'.format(datetime.datetime.now().year)
author = 'BioSimulators Team'

# The short X.Y version
version = ''
release = ''

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.addmetahtml',
    'sphinxprettysearchresults',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set 'language' from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

show_authors = False
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_logo = "_static/biosimulators-logo.svg"

html_css_files = [
    'css/biosimulators.css',
]

html_theme_options = {
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "https://github.com/biosimulations/biosimulations/raw/dev/libs/shared/assets/src/assets/icons/favicon-16x16.png",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "https://github.com/biosimulations/biosimulations/raw/dev/libs/shared/assets/src/assets/icons/favicon-32x32.png",
        },
    ],

    "show_toc_level": 4,
    "navigation_depth": 5,
    "collapse_navigation": True,
    "show_prev_next": False,
    "use_edit_page_button": True,
    "navigation_with_keys": False,

    "search_bar_text": "Enter text to search for ...",

    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/biosimulators/biosimulators.github.io",
            "icon": "fab fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/biosimulators",
            "icon": "fab fa-twitter",
        },
        {
            "name": "Email",
            "url": "mailto:info@biosimulators.org",
            "icon": "fas fa-envelope",
        },
    ],
    "icon_links_label": "Quick links",

    "navbar_center": [
    ],
    "navbar_end": [
        "navbar-icon-links.html",
    ],
    "footer_items": [
        "copyright",
    ],
}

html_context = {
    "github_user": "biosimulators",
    "github_repo": "biosimulators.github.io",
    "github_version": "dev",
    "doc_path": "docs-src",
}

html_sidebars = {
    "**": [
        "search-field.html",
        "sidebar-nav-bs.html",
    ]
}

# -- redirect to https://docs.biosimulations.org  ------------------------

addmetahtml_content = '<meta http-equiv="refresh" content="0; url=https://docs.biosimulations.org/" />'
addmetahtml_enabled = True
