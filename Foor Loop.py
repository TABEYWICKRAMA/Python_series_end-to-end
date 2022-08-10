for x in range(4):
    print(x)

# 0
# 1
# 2
# 3

for item in 'python':
    print(item)

# p
# y
# t
# h
# o
# n

for item in ['mosh','john','sarah']:
    print(item)

# mosh
# john
# sarah

for item in range(10):
    print(item)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for item in range(5,10):
    print(item)

# 5
# 6
# 7
# 8
# 9

for item in range(5, 10, 2):
    print(item)

# 5
# 7
# 9

prices = [10,20,30]
total = 0

for item in prices:
    total += item
    print(total)
print('Total is ' , total)

# 10
# 30
# 60

# Total is  60


# nested loops

numbers = [5, 2, 5, 2, 2]

#   output -

#   xxxxx
#   xx
#   xxxxx
#   xx
#   xx

#using one loop
numbers = [5, 2, 5, 2, 2]
for count in numbers:
    print('x' * count)

print('\n')

#using two loops

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


#   xxxxx
#   xx
#   xxxxx
#   xx
#   xx

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print(x_count)

# 5
# 2
# 5
# 2
# 2

#print a square when input keyboard number

num = int(input('Please enter a number: '))

i=0
for i in range(num):
    j=0
    for j in range(num):
        print('*', end='')
    print('')

# Get star Square using functions 
# Python program to print square star pattern

def pattern(n):
    for i in range(n):
        # printing stars
        print("* " * n)


# take inputs
n = int(input('Enter the number of rows: '))

# calling function
pattern(n)

