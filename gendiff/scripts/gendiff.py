#!/usr/bin/env python

import json
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     prog='gendiff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='json',
                        help="set format of output")

    args = parser.parse_args()
    print(generated_diff(args.first_file, args.second_file))


def generated_diff(first_file, second_file):

    dict_result = {}

    with open(first_file) as file1, open(second_file) as file2:

        dict_file1 = json.load(file1)
        dict_file2 = json.load(file2)

        key_minus = (
            [key
                for key in dict_file1
                if key not in dict_file2
             ]
        )

        key_0 = (
            [key
                for key in dict_file1
                if key in dict_file2 and dict_file1[key] == dict_file2[key]
             ]
        )

        key_plus = (
            [key
                for key in dict_file2
                if key not in dict_file1
             ]
        )

        key_minus_plus = (
            [key
                for key in dict_file1
                if key in dict_file2 and dict_file1[key] != dict_file2[key]
             ]
        )

    update_dict(dict_result, dict_file1, key_minus, '- ')

    update_dict(dict_result, dict_file1, key_0, '  ')

    update_dict(dict_result, dict_file1, key_minus_plus, '- ')

    update_dict(dict_result, dict_file2, key_minus_plus, '+ ')

    update_dict(dict_result, dict_file2, key_plus, '+ ')

    sorted_dict_result = dict(
        sorted(
            dict_result.items(),
            key=lambda item: (
                item[0][2]
            )
        )
    )

    return parser_dict_to_string(sorted_dict_result)


def update_dict(dict_res, dict_file, list_key, token):
    dict_res.update({token + str(key): dict_file[key]
                     for key in list_key})


def parser_dict_to_string(_dict):
    result_str = "{" + '\n'
    for key, value in _dict.items():
        result_str += f'  {str(key).lower()}: {str(value).lower()}\n'
    result_str += "}"
    return result_str


if __name__ == '__main__':
    main()
