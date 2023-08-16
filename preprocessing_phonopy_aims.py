import os

for i in range(1,5):
    os.mkdir('phonopy-FHI-aims-displacement-%03d'%i)
    os.chdir('phonopy-FHI-aims-displacement-%03d'%i)
    os.system('cp ../geometry.in-%03d geometry.in '%i)
    os.system('cp ../control.in .')
    os.chdir('../')
