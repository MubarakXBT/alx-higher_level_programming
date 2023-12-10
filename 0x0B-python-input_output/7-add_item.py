#!/usr/bin/python3
"""
   =========
    Modules
   =========
5-save_to_json_file.py
6-load_from_json_file.py
sys module
json module
os module
"""
import json
import sys
import os
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
newlist = []
counter = len(sys.argv)
if os.path.isfile(filename) is True:
    mylist = load(filename)
    newlist = []
    if counter == 1:
        exit
    i = 0
    while counter > 0:
        if i > 0:
            newlist.append(sys.argv[i])
        i += 1
        counter -= 1
    newlist = mylist + newlist
    save(newlist, filename)
else:
    with open(filename, mode="w", encoding="utf-8") as myfile:
        if counter > 1:
            i = 0
            while counter > 0:
                if i > 0:
                    newlist.append(sys.argv[i])
                i += 1
                counter -= 1
            myfile.write(json.dumps(list(newlist)))
        else:
            myfile.write(json.dumps(list(newlist)))
