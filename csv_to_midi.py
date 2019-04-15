"""
    Author: Trieu Vi Tran (Chris) - 15800120
    Date: 5/4/2019
    Version: 2.0
"""

import os.path
import sys


def csv_to_midi(input_path: str, output_path: str):
    """
    TODO: check if both paths are valid
    Converting all csv .txt files in input_path directory into midi files into output_path
    Require midicsv: https://www.fourmilab.ch/webtools/midicsv/
    :param input_path: input directory with csv.txt files
    :param output_path: output directory for midi files
    :return: Nothing
    """
    files = list(map(lambda s: s.split('.')[0], os.listdir(input_path)))
    for f in files:
        os.system('csvmidi {1}{0}.txt {2}{0}.mid'.format(f, input_path, output_path))


if __name__ == '__main__':
    csv_to_midi(sys.argv[1], sys.argv[2])
