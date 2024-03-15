from functions import urlscrape
import multiprocessing
from joblib import Parallel
from joblib import delayed

# Generating the list of index landing pages to be scraped.
page_numbers= list(range(1,2549+1))
pages=[]
for i in page_numbers:
    finalurl='https:/example-website/page-'+str(i)
    pages.append(finalurl)  

# At the end of the previous chunk of code the list pages contains 2549 URLs, all identical except for their page number


num = multiprocessing.cpu_count()      # This counts how many CPUs are in your computer or computing resource you are using
num_cores=num-1                      # Here we subtract the core(s) we want to leave free in the system. If using on your laptop leave as many as necessary to not crash any other processes that may be underway ( browsers, programs, etc.)
Parallel(n_jobs=num_cores,verbose=10)(delayed(urlscrape)(i) for i in pages)  

"""
The previous line runs the urlscrape function on the specified number of cores. When one of them is done the core is taken up by the next use of the function. 
For example, if num-cores ends up being 8. The program will scrape pages 1-8 and once one of them is done scraping, which could be 4 or 7 for all we know, that core immediately takes up process 9.
"""
