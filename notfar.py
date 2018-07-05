#!/usr/bin/env python3

import os

# requires prompt-toolkit > 2
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.application.current import get_app
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

def get_mainbar():
    """ return keybar adding missing empty keys
    """
    mainbar = [
        (1, 'Help'),
        (10, 'Quit'),
    ]
    # there could be 12 keys at the bottom
    keysno = max(10, max(m[0] for m in mainbar))
    # add missing keys to keybar
    for idx in range(1, keysno+1):  # 1-10 or 1-12
        if len(mainbar) >= idx:
            #print(len(mainbar), idx, mainbar[idx-1])
            if mainbar[idx-1][0] == idx:
                continue
            else:
                mainbar.insert(idx-1, (idx, ''))
        else: # no more buttons
            mainbar.append((idx, ''))
        #print(mainbar)
    return mainbar

def bottom_toolbar():
    keybar = get_mainbar()
    minlabel = 6
    labelled = []
    for key, label in keybar:
        if len(label) > minlabel:  # then trim label
            label = label[:minlabel]
        # {:{}} means width is specified by argument
        labelled.append("{}<label>{:{w}}</label>".format(
                        key, label, w=minlabel))
    return HTML(' '.join(labelled))

@global_kb.add('c-b')  # Ctrl+B
def switch_toolbar(event):
    global global_toolbar, session
    if not global_toolbar:
        global_toolbar = bottom_toolbar
    else:
        global_toolbar = None
    session.bottom_toolbar = global_toolbar


@global_kb.add('f10')  # F10
def quit(event):
    get_app().exit(exception=EOFError)  # mimic Ctrl-D


session = PromptSession(os.getcwd() + ">", key_bindings=global_kb, bottom_toolbar=bottom_toolbar, style=style)
while True:
    try:
        text = session.prompt()
    except KeyboardInterrupt:  # [ ] in Far Ctrl+C does nothing
        break
    except EOFError:           # [ ] in Far Ctrl+D does nothing
        break
    else:
        print("[debug] " + text)

