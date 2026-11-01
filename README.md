# DFT Study of BCC Iron Using Quantum ESPRESSO

## Project Overview
This project investigates the structural and energetic properties of body-centered cubic (BCC) iron using Density Functional Theory (DFT) calculations performed with Quantum ESPRESSO.

The study focuses on the relationship between lattice parameter, total energy, and atomic volume.

## Objectives
- Perform self-consistent field (SCF) calculations for BCC iron.
- Study the effect of lattice parameter variation on total energy.
- Generate energy versus volume and energy versus lattice parameter plots.
- Estimate the equilibrium lattice parameter and bulk modulus using Birch–Murnaghan equation-of-state fitting.

## Software and Tools
- Quantum ESPRESSO
- Python
- NumPy
- SciPy
- Matplotlib
- Linux (Ubuntu)

## Methodology
1. Constructed BCC iron unit cells with different lattice parameters.
2. Performed SCF calculations using Quantum ESPRESSO.
3. Extracted total energies from calculation outputs.
4. Converted energies from Ry to eV and lattice parameters from Bohr to Å.
5. Calculated the atomic volume using V = a³/2.
6. Applied third-order Birch–Murnaghan equation-of-state fitting with B′ fixed at 4.
7. Generated energy–volume plots using Python.

## Preliminary Results
The Python analysis of the recorded energy values produced:

- Estimated equilibrium lattice parameter: approximately 2.93 Å.
- Estimated bulk modulus: approximately 135 GPa.
- Lowest recorded energy among the listed points occurs near 2.92 Å.

These are preliminary fitting results and require verification against the original SCF outputs and convergence settings.

## Project Files
- `fe_bcc.scf.in` — Initial SCF input.
- `fe_bcc.scf.out` — Initial SCF output.
- `fe_bcc_a*.in` — SCF input files for different lattice parameters.
- `fe_bcc_a*.out` — Corresponding SCF output files.
- `energy_volume_new.py` — Python energy–volume analysis and fitting.
- `fe_energy_volume_new.png` — Energy–volume plot.
- `fe_energy_vs_lattice.png` — Energy versus lattice parameter plot.

## Author
Yogita Sharma  
M.Tech, Materials Engineering  
Indian Institute of Science (IISc), Bengaluru

## Project Status
Computational analysis completed at a preliminary level. Verification of calculation convergence and fitted results is ongoing.
