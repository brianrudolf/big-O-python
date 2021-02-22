"""
Asess the time complexity to search for a substring.
"""

import functools
import random
import string
import timeit

import matplotlib.pyplot as plt
from tqdm import tqdm


def lower(main_len=100, sub_len=10, num=10000):
    """Generate a larger string to search for a smaller string.
    Both of varying length, default is a length difference of 10x.

    Python doc description: Return a copy of the string with all
        the cased characters converted to lowercase.

    """

    def time_lower():
        letters = string.ascii_letters

        main_string = "".join(random.choice(letters) for i in range(main_len))
        sub_string = "".join(random.choice(letters) for i in range(sub_len))

        timer = timeit.Timer(functools.partial(main_string.lower))
        sample_time = (timer.timeit(num_time) / num_time) / num_random

        return sample_time

    num_random = int(num / 100)
    num_time = int(num / num_random)

    time_samples = [time_lower() for i in range(num_random)]
    avg_time = sum(time_samples) / len(time_samples)

    return avg_time


if __name__ == "__main__":

    n = [10, 100, 500, 1000, 5000, 10000, 50000, 100000]

    big_O = [lower(main_len=x, sub_len=x // 10) for x in tqdm(n)]

    plt.plot(n, big_O, marker="+")
    plt.show()
