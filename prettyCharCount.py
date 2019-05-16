#Python3.7 - Automate The Boring Stuff - Al Sweigart

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
#pprint.pformat(count)

#If you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead
#pprint.pprint(someDictionaryValue) == print(pprint.pformat(someDictionaryValue))
