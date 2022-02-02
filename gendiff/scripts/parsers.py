import yaml
import json


def parser_file2dict(file_):

    dict_result = {}

    dict_object_natation = {
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
        'json': json.loads
    }

    with open(file_) as file_load:
        input_file = file_load.read()
        type_file = file_.split('.')[-1]
        dict_result = dict_object_natation[type_file](input_file)

    return dict_result


def parser_dict2string(_dict):
    result_str = "{\n"
    for key, value in _dict.items():
        result_str += f'  {str(key).lower()}: {str(value).lower()}\n'
    result_str += "}"
    return result_str
