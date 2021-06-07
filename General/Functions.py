import json


def get_json_data(json_file_path):
    with open(json_file_path) as json_file:
        return json.load(json_file)


def tab_str(some_str, tab_count=1):
    return ("\t" * tab_count) + str(some_str).replace("\n", "\n" + ("\t" * tab_count))
