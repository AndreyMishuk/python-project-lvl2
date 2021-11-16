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

        key_minus = sorted(
            [key
                for key in dict_file1
                    if key not in dict_file2
            ]
        )

        key_0 = sorted(
            [key
                for key in dict_file1
                    if key in dict_file2
                    and dict_file1[key] == dict_file2[key]
            ]
        )

        key_plus = sorted(
            [key
                for key in dict_file2
                    if key not in dict_file1
            ]
        )

        key_minus_plus = sorted(
            [key
                for key in dict_file1
                    if key in dict_file2
                    and dict_file1[key] != dict_file2[key]
            ]
        )

    dict_result.update({'- '+str(key): dict_file1[key] for key in key_minus})
    dict_result.update({'  '+str(key): dict_file1[key] for key in key_0})
    dict_result.update({'- '+str(key): dict_file1[key] for key in key_minus_plus})
    dict_result.update({'+ '+str(key): dict_file2[key] for key in key_minus_plus})
    dict_result.update({'+ '+str(key): dict_file2[key] for key in key_plus})

    return json.dumps(dict_result, indent=4)


if __name__ == '__main__':
    main()
