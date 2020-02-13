#! /usr/bin/env python

import json


def py_to_json(json_py):
    json_obj = json.dumps(json_py)
    return json_obj


def json_to_py(json_obj):
    json_py = json.loads(json_obj)
    return json_py


def json_to_file(file, data):
    with open(file, mode='w', encoding="utf-8") as file_output:
        json.dump(data, file_output)


def file_to_py(file):
    with open(file, mode='r', encoding="utf-8") as file_input:
        return json.load(file_input)


if __name__ == '__main__':
    data = dict(id=1, name="xiaohui", address="baoji", is_love=True, sex=None)
    print(data)
    print("-" * 20)
    json_obj = py_to_json(data)
    print(json_obj)
    print("-" * 20)
    json_py = json_to_py(json_obj)
    print(json_py)
    print("*" * 20)
    json_to_file("d.json", data)
    print("end to write to file")
    print(file_to_py("d.json"))
