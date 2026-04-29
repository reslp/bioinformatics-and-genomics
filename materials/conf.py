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
html_css_files = ["css/course-sidebar.css"]

#html_context = {'css_files': ['_static/custom.css']}
#html_css_files = ["custom.css"]

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/course-navigation.html",
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




# Custom course sidebar. This keeps the sidebar/menu controlled by the main
# repository while the links open the original submodule documents directly.
# Each href is relative to the built HTML root.
course_menu = [
    {
        "id": "linux-intro",
        "caption": "Linux Intro",
        "entries": [{
            "title": "Introduction to Linux and working on the command line",
            "href": "linux-intro/README.html",
            "doc": "linux-intro/README",
            "children": [
                {"title": "0 Learning goals", "href": "linux-intro/README.html#learning-goals"},
                {"title": "1 First steps", "href": "linux-intro/README.html#first-steps"},
                {"title": "2 Basic commands", "href": "linux-intro/README.html#basic-commands"},
                {"title": "3 Additional reading", "href": "linux-intro/README.html#additional-reading"},
            ],
        }],
    },
    {
        "id": "hpc-intro",
        "caption": "HPC intro",
        "entries": [{
            "title": "HPC Intro",
            "href": "AMEB_HPC_demo/README.html",
            "doc": "AMEB_HPC_demo/README",
            "children": [
                {"title": "Connect to the cluster", "href": "AMEB_HPC_demo/README.html#connect-to-the-cluster"},
                {"title": "Meet the cluster", "href": "AMEB_HPC_demo/README.html#meet-the-cluster"},
                {"title": "Submit jobs", "href": "AMEB_HPC_demo/README.html#create-your-first-submission-script"},
                {"title": "Conda and Snakemake", "href": "AMEB_HPC_demo/README.html#set-up-conda-and-install-snakemake"},
            ],
        }],
    },
    {
        "id": "genome-assembly",
        "caption": "Genome Assembly",
        "entries": [{
            "title": "Genome Assembly",
            "href": "short-read-processing-and-assembly/README.html",
            "doc": "short-read-processing-and-assembly/README",
            "children": [
                {"title": "Preparation", "href": "short-read-processing-and-assembly/README.html#introduction-preparation"},
                {"title": "Illumina data basics", "href": "short-read-processing-and-assembly/README.html#illumina-data-basics"},
                {"title": "Read trimming", "href": "short-read-processing-and-assembly/README.html#read-trimming"},
                {"title": "Read merging", "href": "short-read-processing-and-assembly/README.html#read-merging"},
                {"title": "K-mer counting", "href": "short-read-processing-and-assembly/README.html#kmer-counting"},
                {"title": "De novo assembly", "href": "short-read-processing-and-assembly/README.html#de-novo-genome-assembly"},
            ],
        }],
    },
    {
        "id": "post-assembly",
        "caption": "Post Assembly",
        "entries": [{
            "title": "Post Assembly",
            "href": "post-assembly-intro/README.html",
            "doc": "post-assembly-intro/README",
            "children": [
                {"title": "Introduction", "href": "post-assembly-intro/README.html#introduction"},
                {"title": "Post-assembly analyses", "href": "post-assembly-intro/README.html#post-assembly"},
            ],
        }],
    },
    {
        "id": "phylogenomics",
        "caption": "Phylogenomics",
        "entries": [{
            "title": "Phylogenomics",
            "href": "phylogenomics_intro_vertebrata/README.html",
            "doc": "phylogenomics_intro_vertebrata/README",
            "children": [
                {"title": "Introduction", "href": "phylogenomics_intro_vertebrata/README.html#introduction"},
                {"title": "Practical start", "href": "phylogenomics_intro_vertebrata/README.html#let-s-begin"},
            ],
        }],
    },
    {
        "id": "sequence-databases",
        "caption": "Sequence databases",
        "entries": [{
            "title": "Sequence Databases",
            "href": "sequence_databases_similarity_search/README.html",
            "doc": "sequence_databases_similarity_search/README",
            "children": [
                {"title": "Setup", "href": "sequence_databases_similarity_search/README.html#before-we-start"},
                {"title": "Nucleotide sequence databases", "href": "sequence_databases_similarity_search/README.html#1-nucleotide-sequence-databases"},
                {"title": "Sequence alignment and BLAST", "href": "sequence_databases_similarity_search/README.html#2-sequence-alignment"},
                {"title": "BLAST on the command line", "href": "sequence_databases_similarity_search/README.html#2b-use-of-blast-command-line-interface-cli"},
                {"title": "Other alignment tools", "href": "sequence_databases_similarity_search/README.html#3-the-right-method-for-every-occasion-other-commonly-used-alignment-mapping-tools"},
                {"title": "Final task", "href": "sequence_databases_similarity_search/README.html#final-task"},
            ],
        }],
    },
    {
        "id": "metabarcoding-databases",
        "caption": "Metabarcoding databases",
        "entries": [{
            "title": "Metabarcoding Databases",
            "href": "metab_db/README.html",
            "doc": "metab_db/README",
            "children": [
                {"title": "Setup", "href": "metab_db/README.html#before-we-start"},
                {"title": "Introduction", "href": "metab_db/README.html#introduction"},
                {"title": "Reference databases", "href": "metab_db/README.html#nucleotide-reference-databases-for-metabarcoding-and-diversity-assessment-an-example-of-secondary-database"},
                {"title": "Case study", "href": "metab_db/README.html#case-study-welcome-to-the-trieste-coast-a-toy-16s-dataset"},
                {"title": "QIIME environment", "href": "metab_db/README.html#the-qiime-environment"},
            ],
        }],
    },
    {
        "id": "functional-annotation-databases",
        "caption": "Functional annotation databases",
        "entries": [{
            "title": "Functional Annotation Databases",
            "href": "functional_annotation_db/README.html",
            "doc": "functional_annotation_db/README",
            "children": [
                {"title": "Setup", "href": "functional_annotation_db/README.html#before-we-start"},
                {"title": "Introduction", "href": "functional_annotation_db/README.html#introduction"},
                {"title": "Genome annotation concepts", "href": "functional_annotation_db/README.html#what-do-we-mean-by-genome-annotation"},
                {"title": "Databases and tools", "href": "functional_annotation_db/README.html#database-and-tools-for-functional-annotation"},
                {"title": "Pathway analysis and Gene Ontology", "href": "functional_annotation_db/README.html#2-how-to-summarize-the-overwhelming-amount-of-information-of-functional-annotation-pathway-analysis-and-gene-ontology-go"},
                {"title": "Annotation case study", "href": "functional_annotation_db/README.html#3-annotation-a-case-study-using-cyanobacteria"},
                {"title": "Enrichment analysis", "href": "functional_annotation_db/README.html#4-enrichment-analysis-application-transcriptomics"},
            ],
        }],
    },
    {
        "id": "reproducibility-fundamentals",
        "caption": "Reproducibility Fundamentals",
        "entries": [{
            "title": "Reproducibility Fundamentals",
            "href": "reproducibility-workshop/introduction/about.html",
            "doc": "reproducibility-workshop",
            "children": [
                {"title": "Overview", "href": "reproducibility-workshop/introduction/about.html"},
                {"title": "Working environment", "href": "reproducibility-workshop/introduction/setup.html"},
                {"title": "Day 1: command line, software, data, Git", "href": "reproducibility-workshop/day-1/exercise-1-shell-intro.html"},
                {"title": "Day 2: environments and containers", "href": "reproducibility-workshop/day-2/exercise-1-conda.html"},
                {"title": "Day 3: workflows and pipelines", "href": "reproducibility-workshop/day-3/exercise-1-workflows.html"},
            ],
        }],
    },
]

html_context = globals().get("html_context", {})
html_context["course_menu"] = course_menu
