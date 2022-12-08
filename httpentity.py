#!/usr/bin/env python3
import os, sys


path = os.getcwd().replace("\\", "/")

def check_file(file_name):
    file_name = file_name.translate({ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name += ".json"    
    return file_name
    
        
def read(logs_file, correlation_id):
    logs_file = check_file(logs_file)
    # opening the file in read mode
    my_file = open(logs_file, "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text
    # when newline ('\n') is seen.
    list1 = data.split("\n")
    for s in list1:
        print(s)
    my_file.close()


    def save(data, save_file):
        save_file = check_file(save_file)
        with open(save_file, 'w') as f:
            f.write(data)
            f.close()

