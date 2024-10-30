## Terrible Directions

* Run "query.py" on accounting.chtc.wisc.edu to query for data in a range

		$ python3 query.py > YYYY-MM-DD_Ndays.csv

* R script will filter down to jobs that ran on prioritized nodes (we think)

		$ Rscript scratch.R

* Python creates nice summary tables based on user + node

		$ python3 scrach.py

## Changes Christina would make

* Add more arguments (right now you have to manually edit the filenames / dates)
* Turn the R script into a Python script
* Maybe include backfill for prioritized nodes, not just prioritized? to calculate prioritized vs backfill
