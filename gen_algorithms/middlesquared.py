"""
The following is a primitive implementation of middle squared method of generating random number.
Proposed by Von Neumann.

Fairly decent algorithm for numbers with larger number of digits.
A serious disadvantage is that if it ever generates zero, further every other generated number will also be zero.

"""





def nextnum(number):
    string = str(number)
    length = len(string)
    upper_limit = length*'9'
    max_digits = len(str(pow(int(upper_limit),2)))
    squared = number * number
    squared_string = str(squared).zfill(max_digits)
    i = max_digits - length
    i = i//2
    return int(squared_string[i:i+length])

seed = int(input("Enter a sample number with required number of digits: "))
togen = int(input("Enter number of random numbers to be generated: "))
for i in range(togen):
    seed = nextnum(seed)
    print(seed,end=" ")
print("")
