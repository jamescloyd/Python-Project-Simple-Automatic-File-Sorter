# In this project, I am creating a simple automatic file sorter to help sort files to their respective folder

# First, import both the "os" and "shutil" modules
import os, shutil

# Create a variable for the directory where all the files needed to be sorted are located
path = r'/Users/bronnie0826/Documents/Analyst_Builder/Python_Programming_for_Beginners/13_Project 3 - Automatic File Sorter Project/Automatic_Sorter/'

# Create a list of folder names of the folders we want to create and sort the files to
folder_names = ['CSV Files', 'Text Files', 'Image Files', 'TSV Files']

# Write a for loop to iterate through the folder names above to create respective folders if they do not already exist
for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# List out all the files to be sorted in the directory and assign the list to a variable for the iteration later
os.listdir(path)
file_names = os.listdir(path)

# Write a for loop to iterate the file names list and move the files to their respective folder if they are not in it
for file in file_names:
    if ".csv" in file and not os.path.exists(path + 'CSV Files/' + file):
        shutil.move(path + file, path + 'CSV Files/' + file)
    elif ".txt" in file and not os.path.exists(path + 'Text Files/' + file):
        shutil.move(path + file, path + 'Text Files/' + file)
    elif ".png" in file and not os.path.exists(path + 'Image Files/' + file):
        shutil.move(path + file, path + 'Image Files/' + file)
    elif ".tsv" in file and not os.path.exists(path + 'TSV Files/' + file):
        shutil.move(path + file, path + 'TSV Files/' + file)
