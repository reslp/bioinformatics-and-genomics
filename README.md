# Genomic Methods

![RTD badge](https://readthedocs.org/projects/bioinformatics-and-genomics/badge/?version=latest)

This repository contains information about the Module D1/G1 - Bioinformatics and Genomics of the Biology Master curriculum at the University of Graz.

A rendered version can be found here: https://bioinformatics-and-genomics.readthedocs.io/en/latest/


### Contents

This module is part of the specialization in "Evolutionary Ecology" and the specialization in "Digital Biology."\
The focus of this module is on essential skills for producing as well as evaluating, organizing, and analyzing large biological datasets, with special attention, but not limited to, molecular biology data. Among others, the following topics will be covered:\
- Current technologies, methods, and databases in the field of DNA/RNA sequencing
- Fundamental algorithms in computer-assisted molecular biology
- Modern computer-assisted tools, applications, and computing infrastructure for large-scale analyses of DNA/RNA and other data
- Reproducibility in modern computer-assisted biology and data science in general


## Run the documentation locally


Clone the full repository:

```
git clone --recursive https://github.com/reslp/bioinformatics-and-genomics.git
```

The course website is built from the `materials/` directory with Sphinx hence `--recursive`.

If you have [`uv`](https://docs.astral.sh/uv/) installed, build the HTML site with:

```bash
uv run --with-requirements materials/requirements.txt sphinx-build -b html materials materials/_build/html
```

Then serve the rendered site locally:

```bash
cd materials/_build/html
python3 -m http.server 8051 --bind 127.0.0.1
```

Open the local preview at:

```text
http://127.0.0.1:8051/
```

To rebuild after changes, run the `uv run ... sphinx-build ...` command again from the repository root.

## Update content of individual lectures

If you want to update your course content. First make changes to the remote repositories included here.

Then run the following commands to update your part to the latest commit:

(In this case for the `linux-intro` module)

```
git submodule update --remote materials/linux-intro
git status
git add materials/linux-intro
git commit -m "Update linux-intro exercise" 
```

