#!/usr/bin/env python3

import os

from prompt_toolkit import prompt

text = prompt(os.getcwd() + ">")
print("[debug] " + text)
