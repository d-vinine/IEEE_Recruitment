n = int(input("Enter number of rows: "))

for i in range(n):
    print(" "*(n-i-1), end="") # prints the required amount of left padding. It is equal to the total number of rows 'n' minus the number of stars in the current row 'i+1'. 
    print("*"*(i+1)) # prints the required number of '*'
