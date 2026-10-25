This is using the csv files for attendees that Zoom provides. The first column is the name and we can use this to estimate the number of unique attendees across multiple csv files.

Steps to get a rough csv file to check for unique attendees
1. Download the entire csv file from zoom directly for all days into the folder that holds this code
2. Run the setup_output.sh file - this will take the csv files and create an output.txt file
3. Create virtual environement - python3 -m venv venv 
4. Go into the virtual environment - source venv/bin/activate
5. Run the python code - python3 cleanup.py  - it will create a deduped.txt and a removed_review.txt

The deduped.txt is the final list of names you need to double check. You should also double check the removed_review.txt to ensure all the ones it removed are legitimate.
