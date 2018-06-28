#!/usr/bin/env python3

import os

# requires prompt-toolkit > 2
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings


global_kb = KeyBindings()

@global_kb.add('c-b')  # Ctrl+B
def switch_toolbar(event):
    print(event)

text = prompt(os.getcwd() + ">", key_bindings=global_kb)
print("[debug] " + text)
