#!/bin/bash
#SBATCH --job-name=web_scraper_forums
#SBATCH --output=output_%A_%a.out
#SBATCH --error=error_%A_%a.err
#SBATCH --array=1-700   # Number of URLs in the array
#SBATCH --ntasks=100     # This specifies how many concurrent main.py are running at one time
#SBATCH --cpus-per-task=1 # specified that each task is in a separate CPU
#SBATCH --mem-per-cpu= 4G
#SBATCH --time=04:00:00


module load webproxy

python main.py $SLURM_ARRAY_TASK_ID
