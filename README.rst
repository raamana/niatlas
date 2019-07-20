=======
niatlas
=======


.. image:: https://img.shields.io/pypi/v/niatlas.svg
        :target: https://pypi.python.org/pypi/niatlas

.. image:: https://img.shields.io/travis/raamana/niatlas.svg
        :target: https://travis-ci.org/raamana/niatlas


Atlas classes and methods for neuroimaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


This is a placeholder repository for potential development of ``nibabel``-like python package that is intended to make the management of Atlases for neuroimaging seamless, in all their diverse use-cases. We will collect and link to various relevant resources to facilitate this discussion and project development.


As I currently envision it, a decent ``niatlas`` package would offer the following features (consider it a **wishlist**):

 - easy access (including I/O) to all the popular atlases just by their name, both volumetric- and surface-based.
 - a well-defined data structure that provides, not only the parcellations, but also all the relevant ``meta-data``, such as
    - the source of atlas, in terms of modalities and tha processes that generated it
    - methods defining the parcellation,
    - number, names and centroids of ROIs, along with resolution and dimensions
    - whether it is intended to be used as a volumetric or surface atlas,
    - **domain tags** that identify which **age-group** this atlas would be ideal for, along with other info related to target population
    - etc
 - several convenience methods to perform the common operations on atlases including but not limited to
    - computing ROI-based statistics
    - masking operations
 - Methods to obtain different variations of the same atlas e.g.
    - resampling the parcellation to a different resolution, or to different dimensions (that respects the internal parcellations)
    - scale control in terms of number or size of ROIs i.e. methods for subdividing or clustering existing ROIs
    - conversion to different spaces, such as between volumetric and surface-oriented spaces
    - conversion between atlas- and subject-spaces
 - visualization routines for all the common analyses needs
 - easy integration and high interoperability with popular tools and ecosystems

Some prior discussion on potential data structures for Atlas object and uniform access to parcellations at nilearn `here <https://github.com/nilearn/nilearn/issues/1489>`_

Prior Art (software)
~~~~~~~~~~~~~~~~~~~~~~~

 - nilearn ``fetch_{atlas}`` `utilities <https://nilearn.github.io/modules/reference.html#module-nilearn.datasets>`_
 - ` nilabels <https://github.com/nipy/nilabels>`_ :  tools to automate simple manipulations and measurements of medical image segmentations
 - `AtlasReader` to generate coordinate tables and region labels from statistical MRI images : https://github.com/miykael/atlasreader
 - pysurfer visualization tool: https://pysurfer.github.io/auto_examples/index.html
 - python package for subparcellation of fsaverage etc: https://github.com/miykael/parcellation_fragmenter
 - shell scripts to move from atlas space to subject space https://github.com/faskowit/multiAtlasTT


Resources - atlas collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - Different atlases in MNI space: http://www.lead-dbs.org/helpsupport/knowledge-base/atlasesresources/cortical-atlas-parcellations-mni-space/
 - Different atlases from Thomas Yeo's lab 
    - set 1: https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation
    - set 2: https://github.com/ThomasYeoLab/CBIG/tree/master/data
 - `BALSA (Brain Analysis Library of Spatial maps and Atlases) <https://balsa.wustl.edu/>`_ is a database for hosting and sharing neuroimaging and neuroanatomical datasets for human and primate species.
 - Brain signature patterns, atlases of regions, and meta-analysis masks from Tor Wager's lab: https://github.com/canlab/Neuroimaging_Pattern_Masks
