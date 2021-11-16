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
<<<<<<< HEAD

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
=======
        file1_keys = list(dict_file1.keys())
        file2_keys = list(dict_file2.keys())

        key1_set = frozenset(file1_keys)
        diff_keys = [item for item in file2_keys if item not in key1_set]

        dict_result.update(generate_part_dict_diff(
            file1_keys,
            dict_file1,
            dict_file2,
            '- '
        ))

        dict_result.update(generate_part_dict_diff(
            diff_keys,
            dict_file2,
            dict_file1,
            '+ '
        ))

    print(len(dict_result))
    return dict_result


def generate_part_dict_diff(key_dict_1, dict_1, dict_2, sign):

    dict_part_result = {}

    for key in key_dict_1:

        if key in dict_2:
            if dict_1[key] == dict_2[key]:
                dict_part_result[key] = dict_2[key]
                continue
            else:
                dict_part_result['- '+str(key)] = dict_1[key]
                dict_part_result['+ '+str(key)] = dict_2[key]

        dict_part_result[sign+str(key)] = dict_1[key]

    return dict_part_result
>>>>>>> 7db5e5047c1398698901977f7e13694fb43cb754


if __name__ == '__main__':
    main()
