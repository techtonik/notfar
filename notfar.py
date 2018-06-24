#!/usr/bin/env python3

import os

from prompt_toolkit import prompt

import sys

print(sys.stdin.isatty())
print(sys.stdout.isatty())

text = prompt(os.getcwd() + ">")
print("[debug] " + text)
