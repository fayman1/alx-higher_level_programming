#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """
    Prevents user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
