import os.path
import sys


def midi_to_csv(input_path, output_path):
    input_extension = '.mid'
    output_extension = '.txt'

    command = 'midicsv'
    files = list(map(lambda s: s.split('.')[0], os.listdir(input_path)))
    for f in files:
        os.system('{0} {2}/{1}{3} {4}/{1}{5}'
                  .format(command, f, input_path, input_extension, output_path, output_extension))


def csv_to_midi(input_path, output_path):
    input_extension = '.txt'
    output_extension = '.mid'

    command = 'csvmidi'
    files = list(map(lambda s: s.split('.')[0], os.listdir(input_path)))
    for f in files:
        os.system('{0} {2}/{1}{3} {4}/{1}{5}'
                  .format(command, f, input_path, input_extension, output_path, output_extension))


if __name__ == '__main__':
    if sys.argv[1] == 'midi':
        midi_to_csv(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'csv':
        csv_to_midi(sys.argv[2], sys.argv[3])
    else:
        raise Exception('Invalid input file')
