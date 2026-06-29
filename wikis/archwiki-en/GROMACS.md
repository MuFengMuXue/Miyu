# GROMACS

According to the official website, GROMACS is:

:a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.

:It is primarily designed for biochemical molecules like proteins, lipids and nucleic acids that have a lot of complicated bonded interactions, but since GROMACS is extremely fast at calculating the nonbonded interactions (that usually dominate simulations) many groups are also using it for research on non-biological systems, e.g. polymers.

## Installation
Install the  package. Be sure to edit the PKGBUILD to suit your system (i.e. for MPI or GPU support). Some of the CMake options you may want to add/modify in the PKGBUILD are (cf.the latest GROMACS installation guide):

* - Add if you need double precision. According to the GROMACS install guide, double precision is "slower, and not normally useful." If you set this flag, the default suffix for all GROMACS programs is set to .
*, where  is one of  - Add in order to build with GPGPU support. Several other flags may be necessary; refer to the latest GROMACS installation guide.
* - Add to create a build able to run across multiple compute nodes. You will also need to have an MPI library such as  or . If you do not need MPI support (i.e., you just run on a single computer), you do not need this flag. If you set this flag, the default suffix for all GROMACS programs is set to .
* - GROMACS should detect the best SIMD instructions for your processor, so this flag should not be needed. But if you have some kind of compilation error, you can specify the SIMD level here. A list of available options for  is listed in the latest GROMACS installation guide.

* - Set to use , the built-in trajectory viewer. This flag requires the  and  packages.
* - Set to test your GROMACS build. To run the tests set your build to run . The  package is required.
* - Set to turn of default suffix for GROMACS programs for MPI or double precision builds.
* and  - Set the default suffix to xxx for binaries and libraries, respectively.

Some other packages that may increase performance are:
* - An external Boost library can be used to provide better implementation support for smart pointers and exception handling.
* - Run-time detection of hardware capabilities can be improved by linking with hwloc
* - Hardware-optimized BLAS and LAPACK libraries are useful for a few of the GROMACS utilities focused on normal modes and matrix manipulation, but they do not provide any benefits for normal simulations.

Since version 2019, GROMACS build is reproducible.

## Configuration
By default the top-level force field directory is located at . This can be changed by setting a different directory to the  environment variable. This is useful if you make modifications to a force field, or if you have another set of force fields you would like to use.

## Usage
Below is a basic workflow with most of the major commands mentioned. Every command should begin with . For more details on using GROMACS find a good tutorial and read the manual. A helpful flow chart is here.

## Setup
Simulations require a structure file (/), a topology file (), and a parameters file (). The following steps illustrate how to obtain these.

## Obtain structure file
A structure file, which contains the coordinates of all particles, can be obtained from a protein database or created by the user using a program.

## Generate a topology
A topology file indicates how atomic particles interact with one another. One method for generating a topology file is to use . If your solute is in a file named , do the following:

 $ gmx pdb2gmx -f protein.pdb

Then you will be prompted to select a force field and water model. A new structure file in gro format will be generated () as well as the corresponding topology file ().

If you did not obtain your structure file from a protein database, but instead created it yourself, most likely you will need to create a residue template file () for your molecule as well as update the  file. An example  file for OPLS methane is found here with its corresponding  file here (both files are from James Barnett's tutorial). The  file must be placed in the force field directory for the force field you are going to use.

See below for alternative ways to generate or obtain topologies.

## Box creation
A quick way to create a simulation box full of water around a solute is to do:

 $ gmx solvate -cp conf.gro -cs water -box X Y Z -o conf.gro -p topol.top

In the above the solute/protein's coordinates are initially stored in . A water model using water.gro (either found in the top-level force field directory or the current one) is used to fill the box with solvent, and the box dimensions are , , and . The topology file,  is updated and the new system is output to .

If  is omitted, a three-point water model is used. The other available water structures are  and .

You can also use different box types and non-water solvents.

## Adding ions
If the system is not charge-neutral, ions should generally be added. For example if the net charge of your system is -2, to add two positive sodium ions do:

Then select the index group corresponding with the solvent, which will be replaced by the ions. The  argument should correspond to an ion in the force field you are using.

## Parameter files
A parameters file should be created for each different step of a set of simulations (e.g., minimization, equilibration, production). A list of all possible options is here.

Here is a sample parameter file for a ten second production run at standard conditions:

## Running
## Basics
Simulations typically consist of two parts, described below.

First, there is a preprocessing step where the structure file, topology file, and parameters file are read in and written out to a single  file, also sometimes referred to as a topology file:
 $ gmx grompp -f grompp.mdp -c conf.gro -p topol.top -o topol.tpr
Here  is the parameters file for this simulation step,  is the structure file that begins this simulation step, and  is the topology file. A structure file () is output at the end of every simulation, so it should be used with  in a simulation that continues from the previous one (e.g., an initial equilibration run should use the structure file output from a previous minimization step).

Next, there is the actual simulation. The  file is read in with the main program  to run the simulation:
 $ gmx mdrun -s topol.tpr

In general these two parts are repeated for an energy minimization step, an equilibration step, and a production step. Multiple equilibration steps may be needed, especially when turning on pressure coupling. The production step and the last equilibration step should use the exact same parameters () except for the length of the simulation.

As an example, a set of simulations consisting of one minimization step, one equilbration step, and one production step might look like this:

Here , , and  are parameter files for the minimization, equilibration, and production steps, respectively.

## Acceleration & Parallelization
By default GROMACS uses all available processors on a single node. To run across multiple nodes, an MPI library is required. Using openmpi to run GROMACS takes the following form:

 $ mpirun -np totalranks -npernode rankspernode --hostfile filename gmx mdrun -s topol.tpr

Here totalranks is the total number of MPI ranks to create, rankspernode is the number of MPI ranks per node, and filename is the hostfile used to determine on which hosts to run the processes.

OpenMPI be used together with OpenMP as seen here:

 $ mpirun -np totalranks -npernode rankspernode --hostfile filename gmx mdrun -ntomp openmpthreads -s topol.tpr

If compiled without an external MPI library one can control MPI ranks and OMP threads, using GROMAC's thread-MPI. This will not be able to be run across multiple compute nodes:

 $ gmx mdrun -ntmpi totalranks -ntomp openmpthreads -s topol.tpr

Here openmpthreads is the number of OpenMP threads to create. totalranks*openmpthreads should equal the total number of processors.

GROMACS automatically detects any available GPUs if it was compiled with GPU support. The number of MPI ranks must be a multiple of the number of GPUs to be used. Using a GPU requires the Verlet cut-off scheme, which is set with the parameter  in your  file. The command takes the basic form:

 $ mpirun -np totalranks -npernode rankspernode --hostfile filename gmx mdrun -ntomp openmpthreads -s topol.tpr -gpu_id gpuids

Here gpuids is the zero-based id of each GPU in a list. That is, with only one GPU (), you would use . If two GPUs are available (), you would use . To use a GPU on multiple MPI ranks, simply list its id the number of times to be used. For example, to use four MPI ranks on two GPUS one would use , and , thus using each GPU on two MPI ranks. If running on two twenty-core machines, the command would look like:

 $ mpirun -np 8 -npernode 4 --hostfile filename gmx mdrun -ntomp 5 -s topol.tpr -gpu_id 0011

If using GROMACS thread-MPI on one twenty core machine this would be:

 $ gmx mdrun -ntmpi 4 -ntomp 5 -s topol.tpr -gpu_id 0011

See  as well as the GROMACS section on MPI acceleration and parallelization for more options.

## Restart a simulation
To restart a simulation from a checkpoint file do:

 $ gmx mdrun -s topol.tpr -cpi state.cpt

Here  is the original  used in the simulation, and  is the last checkpoint file from that simulation.

## Extend a simulation
To extend a simulation create a modified  file and use it with :

Where time is how much longer to run the simulation in picoseconds,  is the  file associated with the original simulation, and  is the latest checkpoint file from that simulation. Instead of using  one can also use  to specify the absolute ending time in picoseconds.

## Analysis
## Tools
GROMACS comes with many analysis tools built-in. A list of all possible possible commands can be obtained by typing  or by opening the man page for gromacs.

Some of the more prominent analysis commands are:

*  — calculate free energy difference estimates through Bennett's acceptance ratio.
*  — writes energies to xvg files and display averages.
*  — calculate radial distribution functions.
*  — convert and manipulates trajectory files.
*  — Perform weighted histogram analysis after umbrella sampling.

See below for other available tools.

## Index Files
Index files are optionally used in almost all GROMACS analysis programs. The program  controls the creation and modification of index files. Index files consist of group names and integer indices indicating the location of atomic sites in a trajectory frame. They are only required if the available residues found in a structure file do not group atomic sites together in the desired way. When running  the user is presented with a prompt in order to select, combine, and split groups of atoms through various commands. Typing  at the make_ndx prompt gives a full description of the commands available.

## Development
GROMACS uses Git for version control, so familiarize yourself with its usage, especially the topic on collaboration. To begin contributing you need to have a GitLab account with an SSH key. The official repository is located at gromacs/gromacs and it can be forked. Changes should be submitted as merge requests. When making changes, follow the style guidelines for the code and commits.

When you are ready to share your changes, ensure your HEAD is up to date with a branch that you want to contribute to. In general three branches are used:
*main is used for long-term development of major features which may require large changes in code.
*release-x-y is for features that do not require as much code change, where x and y are the major and minor version numbers of the next release respectively.
*release-x-y-patches is for bug fixes and small documentation changes to a previous release.

## Tips and tricks
## Create non-cubic box and fill with solvent
To create a non-cubic box filled with solvent, first do:

 $ gmx editconf -f protein.pdb -bt boxtype -d dist -o box.gro

The above command creates a  box around the molecule in  at  nm in every direction. The box is saved as .  can be , , , or .

Then fill with solvent:

 $ gmx solvate -cs tip4p -cp box.gro -o conf.gro -p topol.top

## Use multiple solutes
If you want to use multiple solutes randomly inserted, first do:

 $ gmx insert-molecules -box X Y Z -ci solute.pdb -nmol N -o box.gro

Where X, Y, and Z are the box dimensions in nanometers, and N is the number to insert. You will need to update your topology file with the inserted number of molecules.

Then fill with solvent:

 $ gmx solvate -cs tip4p -cp box.gro -o conf.gro -p topol.top

## Use a non-water solvent
To use a non-water solvent with standard tools such as  and  do the following:

# Create one solvent molecule's structure file and topology.
# Create a box containing a couple hundred of the solvent molecules (216 seems to be a standard) and run a short equilibration on the system at standard conditions.
# Copy the output structure file  from the simulation to , where solvent is the name you wish to use for this molecule. Place this copy in the top level force field directory (where each force field has its own directory).
# Modify the topology file for the single solvent by removing everything but the  section and name the molecule in the file as .
# Rename the topology file as  and move it to the force field directory to which it applies.
# Update  for the force field you wish to use with this solvent (located in the force field's directory), adding the solvent. You will simply add a line with  where filename omits the file extension.

Now when you run  this solvent model should be available for the applicable force field. Additionally you can use  when running .

## Structure and topology databases
* Automated Topology Builder & Repository  — repository for building blocks and interaction parameter files for molecules as well as an automated builder to help generate building blocks for novel molecules.
* RCSB Protein Data Bank — information about the 3D shapes of proteins, nucleic acids, and complex assemblies that helps students and researchers understand all aspects of biomedicine and agriculture, from protein synthesis to health and disease.
* SwissParam —  provides topology and parameters for small organic molecules compatible with the CHARMM all atoms force field, for use with CHARMM and GROMACS.
* TraPPE Parameter Database — search by molecule name, or build your own, in order to obtain TraPPE force field parameters. Note that it is necessary to convert the parameters to the correct units.
* Virtual Chemistry — comparison of experimental and computational results for thousands of molecules. Contains validated topology input files for CGenFF, GAFF and OPLS/AA.

## External libraries and programs
See List of applications/Science#Chemistry.

## Development
* GROMACS Issues on GitLab — project management page, where bugs, issues, and features are reported and tracked.
* GROMACS Merge requests on GitLab — the project's code review system.

## Documentation
* GROMACS forums — very active forums for users seeking help. Make sure to read the manual and search the archive before posting.
* GROMACS Manual — official GROMACS manual for the current version.
* GROMACS Online Reference

## Tutorials
* Official GROMACS Tutorials
* Justin Lemkul's Tutorials — includes a variety of different simulation methods (umbrella sampling, free energy calculations, etc).
* James Barnett's Tutorials — a few basic tutorials on simulations with an organic solute. Includes how to use  with a user-created molecule.
