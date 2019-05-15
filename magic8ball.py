#Python3.7 - Automate The Boring Stuff - Al Sweigart

import random

def getAnswer(num):
    if num == 1:
        return 'It is certain'
    elif num == 2:
        return 'It is decidedly so'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return 'Reply hazy try again'
    elif num == 5:
        return 'Ask again later'
    elif num == 6:
        return 'Concentrate and ask again'
    elif num == 7:
        return 'My reply is no'
    elif num == 8:
        return 'Outlook not so good'
    elif num == 9:
        return 'No way'

print('Ask the divine magic 8 ball a question!')
question = input()
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# with a list:
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
