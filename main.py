import argparse

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

import funcs.strings as strings
from graph import background


def main(args):
    """Setup the chart, run the analysis on the Python function, and plot the results"""
    samples = np.logspace(1, 3)

    # Method under test
    MUT = getattr(strings, args.func)

    big_O = [MUT(main_len=int(x), sub_len=int(x / 5), num=10000) for x in tqdm(samples)]

    fig, ax = background(samples[-1], big_O[-1])
    # fig, ax = background(samples[-1], samples[-1])

    fig.canvas.set_window_title("Big O Python")
    fig.suptitle(f"Time complexity of {args.func}", fontsize=16)

    ax.plot(samples, big_O, marker="+")
    plt.ylim(0, 1.1 * big_O[-1])
    # plt.ylim(0, samples[-1])

    plt.show()


if __name__ == "__main__":
    """
    Take in a Python function to run the time complexity test.
    Accepts individual functions and sets of functions - both predefined in the func/ directory.

    Args:
        func (string): name of supported Python function to assess

    Returns:
        Plots results on screen
    """

    parser = argparse.ArgumentParser(description="A Python time complexity journey.")
    parser.add_argument(
        "func",
        metavar="func",
        type=str,
        help="Name of Python function to analyze",
    )

    args = parser.parse_args()

    main(args)

    # Run the function under analysis
    # Return two arrays n and O to visualize time complexity

    # assess()

    # Plot n vs O
    # plot()
