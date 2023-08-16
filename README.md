# Ab-initio phonons walkthrough

Walkthrough for the ab-initio phonons tutorial at [TDEP 2023](https://liu.se/en/research/tdep2023) (Linkoping, Sweden). This walkthrough covers your "every-day" finite-displacement phonon calculation, which can be split into the following steps:

1. Relax unit cell (see folder `CdTe_relax`)
2. Build supercell and generate displacements (e.g. `phonopy -d --dim="2 2 2" --aims`)
3. Calculate forces (see folder `CdTe_harmonic_phonons`)
4. Extract forces (e.g. `phonopy -f phonopy-FHI-aims-displacement-{001..004}/aims.out`)
5. Calculate born effective charges and dielectric constant if required (see folder `CdTe_born`)
6. Use the forces to build dynamical matrix and calculate property(s) of interest (e.g. `phonopy -p -s band.conf`)

## Approach and software

One of the strengths of the finite displacement method is that it is modular - so we can use various methods and tools for calculating the forces or post-processing results. In this case we use:

- [phonopy](https://phonopy.github.io/phonopy/) to generate the supercell, build and post-process the force-constant tensor.
- Density Functional Theory to calculate
  - (i) equilibrium lattice parameters at 0T;
  - (ii) forces after atomic displacements;
  - (iii) born effective charges;
  - (iv) dielectric tensors.

We give example input and output files for two popular electronic structure codes: [vasp](https://www.vasp.at/) and [fhi-aims](https://fhi-aims.org/). For licensing reasons the `POTCAR` files required for Vasp calculations cannot be provided. The input files `INCAR` (vasp) and `control.in` (fhi-aims) provide a justification for the various calculation parameters used. 

We also provide example input and output for [fhi-vibes](https://vibes-developers.gitlab.io/vibes/), which automates much of the process by combining many of the steps above into a single workflow. 

⚠️ Some calculation parameters have been chosen so that the calculations can complete in short time period. In particular, `light` basis sets have been used for fhi-aims calculations, whilst `tight` are usually required for production-level results. You should always converge calculation parameters (e.g. basis set, k-point sampling, supercell expansion) for your specific material and property of interest.

### Resources

- Associated powerpoint presentation [here]().
- fhi-aims walkthrough video [here]().

### Following the tutorial

`tutorial_clean`: You can follow along with each step of the walkthrough video using the input files in this folder. Due to time constraints we do not calculate the born effective charges or dielectric tensor, but use a pre-calculated `BORN` file. You will need [ASE](https://wiki.fysik.dtu.dk/ase/), phonopy and fhi-aims installed on your system. The conda dependencies can be found in `environment.yml`. We use mpi to run each calculation with 6 processes.

### Input and output files for electronic structure calculations

For those who may not be able to run the electronic structure calculations we provide the input and output files for each job. You can then post-process these using phonopy. Input and output files are provided for the born effective charge and dielectric calculations.

`CdTe_relax`(Step 2) : Input and output file for unit cell relaxation.

`CdTe_harmonic_phonons` (Step 3): Input and output files to calculate the forces required for harmonic phonons with finite displacement method.

`CdTe_born` (Step 5): Input and output for calculating Born effective charges. This required for the non-analytical charge correction. For more information about calculating Born effective charges with fhi-aims please see [this tutorial](https://fhi-aims-club.gitlab.io/tutorials/phonons-with-fhi-vibes/phonons/5_BEC/exercise-5/).

`CdTe_dielectric` (Step 5): Input and output files to calculate the "ion-clamped" high-frequency dielectric tensor	$\epsilon_\infty$.

`CdTe_harmonic_vibes` (FHI-aims only): Input and output files for calculating a phonon dispersion using fhi-vibes, which combines many of the steps above into a single workflow.

### Other configuration files and scripts 

`band.conf`: Phonopy configuration file for producing phonon dispersion (Step 6)
`mesh.conf`: Phonopy configuration file for producing phonon density of states and thermal properties (Step 6)
`preprocessing_phonopy_aims.py`: setting up multiple folders for force calculations
`run_multiple_jobs_aims.sh`: run multiple fhi-aims jobs in separate folders
