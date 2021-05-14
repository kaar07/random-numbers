# Simple implementation of middle squared algorithm to generate random numbers
# Works for fixed number of digits
# Better results if digit count is high
# Proposed by Jon Von Neumann
# Disadvantage: If it ever generates 0, following values will also be 0.




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
