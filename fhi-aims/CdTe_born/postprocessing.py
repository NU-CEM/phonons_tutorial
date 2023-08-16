from ase.io import read, write
from ase import atoms
import shutil, os
from pathlib import Path

def get_polarization(aims_output_file):
    f = open(aims_output_file, 'r')
    for line in f:
        nline = line.split()
        if 'full' in nline and 'polarization'in nline:
            polarization = float(nline[-2])
            break
    return polarization

atoms = read('geometry.in')
non_equivalent_atoms = [0, 9]
displacement = 0.01 * atoms.get_cell_lengths_and_angles()[0]
print(f'The displacement is 1% from the lattice vector lenghts: {displacement} AA')
volume = atoms.get_volume()
print(f'Volume of the cell is: {volume} AA^3')

aims_output_file = 'aims.out'

for atom in non_equivalent_atoms:
    atom_symbol = atoms.get_chemical_symbols()[atom]
    os.chdir(f'{atom_symbol}')
    polarization = get_polarization(aims_output_file)
    born_charge = (volume / 1.602) * (polarization/displacement) * 0.1
    print(f'Z* for {atom_symbol} is {born_charge}')
    os.chdir('../')

