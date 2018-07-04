#!/usr/bin/env python3

import os

# requires prompt-toolkit > 2
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

global_kb = KeyBindings()

# if bottom toolbar is visible
global_toolbar = None

# color the application
style = Style.from_dict({
    # reset bottom_toolbar style
    'bottom-toolbar': 'noreverse gray bg:black',
    'bottom-toolbar label': 'black bg:darkcyan'
})

def bottom_toolbar():
    return HTML("1<label>Help  </label>")

@global_kb.add('c-b')  # Ctrl+B
def switch_toolbar(event):
    global global_toolbar, session
    if not global_toolbar:
        global_toolbar = bottom_toolbar
    else:
        global_toolbar = None
    session.bottom_toolbar = global_toolbar

session = PromptSession(os.getcwd() + ">", key_bindings=global_kb, bottom_toolbar=global_toolbar, style=style)
while True:
    try:
        text = session.prompt()
    except KeyboardInterrupt:  # [ ] in Far Ctrl+C does nothing
        break
    except EOFError:           # [ ] in Far Ctrl+D does nothing
        break
    else:
        print("[debug] " + text)

