"""
Asess the time complexity to search for a substring.
"""

import functools
import random
import string
import timeit

import matplotlib.pyplot as plt


def count(main_len=100, sub_len=10, num=10000):
    """Generate a larger string to search for a smaller string.
    Both of varying length, default is a length difference of 10x.

    Python doc description: Return the number of non-overlapping
    occurrences of a substring

    """

    def time_count():
        letters = string.ascii_letters

        main_string = "".join(random.choice(letters) for i in range(main_len))
        sub_string = "".join(random.choice(letters) for i in range(sub_len))

        timer = timeit.Timer(functools.partial(main_string.count, sub_string))
        sample_time = (timer.timeit(num) / num) / num_random

        return sample_time

    num_random = 100
    # avg_time = 0

    time_samples = [time_count() for i in range(100)]
    avg_time = sum(time_samples) / len(time_samples)

    # for i in range(num_random):

    # letters = string.ascii_letters

    # main_string = "".join(random.choice(letters) for i in range(main_len))
    # sub_string = "".join(random.choice(letters) for i in range(sub_len))

    # timer = timeit.Timer(functools.partial(main_string.count, sub_string))
    # avg_time += (timer.timeit(num) / num) / num_random

    return avg_time


if __name__ == "__main__":

    n = [10, 100, 500, 1000, 5000, 10000, 50000, 100000]

    big_O = [count(main_len=x, sub_len=x // 10) for x in n]

    plt.plot(n, big_O, marker="+")
    plt.show()
