# DHTech submission

Since this research project is still ongoing, we are not making the scraping functions public at this time. Instead, the files here will focus on the two parallel implementations explained in the submission. 
For this purpose please assume that there is a file __functions.py__ that contains two functions: 
1. _urlscrape()_ which extracts the URLs of every individual forum when provided with the landing URL of the forum index page of which there are 2500, each containing 100 individual forums.
2. _scrapeoneforum()_ which scrapes the data of each post within that forum (date, poster, content) to a CSV for future use.

In this repository, there are two folders: 

### Folder 1- Multiprocessing

Here you will find the __urlscraper.py__ using the multiprocessing module to parallelize the execution of the _urlscrape()_ function for our 2500 index page URLs. 

### Folder 2- SLURM script

Here you will find the __main.py__ file which implements the _scrapeoneforum()_ function with an input from the CSV of the scraped URLs by the previous operation. Then you will find a bash script called __parallelforum.sh__ which submits the main.py file to be run with a job array to execute as many times as needed. This is a trial submit code so you will see the array only has 700 entries as if it's scraping only the first 700 forums even though the project itself scrapes upwards of 2 million forums.

