import os

import matplotlib.pyplot as plt

from processor import Processor


def main():
    file = os.environ.get('PROCESSING_INPUT_IMG')
    try:
        p = Processor(file)
        # p.keep_one_colour([156, 70, 99], 15)
        p.blur()
        plt.imshow(p.img)
        plt.show()
    except (FileNotFoundError, AttributeError):
        print(f'Invalid input: {file}')


if __name__ == '__main__':
    main()
