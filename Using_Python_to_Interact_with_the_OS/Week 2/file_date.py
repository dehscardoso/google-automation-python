# The file_date function creates a new file in the current working directory, checks 
# the date that the file was modified, and returns just the date portion of the timestamp 
# in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" 
# and check the date that it was modified.

import os
import datetime

def file_date(filename):

  with open(filename, "w") as file:
    timestamp = os.path.getmtime(filename)
    date = datetime.datetime.fromtimestamp(timestamp)
 
  return ("{}".format(date.strftime("%Y-%m-%d")))

print(file_date("newfile.txt")) 