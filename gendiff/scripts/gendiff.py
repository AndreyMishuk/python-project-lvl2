import argparse


def main():
    parser = argparse.ArgumentParser(description = 'Generate diff',
                                     prog = 'gendiff',
                                     epilog="set format of output")

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='json')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
