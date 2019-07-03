# PepVis

# PepVis-Peptide Virtual Screening Pipeline
PepVis tool is a python based GUI pipeline which can be used to model and prepare large-scale peptide structure from the sequence and also to perform large-scale peptide virtual screening. PepVis integrates ModPep and Gromacs for modelling and structure optimization of the peptides, while it integrates AutoDock Vina,ZDOCK, AutoDock CrankPep(ADCP) for performing peptide virtual screening. The protein-peptide complexes can be rescored using ZRANK2 and the flexible refinement of the large protein-peptide complexes can also be performed using FlexPepDock. The parallel job execution have been implemented using GNU parallel and the user can provide inputs using GUI which will produce the bash script based on the customized input provided by the user and can be run in terminal. 


* **Software Required to run PepVis:**
    + GNU Parallel (https://www.gnu.org/software/parallel/)
    + Autodock Vina (http://vina.scripps.edu/)
    + MGL Tools 1.5.6 or 1.5.7 (http://mgltools.scripps.edu/)
    + ZDock-3.0.2 (http://zdock.umassmed.edu/software/)
    + ZRANK2 (http://zdock.umassmed.edu/software/)
    + AutoDock CrankPep (https://ccsb.scripps.edu/adcp/)
    + ROSETTA (https://www.rosettacommons.org/software/license-and-download) If user wants to perform Flexible Refinement of the protein-peptide complex
    + AutoDock CrankPep (https://ccsb.scripps.edu/adcp/)

* **PepVis Installation:**
    + Just unzip and run the bash scripts provided directly to run the program. 

    There is no installation required. Provide the directory path of the tools installed as instructued in the manual for one time configuration. 

* **Peptide structure modelling**

* **Peptide Virtual Screening process:**
    + Multiple protein Virtual screening using Autodock VINA
    + Multiple protein Virtual screening using ZDock
    + Multiple protein Virtual screening using AutoDock CrankPep
    + Flexible refinement using FlexPepDock

This tool is distributed under the GNU General Public License (GPL). This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License. This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

**Usage**

Start the GUI by running the command 

python PepVis.py

**Version**

v1.0

**Authors**

Samdani.A & Umashankar.V

**For queries please contact:**
vumashankar@gmail.com

samdani1593@gmail.com




