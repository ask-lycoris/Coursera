Practice Quiz: Managing Files & Directories

1)
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)  # コメントを書き込む
    filesize = len(comments)
  return(filesize)

print(create_python_script("program.py"))

2) ERROR
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open(filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

3)
mkdir()

4) ERROR
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, 'w') as file:
    timestamp = os.path.getmtime(filename)
  print(timestamp)
  # Convert the timestamp into a readable format, then into a string
  dt = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{date}".format(dt.year, dt.month, dt.day))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

5)
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join('..', os.getcwd())

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
