#!/usr/bin/env python3

import sys
import subprocess
import matplotlib.pyplot as plt
import os
import os.path

def main() -> int:
    if not os.path.exists('images'):
        os.mkdir('images')

    with open('pi_dec_1m.txt', 'r') as f:
        digits = f.read()
        digits = digits[2:]
        counts = [0] * 10
        xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        xs_str = [str(x) for x in xs]

        offset = 0
        scaled = 1
        next_scale_change = 10_000
        for i, d in enumerate(digits):
            counts[int(d)] += 1

            if i >= next_scale_change:
                scaled *= 10
                next_scale_change *= 10

            if i % scaled == 0:
                if i >= offset:
                    fig, ax = plt.subplots(nrows=1, ncols=1)
                    ax.bar(xs, counts, tick_label=xs_str)
                    ax.set_title(f'Digit Distributions of Pi ({i + 1} digits)')
                    fig.savefig(f'images/image_{i:08}.png')
                    plt.close(fig)
            print(f'Finished the {i}th digit of pi')


if __name__ == '__main__': sys.exit(main())
