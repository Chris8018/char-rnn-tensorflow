"""
    Author: Trieu Vi Tran (Chris) - 15800120
    Date: 5/4/2019
    Version: 2.0
"""

import os.path
import sys


def midi_to_csv(input_path: str, output_path: str):
    """
    TODO: check if both paths are valid
    Converting midi files in input_path directory into csv.txt files into output_path
    Require midicsv: https://www.fourmilab.ch/webtools/midicsv/
    :param input_path: input directory with midi files
    :param output_path: output directory with csv.txt files
    :return: Nothing
    """
    files = list(map(lambda s: s.split('.')[0], os.listdir(input_path)))
    for f in files:
        os.system('midicsv {1}{0}.mid {2}{0}.txt'.format(f, input_path, output_path))


if __name__ == '__main__':
    midi_to_csv(sys.argv[1], sys.argv[2])
