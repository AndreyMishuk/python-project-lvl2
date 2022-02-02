#!/usr/bin/env python

import argparse
from gendiff.scripts.parsers import parser_dict2string
from gendiff.scripts.parsers import parser_file2dict


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

    dict_file1 = parser_file2dict(first_file)
    dict_file2 = parser_file2dict(second_file)

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

    return parser_dict2string(sorted_dict_result)


def update_dict(dict_res, dict_file, list_key, token):
    dict_res.update({token + str(key): dict_file[key]
                     for key in list_key})


if __name__ == '__main__':
    main()
