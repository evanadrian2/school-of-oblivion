# Magic 8 Ball
# Automate the Boring Stuff
# Chapter 4 Lists

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes Definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])