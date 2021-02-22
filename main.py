import argparse
import inspect

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

import funcs
from graph import background


def main(func_name, func_call):
    """Setup the chart, run the analysis on the Python function, and plot the results"""
    samples = np.logspace(1, 2, num=100)

    big_O = [
        func_call(main_len=int(x), sub_len=int(x / 10), num=1e6) for x in tqdm(samples)
    ]

    fig, ax = background(samples[-1], big_O[-1])

    fig.canvas.set_window_title("Big O Python")
    fig.suptitle(f"Time complexity of '{func_name}()'", fontsize=16)

    ax.plot(samples, big_O, marker="*", label=f"O({func_name})")

    ax.legend()

    plt.ylim(0, 1.25 * big_O[-1])

    plt.savefig(f"images/{func_name}.png")

    plt.show()


if __name__ == "__main__":
    """
    Take in a Python function to run the time complexity test.
    Accepts individual functions and sets of functions - both predefined in the func/ directory.

    Args:
        func (string): name of supported Python function to assess (or module)

    Returns:
        Plots results on screen
    """

    parser = argparse.ArgumentParser(description="A Python time complexity journey.")
    parser.add_argument(
        "FUT",
        metavar="func",
        type=str,
        help="Name of Python function to analyze",
    )

    args = parser.parse_args()

    FUT = getattr(funcs, args.FUT)

    if inspect.ismodule(FUT):
        for func_name, func_call in inspect.getmembers(funcs, inspect.isfunction):
            main(func_name, func_call)
    else:
        main(args.FUT, FUT)
