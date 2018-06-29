#!/usr/bin/env python3

import os

# requires prompt-toolkit > 2
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


global_kb = KeyBindings()

# if bottom toolbar is visible
global_toolbar = None

def bottom_toolbar():
    return "F1 Help"

@global_kb.add('c-b')  # Ctrl+B
def switch_toolbar(event):
    global global_toolbar, session
    if not global_toolbar:
        global_toolbar = bottom_toolbar
    else:
        global_toolbar = None
    session.bottom_toolbar = global_toolbar


session = PromptSession(os.getcwd() + ">", key_bindings=global_kb, bottom_toolbar=global_toolbar)
text = session.prompt()
print("[debug] " + text)

