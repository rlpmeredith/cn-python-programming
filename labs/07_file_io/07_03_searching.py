'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''
# Tested 06-8-19

import os

my_dir = input("Type in the absolute pathname of the directory you wish to start from: ")
my_dict = {}

print("The list of jpg files under your directory is:")
for (root, dirs, files) in os.walk(my_dir):
    for name in files:
        if name.endswith('.jpg'):
            print(os.path.join(root, name))

print("The number of files of each type in your directory is:")
for item in os.scandir(my_dir):
    if not item.name.startswith('.'):
        filename, file_extension = os.path.splitext(item.name)
        if file_extension in my_dict:
            my_dict[file_extension] += 1
        else:
            my_dict[file_extension] = 1
print(my_dict)