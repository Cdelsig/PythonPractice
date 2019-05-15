#Python3.7 - Automate The Boring Stuff - Al Sweigart
#challenge problem - ch3

def collatz(num):
    x = 0
    if num % 2 == 0: #it's even
        x = num // 2
        print(str(x))
    else: #it's odd (num % 2 == 1)
        x = (3 * num) + 1
        print(str(x))
    return x

print("Let's play a game! Enter a number: ")
try:
    x = collatz(int(input()))
    while x != 1:
        x = collatz(x)
except:
    print("You didn't enter a number!! Please enter numbers only. :)")
