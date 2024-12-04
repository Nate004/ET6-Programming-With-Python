#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Swapping Values

Fill in the blanks to pass the assertions.

"""

a = 2
b = 1

assert a == int(input()), "a's initial value"
assert b == int(input()), "b's initial value"

temp = a
assert temp == int(input()), "temp's final value"

a = b
assert a == int(input()), "a's final value"

b = temp
assert b == int(input()), "b's final value"
