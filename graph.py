import matplotlib.pyplot as plt
import numpy as np

# Return a standard background plot showing common big-O functions


def background(x_max, y_max):
    fig, ax = plt.subplots(nrows=1, ncols=1)

    x = np.linspace(1, x_max, num=100)
    y = np.linspace(1e-3 * y_max, y_max, num=100)

    # log = np.log2(x)
    # log *= y_max / log2[-1]

    log = np.log(x)
    # log *= y_max / log[-1]
    log *= y_max / x[-1]

    nlog = x * np.log(x)
    # nlog *= y_max / nlog[-1]
    nlog *= y_max / x[-1]

    nsquare = np.square(x)
    # nlog *= y_max / nlog[-1]
    nsquare *= y_max / x[-1]

    ax.plot(x, nsquare, color="red", alpha=0.5, label="O(n^2)")
    ax.plot(x, nlog, color="darkorange", alpha=0.5, label="O(nlog(n))")
    ax.plot(x, y, color="goldenrod", alpha=0.5, label="O(n)")
    ax.plot(x, log, color="limegreen", alpha=0.5, label="O(log(n))")

    ax.set_facecolor("lightgrey")

    ax.grid(True, color="grey", alpha=0.5)

    return fig, ax


if __name__ == "__main__":

    x = 10
    y = 10

    fig, ax = background(x, y)

    fig.canvas.set_window_title("Big O Python")
    fig.suptitle("Background demo", fontsize=16)

    ax.legend()

    plt.ylim(0, y)
    plt.xlim(1, x)

    plt.savefig("images/background.png")

    plt.show()
