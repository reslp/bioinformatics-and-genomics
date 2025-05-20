===========================
Bioinformatics and Genomics
===========================

This repository contains information about the Module D1/G1 - Bioinformatics and Genomics of the Biology Master curriculum at the University of Graz.

--------
Contents
--------

This module is part of the specialization in "Evolutionary Ecology" and the specialization in "Digital Biology."  
The focus of this module is on essential skills for producing as well as evaluating, organizing, and analyzing large biological datasets, with special attention, but not limited to, molecular biology data. Among others, the following topics will be covered:  

* Current technologies, methods, and databases in the field of DNA/RNA sequencing  
* Fundamental algorithms in computer-assisted molecular biology  
* Modern computer-assisted tools, applications, and computing infrastructure for large-scale analyses of DNA/RNA and other data  
* Reproducibility in modern computer-assisted biology and data science in general  

The module is devided into 3 individual lectures:  

1. Genomic Methods in Evolutionary Biology and Ecology  
2. Databases in Ecology and Comparative Genomics  
3. Fundamentals of Reproducable Data Analysis  

-----------------------------------------------
Expected Learning Outcomes and Competencies
-----------------------------------------------

Upon completion of the module, students will be able to:  

- Design evolutionary biological and ecological studies based on DNA/RNA data  
- Select appropriate sequencing technologies and applications for studies  
- Evaluate high-throughput data (NGS) of various types (QC)  
- Analyze high-throughput data (NGS) both qualitatively and quantitatively  
- Explain and apply fundamental algorithms of computer-assisted molecular biology  
- Interact with important public biological databases  
- Use High Performance Computing infrastructure (HPC)  
- Process large (biological) datasets efficiently and reproducibly  
- Organize large (biological) datasets and utilize workflow management systems  
- Use and develop software containers and computer-assisted automated workflows  

---------------------------------------------
Teaching and Learning Activities, Methods
---------------------------------------------

Lectures by teachers and students, a mix of interactive didactic teaching and guided practical work and exercises, independent work in small groups, writing of written assignments\

========
Syllabus
========
-------------------------------------------------------
Genomic Methods in Ecology and Evolutionary Biology
-------------------------------------------------------

+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| Day | Date         | Topics                                                      | Material                                 |
+=====+==============+=============================================================+==========================================+
| 1   | 2 June 2025  | Introduction to Linux, working on the command line,         | `linux intro <linux-intro/README.html>`_ |
|     |              | working on remote computers.                                |                                          |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 2   | 3 June 2025  | Working with HTS data, evaluation of data quality,          | xxx                                      |
|     |              | data filtering                                              |                                          |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 3   | 4 June 2025  | Genome assembly, evaluation, Metagenome cleaning            | xxx                                      |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 4   | 5 June 2025  | Transcriptome assembly, differential gene expression        | xxx                                      |
|     |              | analysis                                                    |                                          |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 5   | 24 June 2025 | Genome annotation, Orthology, Phylogenomics                 | xxx                                      |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 6   | 25 June 2025 | Working on individual project                               | xxx                                      |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 7   | 26 June 2025 | Working on individual project                               | xxx                                      |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+
| 8   | 27 June 2025 | Working on individual project                               | xxx                                      |
+-----+--------------+-------------------------------------------------------------+------------------------------------------+

---------------------------------------------
Databases in Ecology and Comparative Genomics
---------------------------------------------

+-----+--------------+----------------------------------------------------------------------------------+----------+
| Day | Date         | Topics                                                                           | Material |
+=====+==============+==================================================================================+==========+
| 1   | 16 June 2025 | Sequence Databases (e.g. NCBI-Genbank, OrthoDB)                                  | xxx      |
|     |              | and similarity search (e.g. BLAST, HMMER)                                        |          |
+-----+--------------+----------------------------------------------------------------------------------+----------+
| 2   | 17 June 2025 | Databases in Metabarcoding (e.g. Silva, BOLD, UNITE):                            | xxx      |
|     |              | taxonomic assignment and ecological metadata (e.g. Gbif, WorldClim,              |          |
|     |              | Copernicus)                                                                      |          |
+-----+--------------+----------------------------------------------------------------------------------+----------+
| 3   | 18 June 2025 | Databases for functional annotation (e.g. Pfam-InterPro, GO, KEGG)               | xxx      |
+-----+--------------+----------------------------------------------------------------------------------+----------+
| 4   | 23 June 2025 | Working on indiviual project                                                     | xxx      |
+-----+--------------+----------------------------------------------------------------------------------+----------+



---------------------------------------------
Fundamentals of Reproducible Data Analysis
---------------------------------------------

+-----+--------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Day | Date         | Topics                                                                       | Material                                                                                             |
+=====+==============+==============================================================================+======================================================================================================+
| 1   | 06 June 2025 | Advanced command line, random numbers, Reproducible software installation,   | `about <reproducibility-workshop/introduction/about.html>`_                                          |
|     |              | Data organication, Git                                                       |                                                                                                      |
|     |              |                                                                              | `working environment <reproducibility-workshop/introduction/setup.html>`_                            |
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 1 <reproducibility-workshop/day-1/exercise-1-shell-intro.html>`_                           |
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 2 <reproducibility-workshop/day-1/exercise-2-reproducible-software-installation.html>`_    |  
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 3 <reproducibility-workshop/day-1/exercise-3-data-organization.html>`_                     |
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 4 <reproducibility-workshop/day-1/exercise-4-git.html>`_                                   |
+-----+--------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| 2   | 11 June 2025 | Virtual environments, Container basics, advanced topics and pitfalls         |                                                                                                      |
|     |              |                                                                              | `exercise 1 <reproducibility-workshop/day-2/exercise-1-conda.html>`_                                 |
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 2 <reproducibility-workshop/day-2/exercise-2-docker.html>`_                                |  
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 3 <reproducibility-workshop/day-2/exercise-3-advanced-docker.html>`_                       |
|     |              |                                                                              |                                                                                                      |
|     |              |                                                                              | `exercise 4 <reproducibility-workshop/day-3/exercise-4-docker-pitfalls.html>`_                       |
+-----+--------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| 3   | 12 June 2025 | Workflow management systems: GNU Make, Snakemake, Nextflow                   | `exercise 1 <reproducibility-workshop/day-3/exercise-1-workflows.html>`_                             |
+-----+--------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| 4   | 13 June 2025 | Working on individual project                                                | `exercise 1 <reproducibility-workshop/day-3/exercise-1-phylogenomics.html>`_                         |
+-----+--------------+------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+


.. toctree::
   :caption: Linux Intro
   :maxdepth: 2
   :hidden:
   :glob:

   linux-intro/README.md

.. toctree::
   :caption: HPC intro
   :name: hpcdemo
   :maxdepth: 1
   :hidden:
   :glob:

   AMEB_HPC_demo/README

.. toctree::
   :caption: Genome Assembly
   :name: assembly
   :maxdepth: 1
   :hidden:
   :glob:

   short-read-processing-and-assembly/README

.. toctree::
   :caption: Post Assembly
   :name: postassembly
   :maxdepth: 1
   :hidden:
   :glob:

   post-assembly-intro/README

.. toctree::
   :caption: Phylogenomics
   :maxdepth: 1
   :hidden:
   :glob:

   phylogenomics_intro_vertebrata/README.md


.. toctree::
   :caption: Reproducibility Fundamentals
   :maxdepth: 1
   :hidden:
   :glob:

   reproducibility-workshop/introduction/about.rst
   reproducibility-workshop/introduction/setup.rst
   reproducibility-workshop/day-1/exercise-1-shell-intro.rst
   reproducibility-workshop/day-1/exercise-2-reproducible-software-installation.rst
   reproducibility-workshop/day-1/exercise-3-data-organization.rst
   reproducibility-workshop/day-1/exercise-4-git.rst

   reproducibility-workshop/day-2/exercise-1-conda.rst
   reproducibility-workshop/day-2/exercise-2-docker-intro.rst
   reproducibility-workshop/day-2/exercise-3-advanced-docker.rst
   reproducibility-workshop/day-2/exercise-4-docker-pitfalls.rst

   reproducibility-workshop/day-3/exercise-1-workflows.rst
   reproducibility-workshop/day-3/exercise-2-phylogenomics.rst
