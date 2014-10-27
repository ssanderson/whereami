whereami
========

A simple Python module for figuring out where the heck your code is.

Usage:

In a file at `/foo/bar/buzz.py`
```
from whereami import relative_path, whereami

# Returns /foo/bar
path = whereami()

# Returns /foo/conf.conf
config_file = relative_path('../conf.conf')
```
