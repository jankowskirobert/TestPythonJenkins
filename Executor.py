import os

__author__ = 'rob'

def fivePrint():
    print("HEHEH 5")
    return 5

def sixPrint():
    print("HEHEH 6")
    return 6
# Functions
fivePrint()
sixPrint()
current_folder_path, current_folder_name = os.path.split(os.getcwd())
print(current_folder_name + " " + current_folder_path)
