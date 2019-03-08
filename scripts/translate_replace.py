import fileinput
import os
import ast
import json
filename = '/Users/nicola/Documents/repository/wicloud/angular/src/app/pages/installation-wilamp/installation-wilamp.component.html'
# contents = open(filename).read()
# print(contents)

from collections import MutableMapping


def rec_merge(d1, d2):
    for k, v in d1.items(): # in Python 2, use .iteritems()!
        if k in d2:
            if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                d2[k] = rec_merge(v, d2[k])
    d3 = d1.copy()
    d3.update(d2)
    return d3


def add_key_to_json(value):
    filename_json = '/Users/nicola/Documents/repository/wicloud/angular/src/assets/i18n/it.json'
    current_dict = ast.literal_eval(open(filename_json).read())

    keys = value.split('.')
    keys_ = keys[:-1]

    index = len(keys) - 1
    temp_dict = dict()
    temp_dict[keys[index]] = value
    index -= 1

    while index > -1:
        new_dict = dict()
        new_dict[keys[index]] = temp_dict
        temp_dict = new_dict
        index -= 1

    current_dict = rec_merge(current_dict, temp_dict)
    open(filename_json, 'w').close()
    f2 = open(filename_json, 'w')
    f2.write(json.dumps(current_dict, indent=4))




dir_name = '/Users/nicola/Documents/repository/wicloud/angular/src/app/pages/installation-wilamp/'

dir_lists = [
    # 'address-wilamp',
    # 'contact-wilamp',
    # 'customer-wilamp',
    # 'energy-meter-module-wilamp',
    # 'gateway-wilamp',
    # 'installation-wilamp',
    # 'light-fixture-wilamp',
    'light-management-measure-wilamp',
    # 'light-management-module-wilamp',
    # 'light-profile-slot-wilamp',
    # 'light-profile-wilamp',
    # 'motion-management-module-wilamp',
    # 'node-modules-wilamp',
    # 'node-wilamp',
    # 'order-wilamp',
    # 'shipping-wilamp',
    # 'twilight-management-module-wilamp'
]

for single_name in dir_lists:
    dir_name = f"/Users/nicola/Documents/repository/wicloud/angular/src/app/pages/{single_name}/"
    files_list = os.listdir(dir_name)
    for file_ in files_list:
        if str.find(file_, '.component.html') > -1:
            with fileinput.FileInput(dir_name + file_) as file:
                lines_memory = []
                for line in file:
                    print(line)
                    flag_break = False
                    while True:
                        if str.find(line, 'jhiTranslate') > -1:
                            new_line = line[str.find(line, 'jhiTranslate'):]
                            new_line2 = new_line[2 + str.find(new_line, "=\""):]
                            key_old = new_line2[:str.find(new_line2, "\"")]
                            key = str.replace(key_old, 'wilampCloudApp.', '')
                            add_key_to_json(key)
                            line_to_find = f"jhiTranslate=\"{key_old}\""
                            line_to_insert = f"[translate]=\"'{key}'\""
                            line = str.replace(line, line_to_find, line_to_insert)
                        else:
                            lines_memory.append(line)
                            flag_break = True
                        if flag_break:
                            break

            print(lines_memory)

            open(dir_name + file_, 'w').close()
            f2 = open(dir_name + file_, 'w')
            for line in lines_memory:
                f2.write(line)
