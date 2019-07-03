from Tkinter import *
import tkFileDialog
import tkMessageBox
import subprocess
import os
import ConfigParser
import multiprocessing
root = Tk()
root.title("PepVis")
MODPEP=""
PSIPRED=""
MGLROOT=""
GROMACS_PREFIX=""
ZDOCK=""
ZRANK=""
HBPLUS=""
FLEXPEPDOCK=""
ADFRROOT=""
RANKALL="YES" # For ADCP: YES-to consider all top 10 ranking solutions, NO- to consider top 1 solution alone
#~~ 
PEPTIDE=""
INPUTPEP=""
WORKING=""
RECEPTOR=""
joobs=""
#~~
NUMMOD=""
CWD=os.getcwd()
def run_pepmod():
	run_pep=Toplevel(root)
	run_pep.title("Peptide Modelling")
	global CWD
#	if CONFIG_check.get() == 0:
#		if MODPEP:
#			asd_config.set("softwares","MODPEP",MODPEP)
#		if PSIPRED:
#			asd_config.set("softwares","PSIPRED",PSIPRED)
#		if MGLROOT:
#			asd_config.set("softwares","MGLROOT",MGLROOT)
#		if GROMACS_PREFIX:
#			asd_config.set("softwares","GROMACS_PREFIX",GROMACS_PREFIX)
#		if ZDOCK:
#			asd_config.set("softwares","ZDOCK",ZDOCK)
#		if ZRANK:
#			asd_config.set("softwares","ZRANK",ZRANK)
#		if HBPLUS:
#			asd_config.set("softwares","HBPLUS",HBPLUS)
#		if FLEXPEPDOCK:
#			asd_config.set("softwares","FLEXPEPDOCK",FLEXPEPDOCK)
#		if ADFRROOT:
#			asd_config.set("softwares","ADFRROOT",ADFRROOT)
#		config_file=open('config.ini','w')
#		asd_config.write(config_file)
#		config_file.close()
	#~~~~~
	#~~~~~~ Peptide model start
	PEPMODEL_check=IntVar()
	PEPSS_check=IntVar()
	Label(run_pep,bg="white",text="Do you want to model the peptides?",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=0,column=0,sticky=E+W+N+S)
	Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=PEPMODEL_check,font=("Times",15,"bold"),relief=SOLID,width=10,height=2).grid(row=0,column=1,sticky=E+W+N+S)
	def pepmodel_check(*args):
		if PEPMODEL_check.get() == 1:
			Label(run_pep,bg="white",text="Provide the peptide sequence file",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=1,column=0,sticky=E+W+N+S)
			def get_peptide_dir():
				filetemp=tkFileDialog.askopenfilename(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/peptide",title="Enter the peptide sequence file",parent=run_pep)
				if filetemp:
					if ' ' in filetemp:
						tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=run_pep)
						return
					else:
						if os.path.exists(filetemp):
							global PEPTIDE
							global INPUTPEP
							PEPTIDE=os.path.split(filetemp)[0]
							INPUTPEP=os.path.split(filetemp)[1]
						else:
							tkMessageBox.showinfo("Warning!","File not found in the directory path!",parent=run_pep)
							return
				else:	
					tkMessageBox.showinfo("Warning!","Directory not specified!",parent=run_pep)
					return
			Button(run_pep,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=2,command=get_peptide_dir).grid(row=1,column=1,sticky=E+W+N+S)
			Label(run_pep,bg="white",text="Predict peptide secondary structure \nusing PSI-PRED?",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=2,column=0,sticky=E+W+N+S)
			Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=PEPSS_check,font=("Times",15,"bold"),relief=SOLID,width=10,height=2).grid(row=2,column=1,sticky=E+W+N+S)
			NUM_MODEL=StringVar()
			Label(run_pep,bg="white",text="Enter the number of models to \n generate per peptide",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=3,column=0,sticky=E+W+N+S)
			Entry(run_pep,bd=5,textvariable=NUM_MODEL,font=("Times",15,'bold'),justify=CENTER).grid(row=3,column=1,sticky=W+E+N+S)
			def num_model(*args):
				if len(NUM_MODEL.get()) > 0:
					for f in NUM_MODEL.get():
						if f not in '0123456789':
							tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=run_pep)
							return
					global NUMMOD
					NUMMOD=int(NUM_MODEL.get())
				else:
					tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=run_pep)
					return
			NUM_MODEL.trace('w',num_model)
		if PEPMODEL_check.get() == 0:
			Label(run_pep,bg="white",text="Provide the peptide sequence file",font=("Times",15,"bold"),state=DISABLED,width=35,height=2).grid(row=1,column=0,sticky=E+W+N+S)
			Button(run_pep,text="Open",bg="gold",font=("Times",15,"bold","underline"),state=DISABLED,relief=RAISED,borderwidth=3,width=10,height=2).grid(row=1,column=1,sticky=E+W+N+S)
			Label(run_pep,bg="white",text="Predict peptide secondary structure \nusing PSI-PRED?",font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=35,height=2).grid(row=2,column=0,sticky=E+W+N+S)
			Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=PEPSS_check,font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=10,height=2).grid(row=2,column=1,sticky=E+W+N+S)
			Label(run_pep,bg="white",text="Enter the number of models to \n generate per peptide",font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=35,height=2).grid(row=3,column=0,sticky=E+W+N+S)
			Entry(run_pep,bd=5,font=("Times",15,'bold'),state=DISABLED,justify=CENTER).grid(row=3,column=1,sticky=W+E+N+S)
	PEPMODEL_check.trace('w',pepmodel_check)
	#~~~~~~ Peptide model end	
	#~~~~~ Peptide minim start
	MINIM_check=IntVar()
	Label(run_pep,bg="white",text="Do you want to minimize \nthe peptides structures?",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=4,column=0,sticky=E+W+N+S)
	Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=MINIM_check,font=("Times",15,"bold"),relief=SOLID,width=10,height=2).grid(row=4,column=1,sticky=E+W+N+S)
	def minim_check(*args):
		if MINIM_check.get() == 1:
			if PEPMODEL_check.get() == 0:
				Label(run_pep,bg="white",text="Provide the peptide structure directory",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=5,column=0,sticky=E+W+N+S)
				def get_peptide_str_dir():
					filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/peptide",title="Enter the peptide sequence file",parent=run_pep)
					if filetemp:
						if ' ' in filetemp:
							tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=run_pep)
							return
						else:
							global PEPTIDE
							PEPTIDE=filetemp
					else:	
						tkMessageBox.showinfo("Warning!","Directory not specified!",parent=run_pep)
						return
				Button(run_pep,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=2,command=get_peptide_str_dir).grid(row=5,column=1,sticky=E+W+N+S)
			elif PEPMODEL_check.get() == 1:
				Label(run_pep,bg="white",text="Provide the peptide structure directory",font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=35,height=2).grid(row=5,column=0,sticky=E+W+N+S)
				Button(run_pep,text="Open",bg="gold",font=("Times",15,"bold","underline"),state=DISABLED,relief=RAISED,borderwidth=3,width=10,height=2).grid(row=5,column=1,sticky=E+W+N+S)
	MINIM_check.trace('w',minim_check)
	#~~~~ Peptide minim end
	#~~~~ PDBQT start
	PDBQT_check=IntVar()
	TORSION_check=IntVar()
	Label(run_pep,bg="white",text="Do you want the peptides \n structures in PDBQT format?",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=6,column=0,sticky=E+W+N+S)
	Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=PDBQT_check,font=("Times",15,"bold"),relief=SOLID,width=10,height=2).grid(row=6,column=1,sticky=E+W+N+S)
	def pdbqt_check(*args):
		if PDBQT_check.get() == 1:
			Label(run_pep,bg="white",text="Do you want to the inactivate \npeptide torsions?",font=("Times",15,"bold"),relief=SOLID,width=35,height=2).grid(row=7,column=0,sticky=E+W+N+S)
			Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=TORSION_check,font=("Times",15,"bold"),relief=SOLID,width=10,height=2).grid(row=7,column=1,sticky=E+W+N+S)
		elif PDBQT_check.get() == 0:
			Label(run_pep,bg="white",text="Do you want to the inactivate \npeptide torsions?",font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=35,height=2).grid(row=7,column=0,sticky=E+W+N+S)
			Checkbutton(run_pep,bg="white",offvalue=0,onvalue=1,variable=TORSION_check,font=("Times",15,"bold"),state=DISABLED,relief=SOLID,width=10,height=2).grid(row=7,column=1,sticky=E+W+N+S)
	PDBQT_check.trace('w',pdbqt_check)
	#~~~~ PDBQT end
	Label(run_pep,bg="white",text="Enter the working directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=2).grid(row=8,column=0,sticky=E+W+N+S)
	def get_working_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/working",title="Enter the working directory",parent=run_pep)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=run_pep)
				return
			else:
				os.chdir(filetemp)
				zxc=os.listdir('.')
				if zxc:
					tkMessageBox.showinfo("Warning!","Working directory is not empty!",parent=run_pep)
					return
				else:
					global WORKING
					WORKING=filetemp
					os.chdir(CWD)
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=run_pep)
			return
	Button(run_pep,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=2,command=get_working_dir).grid(row=8,column=1,sticky=E+W+N+S)
	#~~~~~~~~~~~~~~ Number of CPU calculation start
	Ncpu=multiprocessing.cpu_count()
	Label(run_pep,bg="white",text=str(Ncpu)+" number of CPU processors \n detected in your system",relief=SOLID,font=("Times",15,'bold'),width=30,height=3,justify=CENTER).grid(row=9,column=0,columnspan=2,sticky=E+W+N+S)
	Label(run_pep,bg="white",text="Enter the number of CPU \n for running jobs in parallel:",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=10,column=0,sticky=W+E+N+S)
	global Numcpu
	Numcpu=StringVar()
	Numcpu.set(Ncpu)
	joobs=int(Numcpu.get())
	if joobs:
		Label(run_pep,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=11,column=0,columnspan=2,sticky=W+E+N+S)
	Entry(run_pep,bd=5,textvariable=Numcpu,font=("Times",15,'bold'),justify=CENTER).grid(row=10,column=1,sticky=W+E+N+S)
	def checkback(*args):
		for f in Numcpu.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=run_pep)
				return
		global joobs
		joobs=0
		if len(Numcpu.get()) > 0:
			if int(Numcpu.get()) > Ncpu or int(Numcpu.get()) == 0 :
				tkMessageBox.showinfo("Warning","Please provide the values less than "+str(Ncpu)+"!",parent=run_pep)
				return
			else:
				Label(run_pep,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=11,column=0,columnspan=2,sticky=W+E+N+S)
				joobs=int(Numcpu.get())
		else:
			Label(run_pep,bg="white",text= "0 Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=11,column=0,columnspan=2,sticky=W+E+N+S)
	Numcpu.trace('w',checkback)
	#~~~~~~~~~~ Number of CPU calculation end
	def print_bash_script():
	#~~~ CHECK for installation and input start
		if PARALLEL_check.get() == 0:
			tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=run_pep)
			return
		if PDBQT_check.get() == 1:
			if not MGLROOT:
				tkMessageBox.showinfo("Warning!","MGLROOT not found!",parent=run_pep)
				return
		if not MODPEP:
			tkMessageBox.showinfo("Warning!","Modpep not found!",parent=run_pep)
			return
		if PEPMODEL_check.get() == 1:
			if not NUMMOD:
				tkMessageBox.showinfo("Warning!","Number of peptides model not specified!",parent=run_pep)
				return
		if PEPSS_check.get() == 1:
			if not PSIPRED:
				tkMessageBox.showinfo("Warning!","PSIPRED not found!",parent=run_pep)
				return
		if MINIM_check.get() == 1:
			if not GROMACS_PREFIX:
				tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=run_pep)
				return
		if not joobs:
			tkMessageBox.showinfo("Warning!","Number of jobs to run in parallel not specified!",parent=run_pep)
			return
		if not PEPTIDE:
			tkMessageBox.showinfo("Warning!","PEPTIDE directory not specified!",parent=run_pep)
			return
		if not WORKING:
			tkMessageBox.showinfo("Warning!","WORKING directory not specified!",parent=run_pep)
			return
	#~~~ CHECK for installation and input end
		BASHSCRIPT='''
#!/bin/bash
PEPTIDE="%s"
WORKING="%s"
joobs=%d''' %(PEPTIDE,WORKING,joobs)
		if PEPMODEL_check.get() == 1:
			BASHSCRIPT+='''\nMODPEP="%s"\nNUMMOD=%d\nINPUTPEP="%s"\n''' %(MODPEP,NUMMOD,INPUTPEP)
		if PEPSS_check.get() == 1:
			BASHSCRIPT+='''\nPSIPRED="%s"\n''' %(PSIPRED)
		if MINIM_check.get() == 1:
			BASHSCRIPT+='''\nGROMACS_PREFIX="%s"\n''' %(GROMACS_PREFIX)
		if PDBQT_check.get() == 1:
			BASHSCRIPT+='''\nMGLROOT="%s"\n''' %(MGLROOT)
		BASHSCRIPT+='''\n\n
echo -e "================================================================================"
echo -e "Peptide directory: "$PEPTIDE""
echo -e "Working directory: "$WORKING""
echo -e "Number of parallel jobs: "$joobs""'''
		if PEPMODEL_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Number of models per peptide: "$NUMMOD""'''
		if PEPSS_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Secondary structure Prediction using PSI-PRED: YES"'''
		if MINIM_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Minimization using Gromacs: YES"\necho -e "GROMACS Prefix: "$GROMACS_PREFIX""'''
		if PDBQT_check.get() == 1:
			BASHSCRIPT+='''\necho -e "PDBQT conversion: YES"'''
			if TORSION_check.get() == 1:
				BASHSCRIPT+='''\necho -e "Peptide Torsions: OFF"'''
			if TORSION_check.get() == 0:
				BASHSCRIPT+='''\necho -e "Peptide Torsions: ON"'''
		BASHSCRIPT+='''
echo -e "================================================================================"
echo -e "Please enter [1] to accept the input [2] to quit"
i=1
while [ "$i" -ge 0 ]
do
	read -ep ">>>" check
	if [ "$check" == 1 ]
	then
		:
		break
	elif [ "$check" == 2 ]
	then
		exit
	else
		echo "Wrong input! Enter again"
	fi
done
echo -e "\\n-------------------------------------------------------------------------------\\n---------------------------------Summary Report--------------------------------\\n-------------------------------------------------------------------------------\\n\\n\\nPeptide Input Directory="$PEPTIDE"\\nWorking directory="$WORKING"\\nNumber of parallel jobs: "$joobs"\\n" >>"$WORKING"/summary.txt'''
		if PEPMODEL_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Number of models per peptide: "$NUMMOD"" >>"$WORKING"/summary.txt'''
		if PEPSS_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Secondary structure Prediction using PSI-PRED: YES" >>"$WORKING"/summary.txt'''
		if MINIM_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Minimization using Gromacs: YES\\nGROMACS Prefix: "$GROMACS_PREFIX"" >>"$WORKING"/summary.txt'''
		if PDBQT_check.get() == 1:
			BASHSCRIPT+='''\n echo -e "PDBQT conversion: YES" >>"$WORKING"/summary.txt'''
			if TORSION_check.get() == 1:
				BASHSCRIPT+='''\n echo -e "Peptide Torsions: OFF" >>"$WORKING"/summary.txt'''
			if TORSION_check.get() == 0:
				BASHSCRIPT+='''\n echo -e "Peptide Torsions: ON" >>"$WORKING"/summary.txt'''
		BASHSCRIPT+='''\ntime=`date +"%c"`;echo -e "\\n\\nPeptide preparation start time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt''' 
		if PEPMODEL_check.get() == 1:
			if PEPSS_check.get() == 1:
				BASHSCRIPT+='''
clear
#~~~~~ Peptide Secondary Structure ~~~~~~~~~~~~~~
echo -e "##~~~ Running PSI-PRED prediction ~~~~##"
time=`date +"%c"`;echo -e "Secondary structure prediction start time : "$time"\\n" >>"$WORKING"/summary.txt
cd "$WORKING"; mkdir psipred modpep; cd psipred;
echo -n "ls -1 | parallel -j 1 rm {}" >del.bash
cat "$PEPTIDE"/"$INPUTPEP" | parallel -j "$joobs" --eta "mkdir {}; cd {};echo '>seq1' >{}.txt; echo {} >>{}.txt;"$PSIPRED"/runpsipred {}.txt &>>log_{}.txt;cp {}.ss2 ../; bash ../del.bash;cd ../;rmdir {};"
clear
time=`date +"%c"`;echo -e "Secondary structure prediction end time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
#~~~~~~~~~~~~ Peptide Modelling ~~~~~~~~~~~~~~~~~~~
echo -e "##~~~ Running Peptide structure modelling using MODPEP ~~~~##"
time=`date +"%c"`;echo -e "Peptide modelling using modpep start time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
cd "$WORKING"/modpep;mv ../psipred/del.bash .;mkdir temp; cd temp; cp "$MODPEP"/*.pdb .; rm 1kv6_C.pdb;cd ..;
cat "$PEPTIDE"/"$INPUTPEP" | parallel -j "$joobs" --eta "mkdir {}; cd {};echo '>seq1' >{}.txt; echo {} >>{}.txt;cp ../temp/*.pdb .;"$MODPEP"/modpep {}.txt {}.pdb -n "$NUMMOD" -L ./ -h ../../psipred/{}.ss2 &>>log_{}.txt;cp {}.pdb ../; bash ../del.bash;cd ../;rmdir {};"
cd temp; ls -1 | parallel "rm {}"; cd ../; rmdir temp; rm del.bash
'''
			elif PEPSS_check.get() == 0:
				BASHSCRIPT+='''
clear
echo -e "##~~~ Running Peptide structure modelling using MODPEP ~~~~##"
time=`date +"%c"`;echo -e "Peptide modelling using modpep start time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
cd "$WORKING"; mkdir modpep;
cd modpep;
echo -n "ls -1 | parallel -j 1 rm {}" >del.bash
mkdir temp; cd temp; cp "$MODPEP"/*.pdb .; rm 1kv6_C.pdb;cd ..;
cat "$PEPTIDE"/"$INPUTPEP" | parallel -j "$joobs" --eta "mkdir {}; cd {};echo '>seq1' >{}.txt; echo {} >>{}.txt;cp ../temp/*.pdb .;"$MODPEP"/modpep {}.txt {}.pdb -n "$NUMMOD" -L ./ &>>log_{}.txt;cp {}.pdb ../; bash ../del.bash;cd ../;rmdir {};"
cd temp; ls -1 | parallel -j 1 "rm {}"; cd ../; rmdir temp;rm del.bash
'''
			if NUMMOD > 1:
				BASHSCRIPT+='''
if [ "$NUMMOD" -gt 1 ]
then
	clear
	cd "$WORKING"/modpep;
	echo -e "##~~ Spliting the Modelled Peptides~~~##"
	echo -n "a=1;while read -r l;do echo \\"\$l\\" >>\$1_\$a.pdb; if [ \\"\$l\\" == 'ENDMDL' ]; then a=\`expr \$a + 1\`; fi; done <\$1.pdb; rm \$1.pdb" >split.bash
	ls -1U | grep 'pdb' | parallel -j "$joobs" --eta "bash split.bash {.}"
	rm split.bash
fi
'''
			BASHSCRIPT+='''
cd "$WORKING"/modpep
echo -n "
#-*- coding: utf-8 -*-
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
asd=open(sys.argv[1],'w')
for f in FILE1:
	if f[0:6].strip() == 'ATOM':
		stump=f[0:21]+'P'+f[22:]
		asd.write(stump)
asd.close()" >chainadd.py
	echo -e "##~~ Adding Chain name to the Peptides~~~##"
ls -1U | grep 'pdb' | parallel -j "$joobs" --eta "python chainadd.py {}"
rm chainadd.py
time=`date +"%c"`;echo -e "Peptide modelling using modpep end time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
'''
		if MINIM_check.get() == 1:
			BASHSCRIPT+='''
clear
#~~~~~ MINIMIZATION
cd "$WORKING"
mkdir minim; cd minim; mkdir error_minim
#~~~ MDP FILE: Vacuum ~~~~#
echo -n "
integrator	= steep
emtol	        = 1000.0
nsteps	        = 50000
nstenergy	= 1
emstep          = 0.01      
energygrps	= system
nstlist	        = 1
cutoff-scheme	= group
ns_type	        = grid
rlist           = 1.0
coulombtype     = cut-off
rcoulomb        = 1.0
rvdw            = 1.0
pbc             = no" >minim_vacuum.mdp

	#~~~ MDP FILE: Solvated ~~~~#
	echo -n "
define          = -DFLEXIBLE
integrator	= steep
emtol		= 1000.0
nsteps		= 50000
nstenergy	= 1	
emstep          = 0.01  
energygrps	= system
nstlist		= 1	
ns_type		= grid	
rlist		= 1.0	
coulombtype	= PME	
rcoulomb	= 1.0	
rvdw		= 1.0	
pbc		= xyz" >minim_solv.mdp

	#~~~~ Gromacs Minimization python script ~~~~~~#
echo -n "
#-*- coding: utf-8 -*-
#Check rmdir in local system.
import subprocess
import re
import sys
import os
from shutil import copyfile
from shutil import move

def ant (line,at):
	### Extract the details about atom type, reisdue name, chain ID, atom number, residue number and x,y,z co-ordinates.
	atom_hetatm=line[0:6].strip()
	if atom_hetatm in ['ATOM','HETATM']:	#splicing the second index value omited i.e [7:11] means will return value from 7-10
		if at=='an':
			atom_number=line[6:11].strip()
			return atom_number
			#print(atom_number)
		elif at=='aa':
			atom_name=line[12:16].strip()
			return atom_name
			#print(atom_name)
		elif at=='ra':
			res_name=line[17:20].strip() #check
			return res_name
			#print(res_name)
		elif at=='ca':
			chain=line[21].strip() #check
			return chain
			#print(chain)
		elif at=='rn':
			res_number=line[22:26].strip()
			return res_number
			#print(res_number)
		elif at=='x':
			x_co=line[30:38].strip()
			return x_co
			#print(x_co)
		elif at=='y':
			y_co=line[38:46].strip()
			return y_co
			#print(y_co)
		elif at=='z':
			z_co=line[46:54].strip()
			return z_co
			#print(z_co)
		elif at=='xyz':
			xyz_co=[line[30:38].strip()]
			xyz_co.append(line[38:46].strip())
			xyz_co.append(line[46:54].strip())
			return xyz_co
			#print (xyz_co)
		else:
			return 'ERROR'
			#print (Error)
	return 0
GMX_PREFIX='"$GROMACS_PREFIX"'	# gromacs prefix
GROMACS='True'
SIM_INPUT=sys.argv[1]
FORCEFIELD='gromos53a6'	# Forcefield
WATER='spc'		# water-model
WATERGRO='spc216.gro'	# water-model gro file
os.mkdir(SIM_INPUT.split('.')[0])
os.chdir(SIM_INPUT.split('.')[0])
move('../'+SIM_INPUT,SIM_INPUT)
if GROMACS == 'True':
	copyfile('../minim_vacuum.mdp','minim_vacuum.mdp')
	copyfile('../minim_solv.mdp','minim_solv.mdp')
	asd=subprocess.Popen([GMX_PREFIX,'pdb2gmx','-f',SIM_INPUT,'-p','protein.top','-o','protein.gro','-ignh','-ff',FORCEFIELD,'-water',WATER], stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at pdb2gmx!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at pdb2gmx!'+'\\n')
			errq.close()
			sys.exit(1)
		if re.match('Total charge', f):
			CHARGE=float(f.split()[2])
	if os.path.isfile('protein.gro') and os.path.getsize('protein.gro') > 0:
		pass
	else:
		#print('Fatal Error: Found at pdb2gmx!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at pdb2gmx!'+'\\n')
		errq.close()
		sys.exit(1)
	#print(CHARGE)
	#print('~~~~~PDB2GMX Finished!~~~~~~~~~~~~')
	pass
	##pdb2gmx##
	#~~~~~~vacuum minimization~~~~~~#
	asd=subprocess.Popen([GMX_PREFIX,'grompp', '-f', 'minim_vacuum.mdp', '-c', 'protein.gro','-p', 'protein.top', '-o', 'protein_vacuum.tpr'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			#print('Fatal Error: Found at grompp vacuum!')
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at grompp vacuum!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_vacuum.tpr') and os.path.getsize('protein_vacuum.tpr') > 0:
		pass
	else:
		#print('Fatal Error: Found at grompp vacuum!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at grompp vacuum!'+'\\n')
		errq.close()
		sys.exit(1)
	pass
	asd=subprocess.Popen([GMX_PREFIX,'mdrun', '-deffnm', 'protein_vacuum'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at mdrun vacuum!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at mdrun vacuum!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_vacuum.gro') and os.path.getsize('protein_vacuum.gro') > 0:
		pass
	else:
		#print('Fatal Error: Found at mdrun vacuum!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at mdrun vacuum!'+'\\n')
		errq.close()
		sys.exit(1)
	#print('~~~~~Minimization in vacuum Finished!~~~~~~~~~~~~')
	pass
	#~~~~~Editconf~~~~~~~~~~~
	asd=subprocess.Popen([GMX_PREFIX,'editconf','-f','protein_vacuum.gro','-o','protein_pbc.gro','-bt','cubic','-d','1.0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at editconf!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at editconf!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_pbc.gro') and os.path.getsize('protein_pbc.gro') > 0:
		pass
	else:
		#print('Fatal Error: Found at editconf!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at editconf!'+'\\n')
		errq.close()
		sys.exit(1)
	#print('~~~~~EDITCONF Finished!~~~~~~~~~~~~')
	pass
	asd=subprocess.Popen([GMX_PREFIX,'solvate', '-cp', 'protein_pbc.gro', '-cs', WATERGRO, '-p', 'protein.top', '-o', 'protein_water.gro'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at solvate!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at solvate!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_water.gro') and os.path.getsize('protein_water.gro') > 0:
		pass
	else:
		#print('Fatal Error: Found at solvate!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at solvate!'+'\\n')
		errq.close()
		sys.exit(1)
	#print('~~~~~GENBOX Finished!~~~~~~~~~~~~')
	pass
	if CHARGE < 0:
		IONS='POS'
		CHARGE=int(round(CHARGE*(-1)))
	elif CHARGE > 0:
		IONS='NEG'
		CHARGE=int(round(CHARGE*(1)))
	elif CHARGE == 0:
		IONS='NEU'
		os.rename('protein_water.gro','protein_ions.gro')
	if CHARGE != 0:
		asd=subprocess.Popen([GMX_PREFIX,'grompp', '-f', 'minim_solv.mdp', '-c', 'protein_water.gro', '-p', 'protein.top', '-o', 'protein_ions.tpr'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output,error=asd.communicate()
		asd.wait()
		#~~Check for fatal error~~~
		for f in error.split('\\n'):
			if (re.match('Fatal error',f) or re.match('Can not open file',f)):
				copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
				#print('Fatal Error: Found at grompp genion!')
				delete=os.listdir('.')
				for ff in delete:
					os.remove(ff)
				os.chdir('..')
				os.rmdir(SIM_INPUT.split('.')[0])
				errq=open('error_minim/error_log.txt','a')
				errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at grompp genion!'+'\\n')
				errq.close()
				sys.exit(1)
		if os.path.isfile('protein_ions.tpr') and os.path.getsize('protein_ions.tpr') > 0:
			pass
		else:
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at grompp genion!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at genion!'+'\\n')
			errq.close()
			sys.exit(1)
		pass
	if IONS == 'POS':
		asd=subprocess.Popen([GMX_PREFIX,'genion', '-s', 'protein_ions.tpr', '-o', 'protein_ions.gro', '-p', 'protein.top', '-pname', 'NA', '-np', str(CHARGE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output,error=asd.communicate('SOL')
		asd.wait()
		#~~Check for fatal error~~~
		for f in error.split('\\n'):
			if (re.match('Fatal error',f) or re.match('Can not open file',f)):
				copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
				#print('Fatal Error: Found at genion!')
				delete=os.listdir('.')
				for ff in delete:
					os.remove(ff)
				os.chdir('..')
				os.rmdir(SIM_INPUT.split('.')[0])
				errq=open('error_minim/error_log.txt','a')
				errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at genion!'+'\\n')
				errq.close()
				sys.exit(1)
		if os.path.isfile('protein_ions.gro') and os.path.getsize('protein_ions.gro') > 0:
			pass
		else:
			#print('Fatal Error: Found at genion!')
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at genion!'+'\\n')
			errq.close()
			sys.exit(1)
		#print('~~~~~GENION Finished!~~~~~~~~~~~~')
	elif IONS == 'NEG':
		asd=subprocess.Popen([GMX_PREFIX,'genion', '-s', 'protein_ions.tpr', '-o', 'protein_ions.gro', '-p', 'protein.top', '-nname', 'CL', '-nn', str(CHARGE)], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output,error=asd.communicate('SOL')
		asd.wait()
		#~~Check for fatal error~~~
		for f in error.split('\\n'):
			if (re.match('Fatal error',f) or re.match('Can not open file',f)):
				copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
				#print('Fatal Error: Found at genion!')
				delete=os.listdir('.')
				for ff in delete:
					os.remove(ff)
				os.chdir('..')
				os.rmdir(SIM_INPUT.split('.')[0])
				errq=open('error_minim/error_log.txt','a')
				errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at genion!'+'\\n')
				errq.close()
				sys.exit(1)
		if os.path.isfile('protein_ions.gro') and os.path.getsize('protein_ions.gro') > 0:
			pass
		else:
			#print('Fatal Error: Found at genion!')
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at genion!'+'\\n')
			errq.close()
			sys.exit(1)
		#print('~~~~~GENION Finished!~~~~~~~~~~~~')
	pass
	#~~~~~~~~~Steep minimization~~~~~~~~~~~
	asd=subprocess.Popen([GMX_PREFIX,'grompp', '-f', 'minim_solv.mdp', '-c', 'protein_ions.gro', '-p', 'protein.top', '-o', 'protein_minim.tpr'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			#print('Fatal Error: Found at grompp minim steep!')
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at grompp minim steep!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_minim.tpr') and os.path.getsize('protein_minim.tpr') > 0:
		pass
	else:
		#print('Fatal Error: Found at grompp minim steep!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at grompp minim!'+'\\n')
		errq.close()
		sys.exit(1)
	asd=subprocess.Popen([GMX_PREFIX,'mdrun', '-v', '-deffnm', 'protein_minim'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	#~~Check for fatal error~~~
	for f in error.split('\\n'):
		if (re.match('Fatal error',f) or re.match('Can not open file',f)):
			#print('Fatal Error: Found at mdrun minim steep!')
			copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
			delete=os.listdir('.')
			for ff in delete:
				os.remove(ff)
			os.chdir('..')
			os.rmdir(SIM_INPUT.split('.')[0])
			errq=open('error_minim/error_log.txt','a')
			errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at mdrun minim!'+'\\n')
			errq.close()
			sys.exit(1)
	if os.path.isfile('protein_minim.gro') and os.path.getsize('protein_minim.gro') > 0:
		pass
	else:
		#print('Fatal Error: Found at mdrun minim steep!')
		copyfile(SIM_INPUT,'../error_minim/'+SIM_INPUT)
		delete=os.listdir('.')
		for ff in delete:
			os.remove(ff)
		os.chdir('..')
		os.rmdir(SIM_INPUT.split('.')[0])
		errq=open('error_minim/error_log.txt','a')
		errq.write(str(SIM_INPUT.split('.')[0])+' Fatal Error: Found at mdrun minim!'+'\\n')
		errq.close()
		sys.exit(1)
	#print('~~~~~MINIMIZATION USING STEEPEST DESCENTS Finished!~~~~~~~~~~~~')
	pass
	asd=subprocess.Popen([GMX_PREFIX,'editconf','-f','protein_minim.gro','-o','protein_minim.pdb'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	pass
	zxc=open('protein_minim.pdb','r')
	mnb=zxc.readlines()
	zxc.close
	CHAIN='P'
	zxc=open('../'+SIM_INPUT,'w')
	for f in mnb:
		if ant(f,'ra') not in ['SOL','NA','CL']:
			if f[0:6].strip() in ['ATOM']:
				stump=f[0:21]+CHAIN+f[22:]
				zxc.write(stump) #add chain and atom type in the end column
#			else:
#				zxc.write(f)
	zxc.close()
	delete=os.listdir('.')
	for f in delete:
		os.remove(f)
	os.chdir('..')
	os.rmdir(SIM_INPUT.split('.')[0])
	#print('~~~~~MINIMIZATION Finished!~~~~~~~~~~~~')
" >PepLib_Minim.py
echo -e "#~~~ Running Peptide Minimization~~~~#"
time=`date +"%c"`;echo -e "Peptide minimization start time : "$time"\\n" >>"$WORKING"/summary.txt\n'''
			if PEPMODEL_check.get() == 1:
				BASHSCRIPT+='''\nls -1U ../modpep/ | grep 'pdb' | parallel -j 1 --eta "cp ../modpep/{} .; python PepLib_Minim.py {}"'''
			elif PEPMODEL_check.get() == 0:
				BASHSCRIPT+='''\nls -1U "$PEPTIDE" | grep 'pdb' | parallel -j 1 --eta "cp "$PEPTIDE"/{} .; python PepLib_Minim.py {}"'''
			BASHSCRIPT+='''
rm *.mdp; rm PepLib_Minim.py
errcheck=`ls -1 error_minim/`
if [ -n "$errcheck" ]
then
	:
else
	rmdir error_minim
fi
time=`date +"%c"`;echo -e "Peptide minimization end time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
'''
		if PDBQT_check.get() == 1:
			BASHSCRIPT+='''
clear
cd "$WORKING"
mkdir pdbqt; cd pdbqt; mkdir error_pdbqt
cp "$MGLROOT"/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py .
echo -n "
#!/bin/bash
MINIM="$MINIM"
pdbqt_error=\`grep \\"Sorry\\\, there are no Gasteiger parameters\\" \\"\$1\\"\`
pdbqt_warn_error=\`grep \\"WARNING:\\" \\"\$1\\"\`
traceback_error=\`grep \\"Traceback\\" \\"\$1\\"\`
if [ -n \\"\$pdbqt_error\\" ] || [ -n \\"\$pdbqt_warn_error\\" ] || [ -n \\"\$tracebackerror\\" ]
then
	if [ \\"\$MINIM\\" == \\"YES\\" ]
	then
		cp "$WORKING"/minim/\\"\$2\\" "$WORKING"/pdbqt/error_pdbqt/ 2>/dev/null
	else
		cp "$WORKING"/modpep/\\"\$2\\" "$WORKING"/pdbqt/error_pdbqt/ 2>/dev/null
	fi
	rm \\"\$3\\" 2>/dev/null
fi" >pddbqt_error_check.bash
echo -e "#~~~ Running PDBQT conversion ~~~~#"
time=`date +"%c"`;echo -e "PDBQT conversion start time : "$time"\\n" >>"$WORKING"/summary.txt
'''
			if MINIM_check.get() == 1:
				if TORSION_check.get() == 1:
					BASHSCRIPT+='''
ls -1 "$WORKING"/minim/ | grep 'pdb' | parallel -j "$joobs" --eta --no-notice ""$MGLROOT"/bin/pythonsh prepare_ligand4.py -l "$WORKING"/minim/{} -A bonds_hydrogens -Z &>>{.}_log.txt ; bash pddbqt_error_check.bash {.}_log.txt {} {.}.pdbqt ; rm {.}_log.txt"
'''
				elif TORSION_check.get() == 0:
					BASHSCRIPT+='''
ls -1 "$WORKING"/minim/ | grep 'pdb' | parallel -j "$joobs" --eta --no-notice ""$MGLROOT"/bin/pythonsh prepare_ligand4.py -l "$WORKING"/minim/{} -A bonds_hydrogens &>>{.}_log.txt ; bash pddbqt_error_check.bash {.}_log.txt {} {.}.pdbqt ; rm {.}_log.txt"
'''
			elif MINIM_check.get() == 0:
				if TORSION_check.get() == 1:
					BASHSCRIPT+='''
ls -1 "$WORKING"/modpep/ | grep 'pdb' | parallel -j "$joobs" --eta --no-notice ""$MGLROOT"/bin/pythonsh prepare_ligand4.py -l "$WORKING"/modpep/{} -A bonds_hydrogens -Z &>>{.}_log.txt ; bash pddbqt_error_check.bash {.}_log.txt {} {.}.pdbqt ; rm {.}_log.txt"
'''
				elif TORSION_check.get() == 0:
					BASHSCRIPT+='''
ls -1 "$WORKING"/modpep/ | grep 'pdb' | parallel -j "$joobs" --eta --no-notice ""$MGLROOT"/bin/pythonsh prepare_ligand4.py -l "$WORKING"/modpep/{} -A bonds_hydrogens &>>{.}_log.txt ; bash pddbqt_error_check.bash {.}_log.txt {} {.}.pdbqt ; rm {.}_log.txt"
'''
			BASHSCRIPT+='''
rm pddbqt_error_check.bash prepare_ligand4.py
errcheck=`ls -1 error_pdbqt/`
if [ -n "$errcheck" ]
then
	:
else
	rmdir error_pdbqt
fi
time=`date +"%c"`;echo -e "PDBQT conversion end time : "$time"\\n\\n\\n" >>"$WORKING"/summary.txt
'''
		BASHSCRIPT+='''\ntime=`date +"%c"`;echo -e "\\n\\n\\n\\nPeptide preparation end time : "$time"\\n" >>"$WORKING"/summary.txt'''
		os.chdir(WORKING)
		pep_write=open('Pep_Mod.bash','w')
		pep_write.write(BASHSCRIPT)
		pep_write.close()
		root.destroy()
	Button(run_pep,text="Hit Run!",bg="black",fg="white",font=("Times",15,"bold","underline"),width=10,height=2,command=print_bash_script).grid(row=12,column=0,columnspan=2,sticky=E+W+N+S)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Peptide Screening Tools ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~ AutoDock Vina: start
def run_vina():
	docktools.destroy()
	vina_vs=Toplevel(root)
	global CWD
	Label(vina_vs,text="AutoDock Vina: Inputs",bg="white",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=0,column=0,columnspan=2,sticky=E+W+N+S)
	Label(vina_vs,bg="white",text="Enter the peptide structures \n in pdbqt format:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=1,column=0,sticky=E+W+N+S)
	def get_peptide_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/peptide",title="Enter the peptide structures directory",parent=vina_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=vina_vs)
				return
			else:
				global PEPTIDE
				PEPTIDE=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=vina_vs)
			return
	Button(vina_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_peptide_dir).grid(row=1,column=1,sticky=E+W+N+S)
	Label(vina_vs,bg="white",text="Enter the receptor structures:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=2,column=0,sticky=E+W+N+S)
	def get_receptor_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/receptor",title="Enter the receptor structures directory",parent=vina_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=vina_vs)
				return
			else:
				global RECEPTOR
				RECEPTOR=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=vina_vs)
			return
	Button(vina_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_receptor_dir).grid(row=2,column=1,sticky=E+W+N+S)
	Label(vina_vs,bg="white",text="Enter the working directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=3,column=0,sticky=E+W+N+S)
	def get_working_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/working",title="Enter the working directory",parent=vina_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=vina_vs)
				return
			else:
				os.chdir(filetemp)
				zxc=os.listdir('.')
				if zxc:
					tkMessageBox.showinfo("Warning!","Working directory is not empty!",parent=vina_vs)
					return
				else:
					global WORKING
					WORKING=filetemp
					os.chdir(CWD)
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=vina_vs)
			return
	Button(vina_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_working_dir).grid(row=3,column=1,sticky=E+W+N+S)
	#~~~~~~~~~~~~~~ Number of CPU calculation start
	Ncpu=multiprocessing.cpu_count()
	Label(vina_vs,bg="white",text=str(Ncpu)+" number of CPU processors \n detected in your system",relief=SOLID,font=("Times",15,'bold'),width=30,height=3,justify=CENTER).grid(row=4,column=0,columnspan=2,sticky=E+W+N+S)
	Label(vina_vs,bg="white",text="Enter the No. of CPU \nfor single vina job:",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=5,column=0,sticky=W+E+N+S)
	global Numcpu
	Numcpu=StringVar()
	Numcpu.set(8)
	joobs=int(Ncpu/int(Numcpu.get()))
	if joobs:
		Label(vina_vs,bg="white",text= str(int(Ncpu/int(Numcpu.get())))+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
	Entry(vina_vs,bd=5,textvariable=Numcpu,font=("Times",15,'bold'),justify=CENTER).grid(row=5,column=1,sticky=W+E+N+S)
	def checkback(*args):
		for f in Numcpu.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=vina_vs)
				return
		global joobs
		joobs=0
		if len(Numcpu.get()) > 0:
			if int(Numcpu.get()) > Ncpu or int(Numcpu.get()) == 0 :
				tkMessageBox.showinfo("Warning","Please provide the values less than "+str(Ncpu)+"!",parent=vina_vs)
				return
			else:
				Label(vina_vs,bg="white",text= str(int(Ncpu/int(Numcpu.get())))+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
				joobs=int(Ncpu/int(Numcpu.get()))
		else:
			Label(vina_vs,bg="white",text= "0 Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
	Numcpu.trace('w',checkback)	
	#~~~~~~~~~~ Number of CPU calculation end
	#~~~~~ Exhaustiveness start
	Label(vina_vs,bg="white",text="Enter the exhaustiveness:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=7,column=0,sticky=E+W+N+S)
	Exhaust=StringVar()
	Exhaust.set(8)
	global EXHAUSTIVENESS
	EXHAUSTIVENESS=int(Exhaust.get())	
	Entry(vina_vs,bd=5,textvariable=Exhaust,font=("Times",15,'bold'),justify=CENTER).grid(row=7,column=1,columnspan=3,sticky=W+E+N+S)
	def ex_checkback(*args):
		for f in Exhaust.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=vina_vs)
				return
		global EXHAUSTIVENESS
		EXHAUSTIVENESS=int(Exhaust.get())
	Exhaust.trace('w',ex_checkback)
	#~~~~~ Exhaustiveness end
	#~~~~~~~~~~ ZRANK start
	Label(vina_vs,bg="white",text= "Do you want to rescore \n using ZRANK?",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=8,column=0,sticky=W+E+N+S)
	ZRANKRESCORE_check=IntVar()
	Checkbutton(vina_vs,variable=ZRANKRESCORE_check,onvalue=1,offvalue=0,bg="white",font=("Times",10,"bold"),relief=SOLID,width=10,height=3).grid(row=8,column=1,sticky=E+W+N+S)	
	def zrankrescore_check(*args):
		if ZRANKRESCORE_check.get() == 1:
			if not ZRANK:
				tkMessageBox.showinfo("Warning","ZRANK path not specified!",parent=vina_vs)
				return
	ZRANKRESCORE_check.trace('w',zrankrescore_check)
	#~~~~~~~~~ ZRANK end
	#~~~~~~~~ FlexpepDock start
	Label(vina_vs,bg="white",text= "Do you want to run Flexible \n refinement using FlexPepDock?",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=9,column=0,sticky=W+E+N+S)
	FLEXREF_check=IntVar()
	Checkbutton(vina_vs,variable=FLEXREF_check,onvalue=1,offvalue=0,bg="white",font=("Times",10,"bold"),relief=SOLID,width=10,height=3).grid(row=9,column=1,sticky=E+W+N+S)	
	def flexref_check(*args):
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning","FlexPepDock path not specified!",parent=vina_vs)
				return
	FLEXREF_check.trace('w',flexref_check)
	#~~~~~~~~ Flexpepdock: end
	#~~~ Vina script start
	def print_vina_script():
		if PARALLEL_check.get() == 0:
			tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=vina_vs)
			return
		if not PEPTIDE:
			tkMessageBox.showinfo("Warning!","The peptide directory not specified!",parent=vina_vs)
			return
		if not RECEPTOR:
			tkMessageBox.showinfo("Warning!","The Receptor directory not specified!",parent=vina_vs)
			return
		if not WORKING:
			tkMessageBox.showinfo("Warning!","Working directory not specified!",parent=vina_vs)
			return
		if VINA_check.get() == 0:
			tkMessageBox.showinfo("Warning","Vina not installed!",parent=vina_vs)
			return
		if not joobs or not Numcpu.get():
			tkMessageBox.showinfo("Warning","Number of CPU's for parallel jobs not specified!",parent=vina_vs)
			return
		if not EXHAUSTIVENESS:
			tkMessageBox.showinfo("Warning","Exhaustiveness not specified!",parent=vina_vs)
			return
		os.chdir(WORKING)
		BASHSCRIPT='''
#!/bin/bash
PEPTIDE="%s"
RECEPTOR="%s"
WORKING="%s" ''' %(PEPTIDE,RECEPTOR,WORKING)
		if ZRANKRESCORE_check.get() == 1:
			if not ZRANK:
				tkMessageBox.showinfo("Warning","ZRANK2 path not specified!",parent=vina_vs)
				return
			if not HBPLUS:
				tkMessageBox.showinfo("Warning!","HBPLUS path not specified!",parent=vina_vs)
				return
			BASHSCRIPT+='''\nSCORE="YES"\nHBPLUSDIR="%s"\nZRANK="%s"''' %(HBPLUS,ZRANK)
		elif ZRANKRESCORE_check.get() == 0:
			BASHSCRIPT+='''\nSCORE="NO"'''
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning","FlexPepDock path not specified!",parent=vina_vs)
				return
			BASHSCRIPT+='\nROSETTA_DIR="'+'/'.join(FLEXPEPDOCK.split('/')[:-4])+'"'
		BASHSCRIPT+='\njoobs=%d\nnumcpu=%d\nex=%d' %(joobs,int(Numcpu.get()),int(EXHAUSTIVENESS))
		BASHSCRIPT+='''\n\n
echo -e "================================================================================"
echo -e "Peptide directory: "$PEPTIDE""
echo -e "Receptor directory: "$RECEPTOR""
echo -e "Working directory: "$WORKING""
echo -e "Peptide Docking tool: AutoDock Vina"
echo -e "Number of CPU's to run single Vina job: "$numcpu""
echo -e "Number of parallel jobs: "$joobs""
echo -e "Exhaustiveness:"$ex""'''
		if ZRANKRESCORE_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Rescoring using ZRANK2: "YES""'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
echo -e "Rosetta directory:"$ROSETTA_DIR""
echo -e "Flexible refinement using FlexPepDock: YES"'''
		BASHSCRIPT+='''
echo -e "================================================================================"
echo -e "Please enter [1] to accept the input [2] to quit"
i=1
while [ "$i" -ge 0 ]
do
	read -ep ">>>" check
	if [ "$check" == 1 ]
	then
		:
		break
	elif [ "$check" == 2 ]
	then
		exit
	else
		echo "Wrong input! Enter again"
	fi
done
cd "$WORKING"
echo -e "Peptide directory: "$PEPTIDE"\\nReceptor directory: "$RECEPTOR"\\nWorking directory: "$WORKING"\\nPeptide Docking tool: AutoDock Vina\\nNo. of CPU's to run single Vina job: "$numcpu"\\nNo. of parallel jobs: "$joobs"\\nExhaustiveness: "$ex"" >>"$WORKING"/summary.txt'''
		if ZRANKRESCORE_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Rescoring using ZRANK2: "YES"" >>"$WORKING"/summary.txt'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
echo -e "Rosetta directory:"$ROSETTA_DIR"" >>"$WORKING"/summary.txt
echo -e "Flexible refinement using FlexPepDock: YES" >>"$WORKING"/summary.txt'''
		BASHSCRIPT+='''
#~~~ space check in peptide file name
peptotal=`ls -1U "$PEPTIDE"/ | grep "pdbqt" | tee spacecheck.txt | wc -l`
spacecheck=`sed -n "/\s/p" spacecheck.txt`
if [ -n "$spacecheck" ]
then
	echo -e "~~Space detected in the ligand files~~~\\nSpace will be replaced by _ in the filename"
	sed -n "/\s/p" spacecheck.txt >spacefiles.txt
	echo -n "
	#!/bin/bash
	bspace=\`echo \\"\$1\\" | sed \\"s/\s/_/g\\"\` 
	mv \\"\$1\\" \\"\$bspace\\"" >rename.bash
	cat spacefiles.txt | grep "pdbqt" | parallel -j 0 --no-notice --eta bash rename.bash {}
	rm rename.bash spacefiles.txt
else
	:
fi
rm spacecheck.txt
#~~ space check in receptor file name
cd "$RECEPTOR"
###Spack check####
ls -1U >prospacecheck.ali
spacecheck=`sed -n "/\s/p" prospacecheck.ali`
if [ -n "$spacecheck" ]
then
	echo -e "~~Space detected in the receptor files~~~\\nSpace will be replaced by _ in the filename"
	sed -n "/\s/p" prospacecheck.ali >spacefiles.ali
	echo -n "
	#!/bin/bash
	bspace=\`echo \\"\$1\\" | sed \\"s/\s/_/g\\"\` 
	mv \\"\$1\\" \\"\$bspace\\"" >rename.bash
	cat prospacefiles.ali | grep "pdbqt" | parallel -j 0 --no-notice --eta bash rename.bash {}
	cat prospacefiles.ali | grep "txt" | parallel -j 0 --no-notice --eta bash rename.bash {}
	rm rename.bash spacefiles.ali
else
	:
fi
rm prospacecheck.ali
ls -1 *.pdbqt >protein_list.txt
sed -i "s/.pdbqt//g" protein_list.txt
while read -r l
do
	reftxt=`ls "$l".txt  2>/dev/null`
	if [ -n "$reftxt" ]
	then
		:
	else
		rm protein_list.txt; 
		echo -e "Configuration file not found for "$l" protein in the "$RECEPTOR"/\\n Please Check and start the process again\\n\\n"
		exit
	fi
done <protein_list.txt
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clear
cd "$WORKING"
echo -n "
#-*- coding: utf-8 -*-
import sys
asd=open(sys.argv[1],'r')
INPUT=asd.readlines()
asd.close()
check='NO'
asd=open(sys.argv[1],'w')
for f in INPUT:
	if check=='NO':
		if f[0:4] == 'ATOM' and f[21] == 'P':
			asd.write('TER\\n')
			check='YES'
	asd.write(f)" >"$WORKING"/reedit.py

while read -r l
do
	clear
	cd "$WORKING"
	mkdir "$l";cd "$l";mkdir Results;cd Results; mkdir docked_pdb;cd ../
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening Start time for "$l": "$time"\\n\\n" >>"$WORKING"/summary.txt
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening using AutoDock Vina Start time for "$l": "$time"\\n\\n" >>"$WORKING"/summary.txt
	mkdir pdbqt_output pdbqt_txt
	RECEPNAME="$l".pdbqt;configtest="$l".txt
	cd "$WORKING"/"$l"
	cp "$RECEPTOR"/"$l".pdbqt .;cp "$RECEPTOR"/"$l".txt .;
	echo -n "
	#!/bin/bash
	SCORE="$SCORE"
	if [ \\"\$SCORE\\" == 'YES' ]
	then
		mkdir \${1%.txt}; cd \${1%.txt}; cp ../pdbqt_output/\${1%.txt}.pdbqt .
		vina_split --input \${1%.txt}.pdbqt --ligand lig 1>/dev/null
		rm \${1%.txt}.pdbqt; cut -c-66 ../"$RECEPNAME" >${RECEPNAME%.pdbqt}.pdb
		"$HBPLUSDIR"/hbplus ${RECEPNAME%.pdbqt}.pdb -o &>>"$WORKING"/log.txt; rm ${RECEPNAME%.pdbqt}.pdb; 
		for f in lig*.pdbqt
		do
			echo \\"\$f\\" \$(grep 'VINA RESULT' \\"\$f\\" | awk '{print \$4}') >>vina_score.txt
			cut -c-66 \\"\$f\\" | sed '/ROOT/d;/ENDROOT/d;/BRANCH/d;/ENDBRANCH/d;/TORSDOF/d;s/<0>/PEP/g;' >\${f%.pdbqt}.pdb; rm \\"\$f\\"
			"$HBPLUSDIR"/hbplus \${f%.pdbqt}.pdb -o &>>"$WORKING"/log.txt; rm \${f%.pdbqt}.pdb; cat ${RECEPNAME%.pdbqt}.h \${f%.pdbqt}.h >\${f%.pdbqt}.pdb;
			python "$WORKING"/reedit.py \${f%.pdbqt}.pdb
		done
		ls -1 *.pdb >list.txt
		"$ZRANK"/zrank list.txt
		rm list.txt; sort -k2n list.txt.zr.out >zrank_refined.txt; bestmodel=\`head -n 1 zrank_refined.txt | awk '{print \$1}'\`; zrank_score=\`head -n 1 zrank_refined.txt | awk '{print \$2}'\`;
		cat \\"\$bestmodel\\" | sed \\"/^HEADER/d;/^REMARK/d;s/HETATM/ATOM  /g\\" >"$WORKING"/"$l"/Results/docked_pdb/\${1%.txt}.pdb
		vina_score=\`grep \\"\$bestmodel\\" vina_score.txt | awk '{print \$2}'\`
		ls -1U | parallel -j 1 rm {};cd .. ; rmdir \${1%.txt}/
		echo -e \\"\${1%.txt}\\t\\"\$vina_score\\"\\t\\"\$zrank_score\\"\\" >>"$WORKING"/"$l"/Results/output.txt
	else
		lol=\`grep -n \\"\-\-\-\-\-\+\\" "$WORKING"/"$l"/pdbqt_txt/\\"\$1\\" | cut -c1-2\`
		if [ -n \\"\$lol\\" ]
		then
			lol=\`expr \\"\$lol\\" + 1\`
			value=\`cat "$WORKING"/"$l"/pdbqt_txt/\\"\$1\\" | sed -n \\"\$lol\\"p | cut -c10-20\`
		else
			value=0
		fi
		mkdir \${1%.txt}; cd \${1%.txt}; cp ../pdbqt_output/\${1%.txt}.pdbqt .
		vina_split --input \${1%.txt}.pdbqt --ligand lig 1>/dev/null
		rm \${1%.txt}.pdbqt; ltest=\`ls -1 lig*.pdbqt| wc -l\`;if [ \\"\$ltest\\" -le 9 ]; then mv lig1.pdbqt \${1%.txt}.pdbqt; else mv lig01.pdbqt \${1%.txt}.pdbqt;fi; 
		cat ../"$RECEPNAME" | cut -c-66 >"$WORKING"/"$l"/Results/docked_pdb/\${1%.txt}.pdb
		cut -c-66 \${1%.txt}.pdbqt | sed '/ROOT/d;/ENDROOT/d;/BRANCH/d;/ENDBRANCH/d;/TORSDOF/d;s/<0>/PEP/g' >>"$WORKING"/"$l"/Results/docked_pdb/\${1%.txt}.pdb
		ls -1U | parallel -j 1 rm {};cd .. ; rmdir \${1%.txt}/
		echo -e \\"\${1%.txt}\\t\\"\$value\\"\\" >>"$WORKING"/"$l"/Results/output.txt
	fi" >feb.bash
	echo -e "~~~~~~ Running AutoDock Vina for "$l"~~~~~~~~~"
	cd "$WORKING"/"$l"
	ls -1U "$PEPTIDE"/ | grep 'pdbqt' | parallel -j "$joobs" --no-notice --eta "cp "$PEPTIDE"/{} .;  vina --config "$configtest" --receptor "$RECEPNAME" --ligand {} --exhaustiveness "$ex" --cpu "$numcpu" --num_modes 20 --out pdbqt_output/{} --log pdbqt_txt/{.}.txt >>"$WORKING"/log.txt;bash feb.bash {.}.txt ; rm {}"
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	if [ "$SCORE" != 'YES' ]
	then
		cd "$WORKING"/"$l"/Results/docked_pdb;
		ls -1U | grep "pdb" | parallel -j "$joobs" "python "$WORKING"/reedit.py {}"
	fi
	cd "$WORKING"/"$l"; rm "$RECEPNAME" "$configtest" feb.bash 
	cd "$WORKING"/"$l"/Results/;  
	if [ "$SCORE" == 'YES' ]
	then
		sort -k3n output.txt >sorted.txt; rm output.txt;sed -i "1i Peptide_Name\\tVina_SCORE\\tZRANK_SCORE" sorted.txt;
		echo -e "Top 10 results for "$l" screening:" >>"$WORKING"/summary.txt
		head -n 11 sorted.txt >>"$WORKING"/summary.txt
	else
		sort -k2n output.txt >sorted.txt; rm output.txt;sed -i "1i Peptide_Name\\tVina_SCORE" sorted.txt; 
		echo -e "Top 10 results for "$l" screening:" >>"$WORKING"/summary.txt
		head -n 11 sorted.txt >>"$WORKING"/summary.txt
	fi
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening using AutoDock Vina End time for "$l": "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''\n\tjoobs="%d"''' %(int(Numcpu.get()))
			BASHSCRIPT+='''
	cd "$WORKING"/"$l"
	#~~~~ flags for flexpepdock -- prepack ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database
-flexpep_prepack
-ignore_zero_occupancy false
-ex1
-ex2aro
-out:suffix _prepack
-out:file:scorefile score_prepack.sc" >"$WORKING"/"$l"/flags_prepack
	#~~~~ flags for flexpepdock -- refine ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database 
-scorefile score.sc 
-min_receptor_bb 
-lowres_preoptimize 
-pep_refine 
-flexpep_score_only
-nstruct 1 
-ex1 
-ex2aro 
-use_input_sc 
-out:suffix _refine 
-out:file:scorefile score_refine.sc" >"$WORKING"/"$l"/flags_refine
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	clear
	echo -e "#~~~~~~~ Running Flexible Refinement using: FlexpepDock for "$l"~~~~~~~~~#"
	cd "$WORKING"/"$l"/Results; mkdir refine;cd refine
	#~~~~ Residue number re-arrange ~~~~~~~~~~~
	echo -n "
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
LIST=[]
PEP=[]
RECEPTOR=[]
for f in FILE1:
	if f[0:4] == 'ATOM' and f[21] == 'P':
		PEP.append(f.strip('\\n'))
		LIST.append(int(f[22:26].strip()))
	if f[0:4] == 'ATOM' and f[21] != 'P':
		RECEPTOR.append(f.strip('\\n'))
for f in RECEPTOR:
	print(f)
print('TER')
for f in set(sorted(LIST)):
	for ff in PEP:
		if int(ff[22:26].strip()) == f:
			print(ff)" >renumber.py
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	echo -n "
#!/bin/bash
if [ -s \\"\$1\\" ]
then
	rm \\"\${1%_prepack_0001.pdb}.pdb\\"; mv \\"\$1\\" \\"\${1%_prepack_0001.pdb}.pdb\\" 
	mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s \\"\${1%_prepack_0001.pdb}.pdb\\" @flags_refine &>>"$WORKING"/log.txt
	bestrefine=\`grep \\"^SCORE\\" score_refine.sc | sed \\"1d\\" | sort -k2n | head -n 1\`
	modelnum=\`echo \\"\$bestrefine\\" | awk '{print NF}'\`
	refinemodel=\`echo \\"\$bestrefine\\" | awk -v ll=\\"\$modelnum\\" '{print \$ll}'\`
	if [ -s \\"\$refinemodel\\".pdb ]
	then
		mv \\"\$refinemodel\\".pdb "$WORKING"/"$l"/Results/refine/\\"\${1%_prepack_0001.pdb}.pdb\\"
		repos=\\"\\";a=1;for f in \$(grep \\"^SCORE\\" score_refine.sc | sed -n \\"1p\\" | sed \\"s/\\t/,/g\\");do if [ \\"\$f\\" == 'reweighted_sc' ];then repos=\\"\$a\\";break;fi;a=\`expr \$a + 1\`;done
		echo -e \\"\\"\${1%_prepack_0001.pdb}\\"\\t\$(grep \${1%_prepack_0001.pdb} "$WORKING"/"$l"/Results/sorted.txt | cut -f2-)\\t\$(echo \\"\$bestrefine\\" | awk '{print \$2}')\\t\$(echo \\"\$bestrefine\\" | awk -v ll=\\"\$repos\\" '{print \$ll}')\\" >>"$WORKING"/"$l"/Results/Refine_score.txt
	else
		echo \\"\$1 Error during FlexpepDock Refinement\\" >>"$WORKING"/"$l"/Results/refine_error.txt
	fi
else
	echo \\"\$1 Error during FlexpepDock Prepack\\" >>"$WORKING"/"$l"/Results/refine_error.txt
fi
ls -1U | parallel -j 1 rm {}; cd ..; rmdir \${1%_prepack_0001.pdb}" >ROSE_check.bash
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	ls -1U "$WORKING"/"$l"/Results/docked_pdb/| grep "pdb" | parallel -j 1 --eta "mkdir {.}; cd {.}; python ../renumber.py "$WORKING"/"$l"/Results/docked_pdb/{} >{};cp "$WORKING"/"$l"/flags_prepack .; cp "$WORKING"/"$l"/flags_refine .;mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s {} @flags_prepack &>>"$WORKING"/log.txt; bash ../ROSE_check.bash {.}_prepack_0001.pdb"
	cd "$WORKING"/"$l"/Results/
	if [ -s refine_error.txt ]
	then
		echo "~~Error occured during FlexpepDock Refinement!~~"
	else
		if [ "$SCORE" == "YES" ]
		then
			head -n 1 sorted.txt | sed "s/$/\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score/g" >Refine_sorted.txt;sort -k4n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;	
			echo -e "Top 10 results for "$l" screening after flexible refinement:" >>"$WORKING"/summary.txt
			head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
		else
			head -n 1 sorted.txt | sed "s/$/\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score/g" >Refine_sorted.txt;sort -k3n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;		
			echo -e "Top 10 results for "$l" screening after flexible refinement:" >>"$WORKING"/summary.txt
			head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
		fi
	fi
	cd "$WORKING"/"$l"/Results/refine ; rm ROSE_check.bash renumber.py
	cd "$WORKING"/"$l"/; rm flags_prepack flags_refine
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement end time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		BASHSCRIPT+='''
done <"$RECEPTOR"/protein_list.txt
cd "$WORKING"; rm log.txt reedit.py 
rm "$RECEPTOR"/protein_list.txt
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening End time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
	#~~~ vina script end
		bash_script=open('PepVs.bash','w')
		bash_script.write(BASHSCRIPT)
		bash_script.close()
		root.destroy()
	Button(vina_vs,text="Hit Run!",bg="black",fg="white",font=("Times",15,"bold","underline"),width=10,height=3,command=print_vina_script).grid(row=10,column=0,columnspan=2,sticky=E+W+N+S)

#~~~ AutoDock Vina: end


#~~~ ZDOCK: start
def run_zdock():
	docktools.destroy()
	zdock_vs=Toplevel(root)
	global CWD
	Label(zdock_vs,text="ZDOCK: Inputs",bg="white",font=("Times",15,"bold"),relief=SOLID,width=10,height=3).grid(row=0,column=0,columnspan=2,sticky=E+W+N+S)
	Label(zdock_vs,bg="white",text="Enter the peptide structures \n in pdb format:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=1,column=0,sticky=E+W+N+S)
	def get_peptide_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/peptide",title="Enter the peptide structures directory",parent=zdock_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=zdock_vs)
				return
			else:
				global PEPTIDE
				PEPTIDE=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=zdock_vs)
			return
	Button(zdock_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_peptide_dir).grid(row=1,column=1,sticky=E+W+N+S)
	Label(zdock_vs,bg="white",text="Enter the receptor structures:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=2,column=0,sticky=E+W+N+S)
	def get_receptor_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/receptor",title="Enter the receptor structures directory",parent=zdock_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=zdock_vs)
				return
			else:
				global RECEPTOR
				RECEPTOR=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=zdock_vs)
			return
	Button(zdock_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_receptor_dir).grid(row=2,column=1,sticky=E+W+N+S)
	Label(zdock_vs,bg="white",text="Enter the working directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=3,column=0,sticky=E+W+N+S)
	def get_working_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/working",title="Enter the working directory",parent=zdock_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=zdock_vs)
				return
			else:
				os.chdir(filetemp)
				zxc=os.listdir('.')
				if zxc:
					tkMessageBox.showinfo("Warning!","Working directory is not empty!",parent=zdock_vs)
					return
				else:
					global WORKING
					WORKING=filetemp
					os.chdir(CWD)
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=zdock_vs)
			return
	Button(zdock_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_working_dir).grid(row=3,column=1,sticky=E+W+N+S)
	#~~~~~~~~~~~~~~ Number of CPU calculation start
	Ncpu=multiprocessing.cpu_count()
	Label(zdock_vs,bg="white",text=str(Ncpu)+" number of CPU processors \n detected in your system",relief=SOLID,font=("Times",15,'bold'),width=30,height=3,justify=CENTER).grid(row=4,column=0,columnspan=2,sticky=E+W+N+S)
	Label(zdock_vs,bg="white",text="Enter the number of CPU \n for running jobs in parallel :",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=5,column=0,sticky=W+E+N+S)
	global Numcpu
	Numcpu=StringVar()
	Numcpu.set(Ncpu)
	if len(Numcpu.get()) > 0:
		Label(zdock_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
		joobs=int(Numcpu.get())
	Entry(zdock_vs,bd=5,textvariable=Numcpu,font=("Times",15,'bold'),justify=CENTER).grid(row=5,column=1,sticky=W+E+N+S)
	def checkback(*args):
		for f in Numcpu.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=zdock_vs)
				return
		global joobs
		joobs=0
		if len(Numcpu.get()) > 0:
			if int(Numcpu.get()) > Ncpu or int(Numcpu.get()) == 0 :
				tkMessageBox.showinfo("Warning","Please provide the values less than "+str(Ncpu)+"!",parent=zdock_vs)
				return
			else:
				Label(zdock_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
				joobs=int(Numcpu.get())
		else:
			Label(zdock_vs,bg="white",text= "0 Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
	Numcpu.trace('w',checkback)	
	#~~~~~~~~~~ Number of CPU calculation end
	#~~~~~~~~~~ ZRANK start
	Label(zdock_vs,bg="white",text= "Do you want to rescore \n using ZRANK?",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=8,column=0,sticky=W+E+N+S)
	ZRANKRESCORE_check=IntVar()
	Checkbutton(zdock_vs,variable=ZRANKRESCORE_check,onvalue=1,offvalue=0,bg="white",font=("Times",10,"bold"),relief=SOLID,width=10,height=3).grid(row=8,column=1,sticky=E+W+N+S)	
	def zrankrescore_check(*args):
		if ZRANKRESCORE_check.get() == 1:
			if not ZRANK:
				tkMessageBox.showinfo("Warning","ZRANK path not specified!",parent=zdock_vs)
				return
	ZRANKRESCORE_check.trace('w',zrankrescore_check)
	#~~~~~~~~~ ZRANK end
	#~~~~~~~~ FlexpepDock start
	Label(zdock_vs,bg="white",text= "Do you want to run Flexible \n refinement using FlexPepDock?",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=9,column=0,sticky=W+E+N+S)
	FLEXREF_check=IntVar()
	Checkbutton(zdock_vs,variable=FLEXREF_check,onvalue=1,offvalue=0,bg="white",font=("Times",10,"bold"),relief=SOLID,width=10,height=3).grid(row=9,column=1,sticky=E+W+N+S)	
	def flexref_check(*args):
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning","FlexPepDock path not specified!",parent=zdock_vs)
				return
	FLEXREF_check.trace('w',flexref_check)
	#~~~~ ZDOCK script: start
	def print_zdock_script():
		if PARALLEL_check.get() == 0:
			tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=zdock_vs)
			return
		if not PEPTIDE:
			tkMessageBox.showinfo("Warning!","The peptide directory not specified!",parent=zdock_vs)
			return
		if not RECEPTOR:
			tkMessageBox.showinfo("Warning!","The Receptor directory not specified!",parent=zdock_vs)
			return
		if not WORKING:
			tkMessageBox.showinfo("Warning!","Working directory not specified!",parent=zdock_vs)
			return
		if not joobs:
			tkMessageBox.showinfo("Warning!","Number of Jobs to run in parallel not specified!",parent=zdock_vs)
			return
		if not ZDOCK:
			tkMessageBox.showinfo("Warning!","ZDOCK path not specified!",parent=zdock_vs)
			return
		if not joobs:
			tkMessageBox.showinfo("Warning!","Number of CPU's for parallel jobs not specified!",parent=zdock_vs)
			return
		os.chdir(WORKING)
		BASHSCRIPT='''
#!/bin/bash
PEPTIDE="%s"
RECEPTOR="%s"
WORKING="%s" ''' %(PEPTIDE,RECEPTOR,WORKING)
		BASHSCRIPT+='''\nZDOCK="%s"\nHBPLUSDIR="%s"\n''' %(ZDOCK,HBPLUS)
		if ZRANKRESCORE_check.get() == 1:
			if not ZRANK:
				tkMessageBox.showinfo("Warning!","ZRANK2 path not specified!",parent=zdock_vs)
				return
			if not HBPLUS:
				tkMessageBox.showinfo("Warning!","HBPLUS path not specified!",parent=zdock_vs)
				return
			BASHSCRIPT+='''\nSCORE="YES"\nHBPLUSDIR="%s"\nZRANK="%s"''' %(HBPLUS,ZRANK)
		elif ZRANKRESCORE_check.get() == 0:
			BASHSCRIPT+='''\nSCORE="NO"'''
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning!","FlexPepDock path not specified!",parent=zdock_vs)
				return
			BASHSCRIPT+='\nROSETTA_DIR="'+'/'.join(FLEXPEPDOCK.split('/')[:-4])+'"'
		BASHSCRIPT+='\njoobs=%d' %(joobs)
		BASHSCRIPT+='''\n\n
echo -e "================================================================================"
echo -e "Peptide directory: "$PEPTIDE""
echo -e "Receptor directory: "$RECEPTOR""
echo -e "Working directory: "$WORKING""
echo -e "Peptide Docking tool: ZDOCK"
echo -e "Number of CPU's for parallel jobs: "$joobs""'''
		if ZRANKRESCORE_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Rescoring using ZRANK2: "YES""'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
echo -e "Rosetta directory:"$ROSETTA_DIR""
echo -e "Flexible refinement using FlexPepDock: YES"'''
		BASHSCRIPT+='''
echo -e "================================================================================"
echo -e "Please enter [1] to accept the input [2] to quit"
i=1
while [ "$i" -ge 0 ]
do
	read -ep ">>>" check
	if [ "$check" == 1 ]
	then
		:
		break
	elif [ "$check" == 2 ]
	then
		exit
	else
		echo "Wrong input! Enter again"
	fi
done
cd "$WORKING"
echo -e "Peptide directory: "$PEPTIDE"\\nReceptor directory: "$RECEPTOR"\\nWorking directory: "$WORKING"\\nPeptide Docking tool: ZDOCK\\nNo. of CPU's for parallel jobs: "$joobs"" >>"$WORKING"/summary.txt'''
		if ZRANKRESCORE_check.get() == 1:
			BASHSCRIPT+='''\necho -e "Rescoring using ZRANK2: "YES"" >>"$WORKING"/summary.txt'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
echo -e "Rosetta directory:"$ROSETTA_DIR"" >>"$WORKING"/summary.txt
echo -e "Flexible refinement using FlexPepDock: YES" >>"$WORKING"/summary.txt'''
		BASHSCRIPT+='''
#~~~ space check in peptide file name
peptotal=`ls -1U "$PEPTIDE"/ | grep "pdb" | tee spacecheck.txt | wc -l`
spacecheck=`sed -n "/\s/p" spacecheck.txt`
if [ -n "$spacecheck" ]
then
	echo -e "~~Space detected in the ligand files~~~\\nSpace will be replaced by _ in the filename"
	sed -n "/\s/p" spacecheck.txt >spacefiles.txt
	echo -n "
	#!/bin/bash
	bspace=\`echo \\"\$1\\" | sed \\"s/\s/_/g\\"\` 
	mv \\"\$1\\" \\"\$bspace\\"" >rename.bash
	cat spacefiles.txt | grep "pdb" | parallel -j 0 --no-notice --eta bash rename.bash {}
	rm rename.bash spacefiles.txt
else
	:
fi
rm spacecheck.txt
#~~ space check in receptor file name
cd "$RECEPTOR"
###Spack check####
ls -1U >prospacecheck.ali
spacecheck=`sed -n "/\s/p" prospacecheck.ali`
if [ -n "$spacecheck" ]
then
	echo -e "~~Space detected in the receptor files~~~\\nSpace will be replaced by _ in the filename"
	sed -n "/\s/p" prospacecheck.ali >spacefiles.ali
	echo -n "
	#!/bin/bash
	bspace=\`echo \\"\$1\\" | sed \\"s/\s/_/g\\"\` 
	mv \\"\$1\\" \\"\$bspace\\"" >rename.bash
	cat prospacefiles.ali | grep "pdb" | parallel -j 0 --no-notice --eta bash rename.bash {}
	cat prospacefiles.ali | grep "txt" | parallel -j 0 --no-notice --eta bash rename.bash {}
	rm rename.bash spacefiles.ali
else
	:
fi
rm prospacecheck.ali
ls -1 *.pdb >protein_list.txt
sed -i "s/.pdb//g" protein_list.txt
while read -r l
do
	reftxt=`ls "$l".txt  2>/dev/null`
	if [ -n "$reftxt" ]
	then
		:
	else
		rm protein_list.txt; 
		echo -e "Configuration file not found for "$l" protein in the "$RECEPTOR"/\\n Please Check and start the process again\\n\\n"
		exit
	fi
done <protein_list.txt
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clear
cd "$WORKING"
echo -n "
#-*- coding: utf-8 -*-
import sys
asd=open(sys.argv[1],'r')
INPUT=asd.readlines()
asd.close()
check='NO'
asd=open(sys.argv[1],'w')
for f in INPUT:
	if check=='NO':
		if f[0:4] == 'ATOM' and f[21] == 'P':
			asd.write('TER\\n')
			check='YES'
	asd.write(f)" >"$WORKING"/reedit.py

while read -r l
do
	clear
	cd "$WORKING"
	mkdir "$l";cd "$l";mkdir Results;cd Results; mkdir docked_pdb;cd ../
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening using ZDOCK Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	cd Results; mkdir raw_log; cd ../
	echo -n "
# -*- coding: utf-8 -*-
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
asd=open(sys.argv[2],'r')
FILE2=asd.readlines()
asd.close()
CHAIN_temp=[]
for f in FILE2:
	CHAIN_temp.append(str(f.strip().split()[1]))
ACTIVE={}
for f in sorted(set(CHAIN_temp)):
	ACTIVE[f]=[]
for f in FILE2:
	for ff in ACTIVE.keys():
		if f.strip().split()[1] == ff:
			ACTIVE[ff].append(f.strip().split()[0])
for f in FILE1:
	if f[0:6].strip() != 'ATOM':
			print(f.strip('\\n'))
	for ff in ACTIVE.keys():
		if f[0:6].strip() == 'ATOM' and f[21] == ff:
			if f[22:26].strip() in ACTIVE[ff]:
				print(f.strip('\\n'))
			else:
				print(f[:55]+'19'+f[57:].strip('\\n'))" >active_marking.py
	RECEPNAME="$l".pdb; ACTIVESITE="$l".txt
	echo -n "
	SCORE="$SCORE"
	if [ "$SCORE" == 'YES' ]
	then
		"$ZRANK"/zrank \\"\$1\\" 1 2000
		str=\`sort -n +1 \\"\$1\\".zr.out | head -n 1 | cut -f1\`
		zrscore=\`sort -n +1 \\"\$1\\".zr.out | head -n 1 | cut -f2\`
		temp=\`echo \\"\$str\\"+5 | bc\`
		zscore=\`sed -n \\"\$temp\\"p \\"\$1\\"|cut -f7\`
		"$ZDOCK"/create.pl \\"\$1\\" \\"\$str\\"
		cat complex.\\"\$str\\".pdb >../Results/docked_pdb/\${1%.out}.pdb; 
		echo -e \\"\${1%.out}\\t\$zscore\\t\$zrscore\\" >>"$WORKING"/"$l"/Results/output.txt
		mv \\"\$1\\" "$WORKING"/"$l"/Results/raw_log/
		mv \\"\$1\\".zr.out "$WORKING"/"$l"/Results/raw_log/
	else
		"$ZDOCK"/create.pl \\"\$1\\" 1
		zscore=\`sed -n '6p' \\"\$1\\"|cut -f7\`
		cat complex.1.pdb >../Results/docked_pdb/\${1%.out}.pdb; 
		echo -e \\"\${1%.out}\\t\$zscore\\" >>"$WORKING"/"$l"/Results/output.txt
		mv \\"\$1\\" "$WORKING"/"$l"/Results/raw_log/
	fi
	ls -1 | parallel \\"rm {}\\"
	" >score.bash
	echo -e "~~~~~~ Running ZDock for "$l"~~~~~~~~~"
	ls -1U "$PEPTIDE"/| grep "pdb" | parallel --eta -j "$joobs" "cd "$WORKING"/"$l"; mkdir {.}; cd {.};cp "$PEPTIDE"/{} . ;cp "$RECEPTOR"/"$RECEPNAME" .; cp "$RECEPTOR"/"$ACTIVESITE" .; cp "$ZDOCK"/uniCHARMM .;cp "$WORKING"/"$l"/score.bash .; cp "$ZDOCK"/create_lig .; "$HBPLUSDIR"/hbplus "$RECEPNAME" -o &>>"$WORKING"/log.txt; mv ${RECEPNAME%.pdb}.h ${RECEPNAME%.pdb}123.pdb ; "$HBPLUSDIR"/hbplus {.}.pdb -o &>>"$WORKING"/log.txt; mv {.}.h {.}123.pdb;"$ZDOCK"/mark_sur ${RECEPNAME%.pdb}123.pdb ${RECEPNAME%.pdb}_m.pdb &>>"$WORKING"/log.txt; "$ZDOCK"/mark_sur {.}123.pdb {.}_m.pdb &>>"$WORKING"/log.txt; python ../active_marking.py ${RECEPNAME%.pdb}_m.pdb "$ACTIVESITE" >${RECEPNAME%.pdb}_m_bl.pdb;"$ZDOCK"/zdock -R ${RECEPNAME%.pdb}_m_bl.pdb -L {.}_m.pdb -o {.}.out &>>"$WORKING"/log.txt;bash score.bash {.}.out;cd ../;rmdir {.}"
	cd "$WORKING"/"$l"/Results/;  
	if [ "$SCORE" == 'YES' ]
	then
		sort -k3n output.txt >sorted.txt; rm output.txt;sed -i "1i Peptide_Name\\tZDOCK_SCORE\\tZRANK_SCORE" sorted.txt; 
		echo -e "Top 10 results for "$l" screening:" >>"$WORKING"/summary.txt
		head -n 11 sorted.txt >>"$WORKING"/summary.txt
	else
		sort -k2nr output.txt >sorted.txt; rm output.txt;sed -i "1i Peptide_Name\\tZDOCK_SCORE" sorted.txt; 
		echo -e "Top 10 results for "$l" screening:" >>"$WORKING"/summary.txt
		head -n 11 sorted.txt >>"$WORKING"/summary.txt
	fi
	#~~~~~~ Rediting adding TER between receptor and peptide ~~~~~~~~~~
	cd "$WORKING"/"$l"/Results/docked_pdb;
	ls -1U | grep "pdb" | parallel -j "$joobs" "python "$WORKING"/reedit.py {}; sed -i '/^HEADER/d;/^REMARK/d' {}"
	cd "$WORKING"/"$l"; rm score.bash active_marking.py
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening using ZDock End time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
	cd "$WORKING"/"$l"
	#~~~~ flags for flexpepdock -- prepack ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database
-flexpep_prepack
-ignore_zero_occupancy false
-ex1
-ex2aro
-out:suffix _prepack
-out:file:scorefile score_prepack.sc" >"$WORKING"/"$l"/flags_prepack
	#~~~~ flags for flexpepdock -- refine ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database 
-scorefile score.sc 
-min_receptor_bb 
-lowres_preoptimize 
-pep_refine 
-flexpep_score_only
-nstruct 1 
-ex1 
-ex2aro 
-use_input_sc 
-out:suffix _refine 
-out:file:scorefile score_refine.sc" >"$WORKING"/"$l"/flags_refine
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	clear
	echo -e "#~~~~~~~ Running Flexible Refinement using: FlexpepDock for "$l"~~~~~~~~~#"
	cd "$WORKING"/"$l"/Results; mkdir refine;cd refine
	#~~~~ Residue number re-arrange ~~~~~~~~~~~
	echo -n "
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
LIST=[]
PEP=[]
RECEPTOR=[]
for f in FILE1:
	if f[0:4] == 'ATOM' and f[21] == 'P':
		PEP.append(f.strip('\\n'))
		LIST.append(int(f[22:26].strip()))
	if f[0:4] == 'ATOM' and f[21] != 'P':
		RECEPTOR.append(f.strip('\\n'))
for f in RECEPTOR:
	print(f)
print('TER')
for f in set(sorted(LIST)):
	for ff in PEP:
		if int(ff[22:26].strip()) == f:
			print(ff)" >renumber.py
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	echo -n "
#!/bin/bash
if [ -s \\"\$1\\" ]
then
	rm \\"\${1%_prepack_0001.pdb}.pdb\\"; mv \\"\$1\\" \\"\${1%_prepack_0001.pdb}.pdb\\" 
	mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s \\"\${1%_prepack_0001.pdb}.pdb\\" @flags_refine &>>"$WORKING"/log.txt
	bestrefine=\`grep \\"^SCORE\\" score_refine.sc | sed \\"1d\\" | sort -k2n | head -n 1\`
	modelnum=\`echo \\"\$bestrefine\\" | awk '{print NF}'\`
	refinemodel=\`echo \\"\$bestrefine\\" | awk -v ll=\\"\$modelnum\\" '{print \$ll}'\`
	if [ -s \\"\$refinemodel\\".pdb ]
	then
		mv \\"\$refinemodel\\".pdb "$WORKING"/"$l"/Results/refine/\\"\${1%_prepack_0001.pdb}.pdb\\"
		repos=\\"\\";a=1;for f in \$(grep \\"^SCORE\\" score_refine.sc | sed -n \\"1p\\" | sed \\"s/\\t/,/g\\");do if [ \\"\$f\\" == 'reweighted_sc' ];then repos=\\"\$a\\";break;fi;a=\`expr \$a + 1\`;done
		echo -e \\"\\"\${1%_prepack_0001.pdb}\\"\\t\$(grep \${1%_prepack_0001.pdb} "$WORKING"/"$l"/Results/sorted.txt | cut -f2-)\\t\$(echo \\"\$bestrefine\\" | awk '{print \$2}')\\t\$(echo \\"\$bestrefine\\" | awk -v ll=\\"\$repos\\" '{print \$ll}')\\" >>"$WORKING"/"$l"/Results/Refine_score.txt
	else
		echo \\"\$1 Error during FlexpepDock Refinement\\" >>"$WORKING"/"$l"/Results/refine_error.txt
	fi
else
	echo \\"\$1 Error during FlexpepDock Prepack\\" >>"$WORKING"/"$l"/Results/refine_error.txt
fi
ls -1U | parallel -j 1 rm {}; cd ..; rmdir \${1%_prepack_0001.pdb}" >ROSE_check.bash
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	ls -1U "$WORKING"/"$l"/Results/docked_pdb/| grep "pdb" | parallel -j 1 --eta "mkdir {.}; cd {.}; python ../renumber.py "$WORKING"/"$l"/Results/docked_pdb/{} >{};cp "$WORKING"/"$l"/flags_prepack .; cp "$WORKING"/"$l"/flags_refine .;mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s {} @flags_prepack &>>"$WORKING"/log.txt; bash ../ROSE_check.bash {.}_prepack_0001.pdb"
	cd "$WORKING"/"$l"/Results/
	if [ -s refine_error.txt ]
	then
		echo "~~Error occured during FlexpepDock Refinement!~~"
	else
		if [ "$SCORE" == "YES" ]
		then
			head -n 1 sorted.txt | sed "s/$/\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score/g" >Refine_sorted.txt;sort -k4n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;	
			echo -e "Top 10 results for "$l" screening after flexible refinement:" >>"$WORKING"/summary.txt
			head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
		else
			head -n 1 sorted.txt | sed "s/$/\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score/g" >Refine_sorted.txt;sort -k3n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;
			echo -e "Top 10 results for "$l" screening after flexible refinement:" >>"$WORKING"/summary.txt
			head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
		fi
	fi
	cd "$WORKING"/"$l"/Results/refine ; rm ROSE_check.bash renumber.py
	cd "$WORKING"/"$l"/; rm flags_prepack flags_refine
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement end time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		BASHSCRIPT+='''
done <"$RECEPTOR"/protein_list.txt
cd "$WORKING"; rm log.txt reedit.py 
rm "$RECEPTOR"/protein_list.txt
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide screening End time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		bash_script=open('PepVs.bash','w')
		bash_script.write(BASHSCRIPT)
		bash_script.close()
		root.destroy()
	#~~~~ ZDOCK script: end
	Button(zdock_vs,text="Hit Run!",bg="black",fg="white",font=("Times",15,"bold","underline"),width=10,height=3,command=print_zdock_script).grid(row=10,column=0,columnspan=2,sticky=E+W+N+S)
#~~~ ZDOCK: end


#~~~~ AutoDock CrankPep: start
def run_adcp():
	docktools.destroy()
	adcp_vs=Toplevel(root)
	global CWD
	Label(adcp_vs,text="AutoDock CrankPep: Inputs",bg="white",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=0,column=0,columnspan=2,sticky=E+W+N+S)
	Label(adcp_vs,bg="white",text="Enter the peptide sequence file:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=1,column=0,sticky=E+W+N+S)
	def get_peptide_dir():
		filetemp=tkFileDialog.askopenfilename(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/peptide",title="Enter the peptide sequence file",parent=adcp_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=adcp_vs)
				return
			else:
				if os.path.isfile(filetemp):
					global PEPTIDE
					#global INPUTPEP
					PEPTIDE=filetemp
					#INPUTPEP=os.path.split(filetemp)[1]
				else:
					tkMessageBox.showinfo("Warning!","File not found in the directory path!",parent=adcp_vs)
					return
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=adcp_vs)
			return
	Button(adcp_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_peptide_dir).grid(row=1,column=1,sticky=E+W+N+S)
	Label(adcp_vs,bg="white",text="Enter the receptor structures:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=2,column=0,sticky=E+W+N+S)
	def get_receptor_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/adcp_recep",title="Enter the receptor structures directory",parent=adcp_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=adcp_vs)
				return
			else:
				global RECEPTOR
				RECEPTOR=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=adcp_vs)
			return
	Button(adcp_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_receptor_dir).grid(row=2,column=1,sticky=E+W+N+S)
	Label(adcp_vs,bg="white",text="Enter the working directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=3,column=0,sticky=E+W+N+S)
	def get_working_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/working",title="Enter the working directory",parent=adcp_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=adcp_vs)
				return
			else:
				os.chdir(filetemp)
				zxc=os.listdir('.')
				if zxc:
					tkMessageBox.showinfo("Warning!","Working directory is not empty!",parent=adcp_vs)
					return
				else:
					global WORKING
					WORKING=filetemp
					os.chdir(CWD)
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=adcp_vs)
			return
	Button(adcp_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_working_dir).grid(row=3,column=1,sticky=E+W+N+S)
	#~~~~~~~~~~~~~~ Number of CPU calculation start
	Ncpu=multiprocessing.cpu_count()
	Label(adcp_vs,bg="white",text=str(Ncpu)+" number of CPU processors \n detected in your system",relief=SOLID,font=("Times",15,'bold'),width=30,height=3,justify=CENTER).grid(row=4,column=0,columnspan=2,sticky=E+W+N+S)
	Label(adcp_vs,bg="white",text="Enter the number of CPU \n for running jobs in parallel :",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=5,column=0,sticky=W+E+N+S)
	global Numcpu
	Numcpu=StringVar()
	Numcpu.set(Ncpu)
	joobs=int(Numcpu.get())
	if len(Numcpu.get()) > 0:
		Label(adcp_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=10,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
	Entry(adcp_vs,bd=5,textvariable=Numcpu,font=("Times",15,'bold'),justify=CENTER).grid(row=5,column=1,sticky=W+E+N+S)
	def checkback(*args):
		for f in Numcpu.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=adcp_vs)
				return
		global joobs
		joobs=0
		if len(Numcpu.get()) > 0:
			if int(Numcpu.get()) > Ncpu or int(Numcpu.get()) == 0 :
				tkMessageBox.showinfo("Warning","Please provide the values less than "+str(Ncpu)+"!",parent=adcp_vs)
				return
			else:
				Label(adcp_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=10,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
				joobs=int(Numcpu.get())
		else:
			Label(adcp_vs,bg="white",text= "0 Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=6,column=0,columnspan=2,sticky=W+E+N+S)
	Numcpu.trace('w',checkback)
	Label(adcp_vs,bg="white",text="Enter the number of replicas:",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=7,column=0,sticky=W+E+N+S)
	global replica
	replica=StringVar()
	replica.set("50")
	global REPLICA
	REPLICA=50
	Entry(adcp_vs,bd=5,textvariable=replica,font=("Times",15,"bold"),justify=CENTER).grid(row=7,column=1,sticky=W+E+N+S)
	def replicacheck(*args):
		for f in replica.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=adcp_vs)
				return
		if len(replica.get()) > 0:
			global REPLICA
			REPLICA=int(replica.get())
		else:
			tkMessageBox.showinfo("Warning","Please provide the values",parent=adcp_vs)
			return
	replica.trace('w',replicacheck)
	Label(adcp_vs,bg="white",text="Enter the max steps for \none replica:",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=8,column=0,sticky=W+E+N+S)
	global maxsteps
	maxsteps=StringVar()
	maxsteps.set("2500000")
	global MAXSTEPS
	MAXSTEPS=2500000
	Entry(adcp_vs,bd=5,textvariable=maxsteps,font=("Times",15,"bold"),justify=CENTER).grid(row=8,column=1,sticky=W+E+N+S)
	def maxstepscheck(*args):
		for f in maxsteps.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=adcp_vs)
				return
		if len(maxsteps.get()) > 0:
			global MAXSTEPS
			MAXSTEPS=int(maxsteps.get())
		else:
			tkMessageBox.showinfo("Warning","Please provide the values",parent=adcp_vs)
			return
	maxsteps.trace('w',maxstepscheck)
	#~~~~~~~~ FlexpepDock start
	Label(adcp_vs,bg="white",text= "Do you want to run Flexible \n refinement using FlexPepDock?",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=9,column=0,sticky=W+E+N+S)
	FLEXREF_check=IntVar()
	Checkbutton(adcp_vs,variable=FLEXREF_check,onvalue=1,offvalue=0,bg="white",font=("Times",10,"bold"),relief=SOLID,width=10,height=3).grid(row=9,column=1,sticky=E+W+N+S)	
	def flexref_check(*args):
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning","FlexPepDock path not specified!",parent=adcp_vs)
				return
	FLEXREF_check.trace('w',flexref_check)
	#~~~~~ FlexPepDock end
	#~~~~ ADCP script : start
	def print_adcp_script():
		global RANKALL
		if not ADFRROOT:
			tkMessageBox.showinfo("Warning!","ADFR directory not specified!",parent=adcp_vs)
			return
		if PARALLEL_check.get() == 0:
			tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=adcp_vs)
			return
		if not PEPTIDE:
			tkMessageBox.showinfo("Warning!","The peptide directory not specified!",parent=adcp_vs)
			return
		if not RECEPTOR:
			tkMessageBox.showinfo("Warning!","The Receptor directory not specified!",parent=adcp_vs)
			return
		if not WORKING:
			tkMessageBox.showinfo("Warning!","Working directory not specified!",parent=adcp_vs)
			return
		if not joobs:
			tkMessageBox.showinfo("Warning!","Number of Jobs to run in parallel not specified!",parent=adcp_vs)
			return
		if not MAXSTEPS:
			tkMessageBox.showinfo("Warning!","Maximum steps per replica not specified!",parent=adcp_vs)
			return
		if not REPLICA:
			tkMessageBox.showinfo("Warning!","Number of Replica runs not specified!",parent=adcp_vs)
			return
		os.chdir(WORKING)
		BASHSCRIPT='''
#!/bin/bash
PEPTIDE="%s"
RECEPTOR="%s"
WORKING="%s"
REPLICA="%d"
MAXSTEPS="%d"
joobs="%d"
RANKALL="%s"
ADFRROOT="%s"
''' %(PEPTIDE,RECEPTOR,WORKING,REPLICA,MAXSTEPS,joobs,RANKALL,ADFRROOT)
		if FLEXREF_check.get() == 1:
			if not FLEXPEPDOCK:
				tkMessageBox.showinfo("Warning!","FlexPepDock not specified!",parent=adcp_vs)
				return
			BASHSCRIPT+='\nROSETTA_DIR="'+'/'.join(FLEXPEPDOCK.split('/')[:-4])+'"'
		BASHSCRIPT+='''\n\n
echo -e "================================================================================"
echo -e "Peptide file: "$PEPTIDE""
echo -e "Receptor directory: "$RECEPTOR""
echo -e "Working directory: "$WORKING""
echo -e "Peptide Docking tool: AutoDock CrankPep"
echo -e "Number of Replica: "$REPLICA""
echo -e "Maximum steps per replica: "$MAXSTEPS""
echo -e "Number of jobs to run in parallel:"$joobs""
echo -e "Consider top 10 for each peptide: "$RANKALL""'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
echo -e "Rosetta directory:"$ROSETTA_DIR""
echo -e "Flexible refinement using FlexPepDock: YES"'''
		BASHSCRIPT+='''
echo -e "================================================================================"
echo -e "Please enter [1] to accept the input [2] to quit"
i=1
while [ "$i" -ge 0 ]
do
	read -ep ">>>" check
	if [ "$check" == 1 ]
	then
		:
		break
	elif [ "$check" == 2 ]
	then
		exit
	else
		echo "Wrong input! Enter again"
	fi
done
cd "$WORKING"
echo -e "Peptide file: "$PEPTIDE"\\nReceptor directory: "$RECEPTOR"\\nWorking directory: "$WORKING"\\nPeptide Docking tool: AutoDock CrankPep\\nNumber of Replica: "$REPLICA"\\nMaximum steps per replica: "$MAXSTEPS"\\nNumber of jobs to run in parallel:"$joobs"\\nConsider top 10 for each peptide: "$RANKALL"" >>"$WORKING"/summary.txt

echo -n "
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()

for f in FILE1:
	print(f.strip('\\n').lower())
#	#~~~ Shuffled: AsAgHiK
#	a=0
#	temp=""
#	for ff in f.strip('\\n'):
#		if a==0:
#			temp+=ff.upper()
#			a=1
#		elif a==1:
#			temp+=ff.lower()
#			a=0
#	print(temp)
#	#~~~~ shuffled" >pep_lettering.py
python pep_lettering.py "$PEPTIDE" >peptide_list.txt
echo -e "Total number of peptide sequence: $(cat peptide_list.txt | wc -l)" >>"$WORKING"/summary.txt
ls -1U "$RECEPTOR"/ | grep 'trg' | sed "s/.trg//" >protein_list.txt
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Virtual Screening Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
while read -r l;
do
	clear
	echo -e "~~~ Running Peptide Virtual Screening for "$l" ~~~~~~~~~~"
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Virtual Screening for "$l" Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	cd "$WORKING"
	mkdir "$l";cd "$l";mkdir Results docked_files;cd Results;mkdir docked_pdb;cd ../docked_files;cp "$RECEPTOR"/"$l".trg .;cp "$WORKING"/peptide_list.txt .
	unzip "$l".trg &>/dev/null;cd "$l";cut -c-66 "$l".pdbqt >../"$l".pdb;for f in `ls -1`;do rm "$f";done;cd ..;rmdir "$l"
	echo -n "
#!/bin/bash
for f in \`ls -1\`
do
	rm \\"\$f\\"
done
cd ../;rmdir \$1" >del.bash
	echo -n "
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
LIST=[]
for f in FILE1:
	if f[0:4] == 'ATOM':
		LIST.append(int(f[22:26].strip()))
PEP=[]
for f in set(sorted(LIST)):
	for ff in FILE1:
		if ff[0:4].strip() == 'ATOM' and int(ff[22:26].strip()) == f:
			PEP.append(ff.strip('\\n'))
for f in PEP:
	print(f[0:11]+'  '+f[12:16].strip(' ').ljust(4)+f[17:21]+'P'+f[22:75]+'  '+f[76:78].strip(' ').ljust(2))" >pdb_reorder.py
	echo -n "
#!/bin/bash
RANKALL="$RANKALL"
if [ -s \\"\$1\\"_dock_ranked_1.pdb ]
then
	if [ \\"\$RANKALL\\" == \\"YES\\" ]
	then
		for f in *_ranked_*.pdb
		do
			cat ../"$l".pdb >"$WORKING"/"$l"/Results/docked_pdb/\${f/_dock_ranked/}
			python ../pdb_reorder.py \\"\$f\\" >>"$WORKING"/"$l"/Results/docked_pdb/\${f/_dock_ranked/}
		done
	elif [ \\"\$RANKALL\\" == \\"NO\\" ]
	then
		cat ../"$l".pdb >"$WORKING"/"$l"/Results/docked_pdb/\\"\$1\\".pdb
		python ../pdb_reorder.py \\"\$1\\"_dock_ranked_1.pdb >>"$WORKING"/"$l"/Results/docked_pdb/\\"\$1\\".pdb
	fi
	#~~~~~~~ score parsing
	if [ \\"\$RANKALL\\" == \\"YES\\" ]
	then
		while read -r l
		do
			echo -e \\"\$1_\$(echo \\"\$l\\" | awk '{print \$1}')\\t\$(echo \\"\$l\\" | awk '{print \$2}')\\" >>"$WORKING"/"$l"/Results/adcp_score.txt	
		done <<<\$(sed -n \\"/-----+/,\$ p\\" \\"\$1\\"_log.txt | grep -v '\-\-\-\-\-\+' | head -n 10)
	else
		echo -e \\"\$1\\t\$(sed -n \\"/-----+/,\$ p\\" \\"\$1\\"_log.txt | grep -v '\-\-\-\-\-\+' | head -n 1 | awk '{print \$2}')\\" >>"$WORKING"/"$l"/Results/adcp_score.txt
	fi
	bash ../del.bash \\"\$1\\"
else
	echo -e \\"Error occured for \\"\$1\\" docking with "$l"\\" >>"$WORKING"/summary.txt
	bash ../del.bash \\"\$1\\"
fi
" >adcp_check.bash
	cat peptide_list.txt | parallel -j 1 --eta "mkdir {}; cd {};cp ../"$l".trg .;"$ADFRROOT"/bin/adcp -t "$l".trg -s {} -N "$REPLICA" -n "$MAXSTEPS" -S 10 -o {}_dock -c "$joobs" >>{}_log.txt; bash ../adcp_check.bash {}"
	cd "$WORKING"/"$l"/docked_files;rm adcp_check.bash peptide_list.txt del.bash "$l".trg
	cd "$WORKING"/"$l"/Results
	sort -k2n adcp_score.txt >sorted.txt; rm adcp_score.txt
	sed -i "1i Peptide_Name\\tAffinity" sorted.txt
	echo -e "Top 10 results for "$l" screening:" >>"$WORKING"/summary.txt
	head -n 11 sorted.txt >>"$WORKING"/summary.txt
	cd "$WORKING"/"$l"/docked_files;rm "$l".pdb pdb_reorder.py; cd ..; rmdir docked_files
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Virtual Screening for "$l" End time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		if FLEXREF_check.get() == 1:
			BASHSCRIPT+='''
	cd "$WORKING"/"$l"
	#~~~~ flags for flexpepdock -- prepack ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database
-flexpep_prepack
-ignore_zero_occupancy false
-ex1
-ex2aro
-out:suffix _prepack
-out:file:scorefile score_prepack.sc" >"$WORKING"/"$l"/flags_prepack
	#~~~~ flags for flexpepdock -- refine ~~~~~~~~~~#
	echo -n "
-database "$ROSETTA_DIR"/main/database 
-scorefile score.sc 
-min_receptor_bb 
-lowres_preoptimize 
-pep_refine 
-flexpep_score_only
-nstruct 1 
-ex1 
-ex2aro 
-use_input_sc 
-out:suffix _refine 
-out:file:scorefile score_refine.sc" >"$WORKING"/"$l"/flags_refine
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	clear
	echo -e "#~~~~~~~ Running Flexible Refinement using: FlexpepDock for "$l"~~~~~~~~~#"
	cd "$WORKING"/"$l"/Results; mkdir refine;cd refine
	echo -n "
#!/bin/bash
if [ -s \\"\$1\\" ]
then
	rm \\"\${1%_prepack_0001.pdb}.pdb\\"; mv \\"\$1\\" \\"\${1%_prepack_0001.pdb}.pdb\\" 
	mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s \\"\${1%_prepack_0001.pdb}.pdb\\" @flags_refine &>>"$WORKING"/log.txt
	bestrefine=\`grep \\"^SCORE\\" score_refine.sc | sed \\"1d\\" | sort -k2n | head -n 1\`
	modelnum=\`echo \\"\$bestrefine\\" | awk '{print NF}'\`
	refinemodel=\`echo \\"\$bestrefine\\" | awk -v ll=\\"\$modelnum\\" '{print \$ll}'\`
	if [ -s \\"\$refinemodel\\".pdb ]
	then
		mv \\"\$refinemodel\\".pdb "$WORKING"/"$l"/Results/refine/\\"\${1%_prepack_0001.pdb}.pdb\\"
		repos=\\"\\";a=1;for f in \$(grep \\"^SCORE\\" score_refine.sc | sed -n \\"1p\\" | sed \\"s/\\t/,/g\\");do if [ \\"\$f\\" == 'reweighted_sc' ];then repos=\\"\$a\\";break;fi;a=\`expr \$a + 1\`;done
		echo -e \\"\\"\${1%_prepack_0001.pdb}\\"\\t\$(grep \${1%_prepack_0001.pdb} "$WORKING"/"$l"/Results/sorted.txt | cut -f2-)\\t\$(echo \\"\$bestrefine\\" | awk '{print \$2}')\\t\$(echo \\"\$bestrefine\\" | awk -v ll=\\"\$repos\\" '{print \$ll}')\\" >>"$WORKING"/"$l"/Results/Refine_score.txt
	else
		echo \\"\$1 Error during FlexpepDock Refinement\\" >>"$WORKING"/"$l"/Results/refine_error.txt
	fi
else
	echo \\"\$1 Error during FlexpepDock Prepack\\" >>"$WORKING"/"$l"/Results/refine_error.txt
fi
ls -1U | parallel -j 1 rm {}; cd ..; rmdir \${1%_prepack_0001.pdb}" >ROSE_check.bash
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
	ls -1U "$WORKING"/"$l"/Results/docked_pdb/| grep "pdb" | parallel -j 1 --eta "mkdir {.}; cd {.}; cp "$WORKING"/"$l"/Results/docked_pdb/{} .;cp "$WORKING"/"$l"/flags_prepack .; cp "$WORKING"/"$l"/flags_refine .;mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s {} @flags_prepack &>>"$WORKING"/log.txt; bash ../ROSE_check.bash {.}_prepack_0001.pdb"
	cd "$WORKING"/"$l"/Results/
	if [ -s refine_error.txt ]
	then
		echo "~~Error occured during FlexpepDock Refinement!~~"
	else
		head -n 1 sorted.txt | sed "s/$/\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score/g" >Refine_sorted.txt; # Header alone
		sort -k3n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;	
		echo -e "Top 10 results with refinement for "$l" screening:" >>"$WORKING"/summary.txt
		head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
	fi
	cd "$WORKING"/"$l"/Results/refine ; rm ROSE_check.bash
	cd "$WORKING"/"$l"/; rm flags_prepack flags_refine
	time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement end time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		BASHSCRIPT+='''
done <protein_list.txt
cd "$WORKING"; rm pep_lettering.py protein_list.txt peptide_list.txt; if [ -s log.txt ];then rm log.txt;fi
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Virtual Screening End time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
		bash_script=open('PepVs.bash','w')
		bash_script.write(BASHSCRIPT)
		bash_script.close()
		root.destroy()
	#~~~~ ADCP script : end
	Button(adcp_vs,text="Hit Run!",bg="black",fg="white",font=("Times",15,"bold","underline"),width=10,height=3,command=print_adcp_script).grid(row=10,column=0,columnspan=2,sticky=E+W+N+S)


#~~~~ AutoDock CrankPep: end


#~~~~~ FlexPepDock: start
def run_flexpepdock():
	docktools.destroy()
	flexpep_vs=Toplevel(root)
	global CWD
	Label(flexpep_vs,text="FlexPepDock: Inputs",bg="white",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=0,column=0,columnspan=2,sticky=E+W+N+S)
	Label(flexpep_vs,bg="white",text="Enter the protein-peptide \nstructures directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=1,column=0,sticky=E+W+N+S)
	def get_receptor_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/receptor",title="Enter the receptor structures directory",parent=flexpep_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=flexpep_vs)
				return
			else:
				global PEPTIDE
				PEPTIDE=filetemp
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=flexpep_vs)
			return
	Button(flexpep_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_receptor_dir).grid(row=1,column=1,sticky=E+W+N+S)
	Label(flexpep_vs,bg="white",text="Enter the working directory:",font=("Times",15,"bold"),relief=SOLID,width=30,height=3).grid(row=2,column=0,sticky=E+W+N+S)
	def get_working_dir():
		filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/pep_docking/gui/working",title="Enter the working directory",parent=flexpep_vs)
		if filetemp:
			if ' ' in filetemp:
				tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=flexpep_vs)
				return
			else:
				os.chdir(filetemp)
				zxc=os.listdir('.')
				if zxc:
					tkMessageBox.showinfo("Warning!","Working directory is not empty!",parent=flexpep_vs)
					return
				else:
					global WORKING
					WORKING=filetemp
					os.chdir(CWD)
		else:	
			tkMessageBox.showinfo("Warning!","Directory not specified!",parent=flexpep_vs)
			return
	Button(flexpep_vs,text="Open",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=10,height=3,command=get_working_dir).grid(row=2,column=1,sticky=E+W+N+S)
	#~~~~~~~~~~~~~~ Number of CPU calculation start
	Ncpu=multiprocessing.cpu_count()
	Label(flexpep_vs,bg="white",text=str(Ncpu)+" number of CPU processors \n detected in your system",relief=SOLID,font=("Times",15,'bold'),width=30,height=3,justify=CENTER).grid(row=3,column=0,columnspan=2,sticky=E+W+N+S)
	Label(flexpep_vs,bg="white",text="Enter the number of CPU \n for running jobs in parallel :",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=4,column=0,sticky=W+E+N+S)
	global Numcpu
	Numcpu=StringVar()
	Numcpu.set(Ncpu)
	joobs=int(Numcpu.get())
	if len(Numcpu.get()) > 0:
		Label(flexpep_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=10,height=2,justify=CENTER).grid(row=5,column=0,columnspan=2,sticky=W+E+N+S)		
	Entry(flexpep_vs,bd=5,textvariable=Numcpu,font=("Times",15,'bold'),justify=CENTER).grid(row=4,column=1,sticky=W+E+N+S)
	def checkback(*args):
		for f in Numcpu.get():
			if f not in '1234567890' :
				tkMessageBox.showinfo("Warning","Please provide the integer Values!",parent=flexpep_vs)
				return
		global joobs
		joobs=0
		if len(Numcpu.get()) > 0:
			if int(Numcpu.get()) > Ncpu or int(Numcpu.get()) == 0 :
				tkMessageBox.showinfo("Warning","Please provide the values less than "+str(Ncpu)+"!",parent=flexpep_vs)
				return
			else:
				Label(flexpep_vs,bg="white",text= Numcpu.get()+" Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=10,height=2,justify=CENTER).grid(row=5,column=0,columnspan=2,sticky=W+E+N+S)
				joobs=int(Numcpu.get())
		else:
			Label(flexpep_vs,bg="white",text= "0 Jobs will run in parallel",relief=SOLID,font=("Times",15,'bold'),width=30,height=2,justify=CENTER).grid(row=5,column=0,columnspan=2,sticky=W+E+N+S)
	Numcpu.trace('w',checkback)
	def print_flexpep_script():
		if not FLEXPEPDOCK:
			tkMessageBox.showinfo("Warning!","FlexPepDock not found!",parent=flexpep_vs)
			return
		if not PEPTIDE:
			tkMessageBox.showinfo("Warning!","Protein-Peptide complex directory not specified!",parent=flexpep_vs)
			return
		if not WORKING:
			tkMessageBox.showinfo("Warning!","Receptor directory not specified!",parent=flexpep_vs)
			return
		if not joobs:
			tkMessageBox.showinfo("Warning!","Number of Jobs to run in parallel not specified!",parent=flexpep_vs)
			return
		if PARALLEL_check.get() == 0:
			tkMessageBox.showinfo("Warning!","GNU Parallel not found!",parent=flexpep_vs)
			return
		os.chdir(WORKING)
		BASHSCRIPT='''
#!/bin/bash
PEPTIDE="%s"
WORKING="%s" ''' %(PEPTIDE,WORKING)
		BASHSCRIPT+='\nROSETTA_DIR="'+'/'.join(FLEXPEPDOCK.split('/')[:-4])+'"'
		BASHSCRIPT+='\njoobs=%d' %(joobs)
		BASHSCRIPT+='''\n\n
echo -e "================================================================================"
echo -e "Protein-Peptide structures directory: "$PEPTIDE""
echo -e "Working directory: "$WORKING""
echo -e "Number of jobs to run in parallel:"$joobs""
echo -e "Flexbile Refinement using FlexPepDock: YES"
echo -e "Rosetta directory:"$ROSETTA_DIR""
echo -e "================================================================================"
echo -e "Please enter [1] to accept the input [2] to quit"
i=1
while [ "$i" -ge 0 ]
do
	read -ep ">>>" check
	if [ "$check" == 1 ]
	then
		:
		break
	elif [ "$check" == 2 ]
	then
		exit
	else
		echo "Wrong input! Enter again"
	fi
done
cd "$WORKING"
echo -e "Protein-Peptide structures directory: "$PEPTIDE"\\nWorking directory: "$WORKING"\\nFlexible Refinement using FlexPepDock: YES\\nNo. of CPU's for parallel:"$joobs"" >>"$WORKING"/summary.txt'''
		BASHSCRIPT+='''
cd "$WORKING"; mkdir Results
#~~~~ flags for flexpepdock -- prepack ~~~~~~~~~~#
echo -n "
-database "$ROSETTA_DIR"/main/database
-flexpep_prepack
-ignore_zero_occupancy false
-ex1
-ex2aro
-out:suffix _prepack
-out:file:scorefile score_prepack.sc" >"$WORKING"/flags_prepack
#~~~~ flags for flexpepdock -- refine ~~~~~~~~~~#
echo -n "
-database "$ROSETTA_DIR"/main/database 
-scorefile score.sc 
-min_receptor_bb 
-lowres_preoptimize 
-pep_refine 
-flexpep_score_only
-nstruct 1 
-ex1 
-ex2aro 
-use_input_sc 
-out:suffix _refine 
-out:file:scorefile score_refine.sc" >"$WORKING"/flags_refine
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
clear
echo -e "#~~~~~~~ Running Flexible Refinement using: FlexpepDock~~~~~~~~~#"
cd "$WORKING"/Results; mkdir refine;cd refine
#~~~~ Residue number re-arrange ~~~~~~~~~~~
echo -n "
import sys
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()
LIST=[]
PEP=[]
RECEPTOR=[]
for f in FILE1:
	if f[0:4] == 'ATOM' and f[21] == 'P':
		PEP.append(f.strip('\\n'))
		LIST.append(int(f[22:26].strip()))
	if f[0:4] == 'ATOM' and f[21] != 'P':
		RECEPTOR.append(f.strip('\\n'))
for f in RECEPTOR:
	print(f)
print('TER')
for f in set(sorted(LIST)):
	for ff in PEP:
		if int(ff[22:26].strip()) == f:
			print(ff)" >renumber.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo -n "
#!/bin/bash
if [ -s \\"\$1\\" ]
then
	rm \\"\${1%_prepack_0001.pdb}.pdb\\"; mv \\"\$1\\" \\"\${1%_prepack_0001.pdb}.pdb\\" 
	mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s \\"\${1%_prepack_0001.pdb}.pdb\\" @flags_refine &>>"$WORKING"/log.txt
	bestrefine=\`grep \\"^SCORE\\" score_refine.sc | sed \\"1d\\" | sort -k2n | head -n 1\`
	modelnum=\`echo \\"\$bestrefine\\" | awk '{print NF}'\`
	refinemodel=\`echo \\"\$bestrefine\\" | awk -v ll=\\"\$modelnum\\" '{print \$ll}'\`
	if [ -s \\"\$refinemodel\\".pdb ]
	then
		mv \\"\$refinemodel\\".pdb "$WORKING"/Results/refine/\\"\${1%_prepack_0001.pdb}.pdb\\"
		repos=\\"\\";a=1;for f in \$(grep \\"^SCORE\\" score_refine.sc | sed -n \\"1p\\" | sed \\"s/\\t/,/g\\");do if [ \\"\$f\\" == 'reweighted_sc' ];then repos=\\"\$a\\";break;fi;a=\`expr \$a + 1\`;done
		echo -e \\"\\"\${1%_prepack_0001.pdb}\\"\\t\$(echo \\"\$bestrefine\\" | awk '{print \$2}')\\t\$(echo \\"\$bestrefine\\" | awk -v ll=\\"\$repos\\" '{print \$ll}')\\" >>"$WORKING"/Results/Refine_score.txt
	else
		echo \\"\$1 Error during FlexpepDock Refinement\\" >>"$WORKING"/Results/refine_error.txt
	fi
else
	echo \\"\$1 Error during FlexpepDock Prepack\\" >>"$WORKING"/Results/refine_error.txt
fi
ls -1U | parallel -j 1 rm {}; cd ..; rmdir \${1%_prepack_0001.pdb}" >ROSE_check.bash
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement Start time: "$time"\\n\\n" >>"$WORKING"/summary.txt
ls -1U "$PEPTIDE"/| grep "pdb" | parallel -j 1 --eta "mkdir {.}; cd {.}; python ../renumber.py "$PEPTIDE"/{} >{};cp "$WORKING"/flags_prepack .; cp "$WORKING"/flags_refine .;mpirun -np "$joobs" "$ROSETTA_DIR"/main/source/bin/FlexPepDocking.mpi.linuxgccrelease -s {} @flags_prepack &>>"$WORKING"/log.txt; bash ../ROSE_check.bash {.}_prepack_0001.pdb"
cd "$WORKING"/Results/
if [ -s refine_error.txt ]
then
	echo "~~Error occured during FlexpepDock Refinement!~~"
else
	sort -k2n Refine_score.txt >>Refine_sorted.txt; rm Refine_score.txt;
	sed -i "1i Complex_Name\\tFlexpepDock_Total_Score\\tFlexpepDock_reweighted_Score" Refine_sorted.txt
	echo -e "Top 10 results with refinement:" >>"$WORKING"/summary.txt
	head -n 11 Refine_sorted.txt >>"$WORKING"/summary.txt
fi
cd "$WORKING"/Results/refine ; rm ROSE_check.bash renumber.py
cd "$WORKING"/; rm flags_prepack flags_refine
time=`date +"%c"`; echo -e "\\n\\n\\nPeptide Flexible refinement end time: "$time"\\n\\n" >>"$WORKING"/summary.txt
'''
	#~~~~~ BASH script end
		bash_script=open('PepVs.bash','w')
		bash_script.write(BASHSCRIPT)
		bash_script.close()
		root.destroy()
	Button(flexpep_vs,text="Hit Run!",bg="black",fg="white",font=("Times",15,"bold","underline"),width=10,height=3,command=print_flexpep_script).grid(row=6,column=0,columnspan=2,sticky=E+W+N+S)
#~~~~~ FlexPepDock: end
#~~~~~ DOCKING TOOLS GUI: start~~~~~~~~~~
def dock_tools():
	global docktools
	docktools=Toplevel(root)
	Label(docktools,text="Select the prefered docking tool!",bg="white",font=("Times",15,"bold"),relief=SOLID,width=10,height=3).grid(row=0,column=0,columnspan=3,sticky=E+W+N+S)
	Button(docktools,text="AutoDock\nVina",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,width=10,height=3,command=run_vina).grid(row=1,column=0,sticky=E+W+N+S)
	Button(docktools,text="ZDOCK",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,width=10,height=3,command=run_zdock).grid(row=1,column=1,sticky=E+W+N+S)
	Button(docktools,text="AutoDock\nCrankPep",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,width=10,height=3,command=run_adcp).grid(row=1,column=2,sticky=E+W+N+S)
	Button(docktools,text="FlexPepDock",bg="gold",font=("Times",15,"bold","underline"),relief=RAISED,width=10,height=3,command=run_flexpepdock).grid(row=2,column=0,columnspan=3,sticky=E+W+N+S)



#~~~~~ DOCKING TOOLS GUI: end~~~~~~~~~~


#~~~ Peptide Virtual screening end
Label(root,text="PepVis",bg="white",font=("Times",30,"bold"),relief=SOLID,width=30,height=3).grid(row=0,column=0,columnspan=8,sticky=E+W+N+S)
#~~~~ variables for peptie modelling
PARALLEL_check=IntVar()
MGLROOT_check=IntVar()
MODPEP_check=IntVar()
PSIPRED_check=IntVar()
GRO_check=IntVar()


#~~ Check for installations start
#~~~ Minimization tools
Label(root,text="Minimization\nTools",bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=0,sticky=E+W+N+S)
#~~~ GNU Parallel start
try:
	asd=subprocess.Popen(['parallel','-h'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	PARALLEL_check.set(1)
except:
	PARALLEL_check.set(0)
#~~~ GNU Parallel end
#~~~ MGLTOOLS start
temp=os.environ.get('MGLROOT')
if temp:
	if os.path.isfile(temp+'/bin/pythonsh'):
		MGLROOT=temp
		MGLROOT_check.set(1)
	else:
		MGLROOT_check.set(0)
else:
	MGLROOT_check.set(0)
#~~~ MGLTOOLS end
#~~~~ MODPEP Start
def get_modpep_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/tools/modpep-v1.0",title="MODPEP Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/modpep'):
				global MODPEP
				MODPEP=filetemp
				config_writer('MODPEP',MODPEP)
				MODPEP_check.set(1)
			else:
				MODPEP_check.set(0)
				tkMessageBox.showinfo("Warning","Modpep not found in the specified directoy!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning!","Directory not specified!",parent=root)
		MODPEP_check.set(0)
		return

def modpep_check(*args):
	if MODPEP_check.get() == 1:
		Checkbutton(root,text="Modpep",variable=MODPEP_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=3,sticky=E+W+N+S)
MODPEP_check.trace('w',modpep_check)
#~~~~ MODPEP End
#~~~~ PSIPRED start
def get_psipred_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/tools/psipred",title="PSI-PRED Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/runpsipred'):
				global PSIPRED
				PSIPRED=filetemp
				config_writer('PSIPRED',PSIPRED)
				PSIPRED_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","runpsipred not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","File directory not specified!",parent=root)
		return
def psipred_check(*args):
	if PSIPRED_check.get() == 1:
		Checkbutton(root,text="PSI-PRED",variable=PSIPRED_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=4,sticky=E+W+N+S)
PSIPRED_check.trace('w',psipred_check)
#~~~~ PSIPRED end

#~~~~ GROMACS Start
def get_gromacs_prefix():
	top=Toplevel(root)
	top.title('GROMACS PREFIX')
	global GRO_temp
	GRO_temp=StringVar()
	Label(top,text="Enter the gromacs prefix:",font=("Times",10,"bold"),width=35,height=3).grid(row=0,column=0,sticky=E+W+N+S)
	Entry(top,textvariable=GRO_temp,bd=5,font=("Times",10,"bold"),justify=CENTER,width=10).grid(row=1,column=0,sticky=E+W+N+S)
	def gromacs_run_check():
#		global GRO_temp
		if GRO_temp.get():
			try:
				asd=subprocess.Popen([GRO_temp.get()],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
				output,error=asd.communicate()
				asd.wait()
				global GROMACS_PREFIX
				GROMACS_PREFIX=GRO_temp.get()
				config_writer('GROMACS_PREFIX',GROMACS_PREFIX)
				GRO_check.set(1)
				top.destroy()
			except:
				tkMessageBox.showinfo("Warning","Gromacs prefix not found!",parent=top)
				return
		else:
		
			tkMessageBox.showinfo("Warning","No input given!",parent=top)
			return
	Button(top,text="Enter",font=("Times",10,"bold","underline"),width=35,height=2,relief=RAISED,borderwidth=3,command=gromacs_run_check).grid(row=3,column=0,sticky=E+W+N+S)

def gromacs_check(*args):
	if GRO_check.get() == 1:
		Checkbutton(root,text="GROMACS",variable=GRO_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=5,sticky=E+W+N+S)
GRO_check.trace('w',gromacs_check)
#~~~~ GROMACS End

#~~~ CONFIG file
CONFIG_check=IntVar()
asd_config=ConfigParser.ConfigParser()
asd_config.optionxform = lambda option: option
if os.path.isfile("config.ini"):
	asd_config.read("config.ini")
	for a, b in asd_config.items("softwares"):
		if a == "MODPEP":
			MODPEP = b
		if a == "PSIPRED":
			PSIPRED = b
		if a == "MGLROOT":
			MGLROOT = b
		if a == "GROMACS_PREFIX":
			GROMACS_PREFIX = b
		if a == "ZDOCK":
			ZDOCK = b
		if a == "ZRANK":
			ZRANK = b
		if a == "HBPLUS":
			HBPLUS = b
		if a == "FLEXPEPDOCK":
			FLEXPEPDOCK = b
		if a == "ADFRROOT":
			ADFRROOT = b
#	if MODPEP and PSIPRED and MGLROOT and GROMACS_PREFIX and ZDOCK and ZRANK and HBPLUS and FLEXPEPDOCK and ADFRROOT:
#		CONFIG_check.set(1)
#	else:
#		CONFIG_check.set(0)
#else:
#	CONFIG_check.set(0)
#	asd_config.add_section("softwares")

def config_writer(TOOLNAME,PATH):
	dsa_config=ConfigParser.ConfigParser()
	dsa_config.optionxform = lambda option: option
	if dsa_config.read('config.ini'):
		pass
	else:
		dsa_config.add_section("softwares")
	dsa_config.set("softwares",TOOLNAME,PATH)
	config_file=open('config.ini','w')
	dsa_config.write(config_file)
	config_file.close()
	dsa_config=''

if MODPEP:
	MODPEP_check.set(1)
else:
	MODPEP_check.set(0)
	Button(root,text="Modpep",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_modpep_dir).grid(row=1,column=3,sticky=E+W+N+S)
if PSIPRED:
	PSIPRED_check.set(1)
else:
	PSIPRED_check.set(0)
	Button(root,text="PSI-PRED",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_psipred_dir).grid(row=1,column=4,sticky=E+W+N+S)
if GROMACS_PREFIX:
	GRO_check.set(1)
else:
	GRO_check.set(0)
	Button(root,text="GROMACS",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_gromacs_prefix).grid(row=1,column=5,sticky=E+W+N+S)


#~~~~ Docking tools
VINA_check=IntVar()
ZDOCK_check=IntVar()
ZRANK_check=IntVar()
HBPLUS_check=IntVar()
FLEXPEPDOCK_check=IntVar()
ADFR_check=IntVar()
Label(root,text="Peptide Screening\nTools",bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=0,sticky=E+W+N+S)

#~~~~~ VINA start
try:
	asd=subprocess.Popen(['vina'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	VINA_check.set(1)
except:
	VINA_check.set(0)
#~~~~~~~~~~~~~~~~~~
try:
	asd=subprocess.Popen(['vina_split'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output,error=asd.communicate()
	asd.wait()
	VINA_check.set(1)
except:
	VINA_check.set(0)

#~~~~~ VINA end

#~~~~~ ZDOCK start
def get_zdock_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/other/pep_combo/zdock3.0.2_linux_x64",title="ZDOCK Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/zdock'):
				global ZDOCK
				ZDOCK=filetemp
				config_writer('ZDOCK',ZDOCK)
				ZDOCK_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","ZDOCK not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","Directory not specified!",parent=root)
		return
def zdock_check(*args):
	if ZDOCK_check.get() == 1:
		Checkbutton(root,text="ZDOCK",variable=ZDOCK_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=3,sticky=E+W+N+S)
ZDOCK_check.trace('w',zdock_check)		
#~~~~~ ZDOCK end

#~~~~~ ZRANK start
def get_zrank_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/sam/other/pep_combo/zrank2_linux",title="ZRANK Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/zrank'):
				global ZRANK
				ZRANK=filetemp
				config_writer('ZRANK',ZRANK)
				ZRANK_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","ZRANK not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","Directory not specified!",parent=root)
def zrank_check(*args):
	if ZRANK_check.get() == 1:
		Checkbutton(root,text="ZRANK",variable=ZRANK_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=4,sticky=E+W+N+S)
ZRANK_check.trace('w',zrank_check)		
#~~~~~ ZRANK end

#~~~~~ HBPLUS start
def get_hbplus_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/Desktop/tools/hbplus",title="HBPLUS Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/hbplus'):
				global HBPLUS
				HBPLUS=filetemp
				config_writer('HBPLUS',HBPLUS)
				HBPLUS_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","HBPLUS not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","Directory not specified!",parent=root)
def hbplus_check(*args):
	if HBPLUS_check.get() == 1:
		Checkbutton(root,text="HBPLUS",variable=ZRANK_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=5,sticky=E+W+N+S)
HBPLUS_check.trace('w',hbplus_check)		
#~~~~~ HBPLUS end


#~~~~~ ROSETTA start
def get_flexpepdock_dir():
	filetemp=tkFileDialog.askopenfilename(initialdir="/home/bioinfo/Desktop/tools/Rosetta/rosetta_bin_linux_2018.09.60072_bundle/main/source/bin",title="FlexpepDock Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.exists(filetemp):
				global FLEXPEPDOCK
				FLEXPEPDOCK=filetemp
				config_writer('FLEXPEPDOCK',FLEXPEPDOCK)
				FLEXPEPDOCK_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","FlexpepDock not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","Directory not specified!",parent=root)
def flexpepdock_check(*args):
	if FLEXPEPDOCK_check.get() == 1:
		Checkbutton(root,text="FlexPepDock",variable=FLEXPEPDOCK_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=6,sticky=E+W+N+S)
FLEXPEPDOCK_check.trace('w',flexpepdock_check)		
#~~~~~ ROSETTA end

#~~~~ ADFR start
def get_adfr_dir():
	filetemp=tkFileDialog.askdirectory(initialdir="/home/bioinfo/ADFRsuite-1.0",title="ADFR Directory",parent=root)
	if filetemp:
		if ' ' in filetemp:
			tkMessageBox.showinfo("Warning!","Space found in the directory path!\nKindly remove the space",parent=root)
			return
		else:
			if os.path.isfile(filetemp+'/bin/adcp'):
				global ADFRROOT
				ADFRROOT=filetemp
				config_writer('ADFRROOT',ADFRROOT)
				ADFR_check.set(1)
			else:
				tkMessageBox.showinfo("Warning","ADCP not found in the specified directory!",parent=root)
				return
	else:
		tkMessageBox.showinfo("Warning","Directory not specified!",parent=root)
def adfr_check(*args):
	if ADFR_check.get() == 1:
		Checkbutton(root,text="ADFR",variable=ADFR_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=7,sticky=E+W+N+S)
ADFR_check.trace('w',adfr_check)		
#~~~~ ADFR end

if ZDOCK:
	ZDOCK_check.set(1)
else:
	ZDOCK_check.set(0)
	Button(root,text="ZDOCK",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_zdock_dir).grid(row=2,column=3,sticky=E+W+N+S)

if ZRANK:
	ZRANK_check.set(1)
else:
	ZRANK_check.set(0)
	Button(root,text="ZRANK",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_zrank_dir).grid(row=2,column=4,sticky=E+W+N+S)

if HBPLUS: 
	HBPLUS_check.set(1)
else:
	HBPLUS_check.set(0)
	Button(root,text="HBPLUS",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_hbplus_dir).grid(row=2,column=5,sticky=E+W+N+S)

if FLEXPEPDOCK:
	FLEXPEPDOCK_check.set(1)
else:
	FLEXPEPDOCK_check.set(0)
	Button(root,text="FlexPepDock",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_flexpepdock_dir).grid(row=2,column=6,sticky=E+W+N+S)

if ADFRROOT:
	ADFR_check.set(1)
else:
	ADFR_check.set(0)
	Button(root,text="ADFR",bg="white",font=("Times",10,"bold","underline"),relief=RAISED,borderwidth=3,width=15,height=3,command=get_adfr_dir).grid(row=2,column=7,sticky=E+W+N+S)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Checkbutton(root,text="GNU Parallel",variable=PARALLEL_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=1,sticky=E+W+N+S)
Checkbutton(root,text="MGLTools",variable=MGLROOT_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=1,column=2,sticky=E+W+N+S)
Label(root,bg="white",relief=SOLID,width=15,height=3).grid(row=1,column=6,columnspan=2,sticky=E+W+N+S)


Checkbutton(root,text="GNU Parallel",variable=PARALLEL_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=1,sticky=E+W+N+S)
Checkbutton(root,text="AutoDock\nVina",variable=VINA_check,state=DISABLED,bg="white",font=("Times",10,"bold"),relief=SOLID,width=15,height=3).grid(row=2,column=2,sticky=E+W+N+S)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~ Check for installations end
Button(root,text="Peptide Modelling",bg="maroon1",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=30,height=3,command=run_pepmod).grid(row=3,column=0,columnspan=4,sticky=E+W+N+S)
#Button(root,text="Peptide Virtual screening",bg="cyan",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=30,height=3,command=run_pepscreen).grid(row=3,column=3,columnspan=4,sticky=E+W+N+S)
Button(root,text="Peptide Virtual screening",bg="cyan",font=("Times",15,"bold","underline"),relief=RAISED,borderwidth=3,width=30,height=3,command=dock_tools).grid(row=3,column=4,columnspan=4,sticky=E+W+N+S)
mainloop()
