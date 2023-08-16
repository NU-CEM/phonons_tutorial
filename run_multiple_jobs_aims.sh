#!/usr/bin/env bash

for folder in phonopy-*; do cd $folder; nohup mpirun -n 6 aims.220619.scalapack.mpi.x > aims.out & cd ..; done
