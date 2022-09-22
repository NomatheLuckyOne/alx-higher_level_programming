#!/usr/bin/python3
"""Amodule that implements a LockClass"""


class LockedClass:
    """defines a class that prevents the user from dynamically creating
    attributes, except if it is first_name"""
    _slots_ = ["first_name"]
