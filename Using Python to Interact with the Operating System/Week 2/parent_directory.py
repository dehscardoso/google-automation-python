# The parent_directory function returns the name of the directory that's located 
# just above the current working directory. Remember that '..' is a relative path 
# alias that means "go up to the parent directory". Fill in the gaps to complete this function.

import os
def parent_directory():

  dir = os.getcwd()
  relative_parent = os.path.join(dir)

  return os.path.dirname(relative_parent)

print(parent_directory())