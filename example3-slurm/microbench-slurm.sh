#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem=256M
#SBATCH --array=1-100
#SBATCH --output=microbench-slurm.out

source mbenv/bin/activate

python microbench-slurm.py
