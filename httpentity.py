#!/usr/bin/env python3
import os
import sys


def check_file(file_name):
    file_name = file_name.translate(
        {ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name += ".json"
    return file_name


def read(json_file):
    json_file = check_file(json_file)
    my_file = open(json_file, "r")
    data = my_file.read()
    my_file.close()
    list1 = data.split("\n")
    list2 = []
    for s in list1:
        str = s.replace(" ", "").replace("\"", "\\\"")
        list2.append(str)
    m = "\"" + " ".join(list2) + "\""
    print(m)
    save(m)


def save(data):
    with open('httpentity.txt', 'w') as f:
        f.write(data)
        f.close()


file_name = sys.argv[1]
path = os.getcwd().replace("\\", "/")

read(file_name)
