#Python3.7 - Automate The Boring Stuff - Al Sweigart

myCats = []
while True:
    print('Enter the name of cat ' + str(len(myCats) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    myCats = myCats + [name] #list concatenation
print('My cats names are:')
for name in myCats:
    print(name)

# another way to use a for-loop with lists. The way above is more efficient.
for i in range(len(myCats)):
    print(myCats[i])

moreCats = ['Princess Kit Kat', 'Taffy', 'Crystal']
print('Enter your cats name:')
kitty = input()
if kitty not in moreCats:
    print(f'I do not have a cat named {kitty}')
else:
    print(f'{kitty} is the name of my cat too!')
