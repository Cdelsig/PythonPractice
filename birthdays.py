#Python3.7 - Automate The Boring Stuff - Al Sweigart

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print(name + "'s birthday has been added for " + birthdays[name])
