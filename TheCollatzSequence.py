# Collatz Sequence
# Automate the Boring Stuff
# Chapter 3 Functions

print("Enter a Number: ")
try:
    number = (int(input()))
except ValueError:
    print("Please enter a valid Integer")

def collatz(number):

    if number % 2 == 0:
        result = (number // 2)
        print(result)
        return result
    elif number % 2 == 1:
        result = (3*number+1)
        print(result)
        return result
    
while number != 1:
    number = collatz(number)



