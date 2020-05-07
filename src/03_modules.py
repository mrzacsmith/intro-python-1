"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

for arg in sys.argv:
    print('sys.argv', arg)

# Print out the OS platform you're using:

print(f'I am running a {sys.platform} system')

# Print out the version of Python you're using:

print(f'I am running python version {sys.version}')


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Current process ID: {os.getpid()}')

# Print the current working directory (cwd):
print(f'Current working directory: {os.getcwd()}')

# Print out your machine's login name
print()
