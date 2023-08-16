# Ab-initio phonons walkthrough

Walkthrough for the ab-initio phonons tutorial at [TDEP 2023](https://liu.se/en/research/tdep2023) (Linkoping, Sweden). This walkthrough covers your "every-day" finite-displacement phonon calculation, which can be split into the following steps:

1. Relax unit cell (see folder `CdTe_relax`)
2. Build supercell and generate displacements (e.g. `phonopy -d --dim="2 2 2" --aims`)
3. Calculate forces (see folder `CdTe_harmonic_phonons`)
4. Build force constant tensor (e.g. `phonopy -f phonopy-FHI-aims-displacement-{001..004}/aims.out`)
5. Calculate born effective charges and dielectric constant if required (see folder `CdTe_born`)
6. Use the force constant tensor to calculate property of interest (e.g. `phonopy -p -s --nac band.conf`)
7. Plot results for  (e.g. `sumo-phonon-bandplot --filename FORCE_SETS --dim 2 2 2`)

One of the strengths of the finite displacement method is that it is modular - so we can use various methods and tools for calculating the forces or post-processing results. In this case we use:
- [phonopy](https://phonopy.github.io/phonopy/) to generate the supercell and build the force-constant tensor.
- Density Functional Theory to relax the unit cell, calculate forces and calculate born effective charges. We give example input and output files for two popular electronic structure codes: [vasp](https://www.vasp.at/) and [fhi-aims](https://fhi-aims.org/). The input files `INCAR` (vasp) and `control.in` (fhi-aims) provide a justification for the various calculation parameters used. For licensing reasons the `POTCAR` files required for Vasp calculations cannot be provided.
- [sumo](https://smtg-ucl.github.io/sumo/) to produce a publication-ready plot.

We also provide example input and output for [fhi-vibes](https://vibes-developers.gitlab.io/vibes/), which automates much of the process by combining many of the steps above into a single workflow. 

⚠️ Some calculation parameters have been chosen so that the calculations can complete in short time period. In particular, `light` basis sets have been used for fhi-aims calculations, whilst `tight` are usually required for production-level results. You should always converge calculation parameters (e.g. basis set, k-point sampling, supercell expansion) for your specific material and property of interest.

### Resources

- Associated powerpoint presentation [here]().
- vasp walkthrough video [here]().
- fhi-aims walkthrough video [here]().

### Folders

`CdTe_relax`(Step 2) : Input and output file for unit cell relaxation.

`CdTe_harmonic_phonons` (Step 3): Input and output files to calculate the forces required for harmonic phonons with finite displacement method.

`CdTe_born` (Step 5): Input and output for calculating Born effective charges. These are required for the non-analytical charge correction. For more information about calculating Born effective charges with fhi-aims please see [this tutorial](https://fhi-aims-club.gitlab.io/tutorials/phonons-with-fhi-vibes/phonons/5_BEC/exercise-5/).

`CdTe_dielectric` (Step 5): Input and output files to calculate the "ion-clamped" static	macroscopic	dielectric tensor	$\epsilon_\infty$.

`CdTe_harmonic_vibes` (FHI-aims only): Input and output files for calculating a phonon dispersion using fhi-vibes, which combines many of the steps above into a single workflow.

### Other configuration files and scripts 

`band.conf`: Phonopy configuration file for producing phonon dispersion (Step 6)
