#!/usr/bin/env python3  

import os
import sys
from dataclasses import dataclass, field


"""
author: dmaynor@gmail.com
The script will scan through my !/code and !/home directory to look for virtual enviroments for python by looking for a venv directory structure.
It can be called from my ~/tools/bin directory so first it has to change working directory to my home directory, It will then scan ~/code and ~/work 
looking for venv directories. If it finds one the full path to venv is sotred in a list. When the scan is complete the list of all discovered venv directories
is displayed to the user. The user can then select a venv directory and the script will then change the working directory to that directory and execute the venv/bin/activate script.
"""
#Build a dataclass to store the path to the venv directory and metadata about the venv and project.
@dataclass
class ProjectList:
    project_lists: list = field(default_factory=dict)

    def __repr__(self) -> str:
        
        pass

#Initialize the ProjectList dataclass
pl = ProjectList()

#Check wthe current directory is my home directory, if not change to my homme directory
if os.getcwd() != os.path.expanduser('~'):
    os.chdir(os.path.expanduser('~'))

#build a list with code and work directories
directories = [os.path.expanduser('~/code'), os.path.expanduser('~/work')]

#recursively scan through the directories and look for venv directories
venv_list = []
found_count=1
for directory in directories:
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == 'venv':
                venv_dir = os.path.join(root, dir)
                venv_list.append(venv_dir)
                pl.project_lists[found_count] = venv_dir
                found_count += 1

#print the list of venv directories
print('\n')
if len(venv_list) == 0:
    print('No venv directories found')
else:
    print('The following venv directories were found:')
    for venv in venv_list:
        print(venv) 
    print("Dataclass:", pl.project_lists)



