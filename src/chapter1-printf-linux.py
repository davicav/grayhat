from ctypes import *

"""
On Linux, it is required to specify the filename including the extension to
load a library, so attribute access can not be used to load libraries. Either
the LoadLibrary() method of the dll loaders should be used, or you should load
the library by creating an instance of CDLL by calling the constructor:

Ref: http://docs.python.org/2/library/ctypes.html#loading-dynamic-link-libraries
"""
libc = CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("Testing: %s", message_string)
