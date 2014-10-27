"""
Simple functions for finding files relative to the current file.
"""
from os import path
from traceback import extract_stack


def whereami():
    """
    Return the directory containing the file calling this function.

    Returns None when running from an interpreted session.
    """
    stack = extract_stack()
    calling_file = stack[-2][0]
    fullpath = path.realpath(calling_file)
    if path.exists(fullpath):
        return path.dirname(fullpath)
    else:
        return None


def relative_path(relpath):
    """
    Return a path relative to the directory containing the current file.
    """
    location = whereami()

    if location is not None:
        return path.realpath(path.join(location, relpath))
