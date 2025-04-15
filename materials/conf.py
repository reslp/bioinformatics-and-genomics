import os
import sys
from datetime import datetime
import subprocess

# check if documentation is built on the rtd server, in which case the conversion script needs to be run first.
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
	subprocess.check_call(['python', 'convert-gfm.py']) 

#sys.path.append(os.path.join(os.environ["SAMPLE_DOCS_LOCATION"], "demo"))
#print("", sys.path[-1], "", sep="\n" + "-" * 80 + "\n")

#from recommonmark.parser import CommonMarkParser
#from mdx_gfm import GithubFlavoredMarkdownExtension

source_suffix = ['.rst', '.md']
#source_parsers = {'.md': CommonMarkParser}
#source_parsers = {'.md': GithubFlavoredMarkdownExtension()}

# -- Project information -----------------------------------------------------

project = "Genomic Methods"
copyright = "2025, Philipp Resl, Claudio G. Ametrano and Christoph Hahn"
author = "Philipp Resl, Claudio G. Ametrano and Christoph Hahn"

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "sphinx_markdown_tables",
#    "recommonmark",
    "myst_parser",
]

# -- Options for HTML output -------------------------------------------------

html_title = project

# NOTE: All the lines are after this are the theme-specific ones. These are
#       written as part of the site generation pipeline for this project.
# !! MARKER !!

#html_theme = "sphinx_rtd_theme"
html_theme = "furo"
#html_theme = "sphinxawesome_theme"
#html_logo = "images/logo_small.png"
#html_theme_options = {'logo_only': True, "sidebar_hide_name": True,}
#html_theme = "furo"
html_static_path = ['_static']

#html_context = {'css_files': ['_static/custom.css']}
#html_css_files = ["custom.css"]

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

#def setup(app):
#    app.add_css_file('custom.css')

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    'sphinx.ext.autodoc',
#    'sphinx.ext.mathjax',
#    'sphinx.ext.viewcode',
#    'sphinx.ext.autosectionlabel',
#]

date = datetime.now()
copyright = "{year}, Philipp Resl, Claudio G. Ametrano and Christoph Hahn".format(year=date.timetuple()[0])

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'


