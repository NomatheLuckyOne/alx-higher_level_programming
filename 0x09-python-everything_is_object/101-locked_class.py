#!/usr/bin/python3
"""Amodule that implements a LockClass"""


class LockedClass:
    """defines a class that prevents the user from dynamically creating
    attributes, except if it is first_name"""
    _noma_ = ["first_name"]
