#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loops with Raw Input"""


import authentication


def login(username, maxattempts=3):
    """Allows 3 password attempts.

    Args:
        username = (str) a string representing the username of the user
        maxattempts = (int, optional) maximum number of password attempts. Default 3

    Returns:
        str and number of attempts left

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False
    """
CODEWORD = False

while not loggedin:
    getpass.getpass(userid) = authentication.authenticate(raw_input('Please enter your password: '))
    if getpass.getpass(userid) == 'yes':
        CODEWORD = True
    elif userid == False
return results

