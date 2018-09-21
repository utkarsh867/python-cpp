# Running a C++ program using Python
Using `subprocess` module to call external commands and applications.

## Motivation
Usage in various server-side applications to write algorithms in C++.

## Notes
* Add `shell=True` in `subprocess.call()` for Linux machines.
* `capture_output` was added in `Python 3.7`, hence, won't work for below v3.7
