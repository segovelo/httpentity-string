#!/usr/bin/env python3
import os
import sys


def check_file(file_name, ext):
    file_name = file_name.translate(
        {ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name += ext
    return file_name


def read(json_file, save_name):
    json_file = check_file(json_file, ".json")
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
    save(m, save_name)


def save(data, save_name):
    with open(check_file(save_name, ".txt"), 'w') as f:
        f.write(data)
        f.close()


file_name = sys.argv[1] if len(sys.argv) > 1 else "test"
save_name = sys.argv[2] if len(sys.argv) > 2 else "httpentity"
path = os.getcwd().replace("\\", "/")

read(file_name, save_name)
