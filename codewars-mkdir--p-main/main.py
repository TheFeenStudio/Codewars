'''
Write a synchronous function that makes a directory and recursively makes all of its parent directories as necessary.

A directory is specified via a sequence of arguments which specify the path. For example:

mkdirp('/','tmp','made','some','dir')
...will make the directory /tmp/made/some/dir.

Like the shell command mkdir -p, the function you program should be idempotent if the directory already exists.

HINT:

In javascript/coffescript, you will want to require('fs') and use functions in that library.
Documentation on fs.
In python, you will want to use the os module and os.path
Documentation on os module
Documentation on os.path module
'''

import os
def mkdirp(*directories):
    if directories[0] == '/':
        arr = list(directories)
        arr.pop(0)
        directories = tuple(arr)
    full_path = '/'.join(directories)
    os.makedirs(full_path)

    if os.path.exists(full_path):
        return print(full_path)
    else:
        return print(full_path + ' does not exist')
