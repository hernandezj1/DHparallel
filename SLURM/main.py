from functions import scrapeoneforum
import sys
import pandas as pd


def main():
    # Read the input CSV with the URL's extracted by the code in the multiprocessing folder
    data = pd.read_csv("urlscomplete.csv", header=0)
    urllist = list(data.URL)

    # Get the index for the current job array task from the slurm script by utilizing the sys module
    task_index = int(sys.argv[1]) - 1

    # Get the corresponding URL from the CSV
    url = urllist[task_index]

    # Input the URL into the function
    scrapeoneforum(url)

if __name__ == "__main__":
    main()
