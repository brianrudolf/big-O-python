# big-O-python
This project assesses the time complexity of various built in Python functions. The program will display a plot of the time to run a function vs the size of the input, and compares that against some common Big O approximate times. The common times are O(n<sup>2</sup>), O(n * log(n)), O(n), and O(log(n)).

`python3 main.py count`

---

_Contents:_
**[Installation](#installation)** |
**[Use](#use)** |
**[Example Output](#example-output)** |

---

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Installation
`pip3 install -r requirements.txt`

## Use
`python3 main.py <function or module to assess>`

The program will accept either an individual function to assess or a collection of functions as organized in `funcs/`

## Example Output
![alt text](images/count.png)
