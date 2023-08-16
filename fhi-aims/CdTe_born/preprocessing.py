from ase.io import read, write
from ase import atoms
import shutil, os
from pathlib import Path

atoms = read('geometry.in')
non_equivalent_atoms = [0, 9]
displacement = 0.01 * atoms.get_cell_lengths_and_angles()[0]
print(f'The displacement is 1% from the lattice vector lenghts: {displacement} AA')
print(atoms.get_volume())

for atom in non_equivalent_atoms:
    atom_symbol = atoms.get_chemical_symbols()[atom]
    Path(f'{atom_symbol}').mkdir(parents=True, exist_ok=True)
    os.chdir(f'{atom_symbol}')
    atoms_copy = atoms.copy()
    atoms_copy.positions[atom][0] += displacement
    shutil.copy('../control.in', '.')
    atoms_copy.write('geometry.in')
    os.chdir('../')

