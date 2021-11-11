import argparse


parser = argparse.ArgumentParser(description = 'Generate diff',
                                 prog = 'gendiff')

parser.add_argument('first_file')
parser.add_argument('second_file')

args = parser.parse_args()
print(args.accumulate(args.integers))
