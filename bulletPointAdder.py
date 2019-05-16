#Python3.7 - Automate The Boring Stuff - Al Sweigart
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.
#! python3

import pyperclip
text = pyperclip.paste()
# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
