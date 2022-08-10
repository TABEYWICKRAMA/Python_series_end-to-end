i = 1
while i <= 10:
    print(i)
    i += 1

#output

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10





i = 1
while i <= 10:
    print(i * '*')
    i += 1

#output

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********



i=1
while i<=3:
    print(i)
    i+=1
# 1
# 2
# 3



#i -> rows
#j -> columns

num = int(input('Please enter any Side of a Square: '))
print('Square Star Pattern')

i = 0
while i <= num:
    j = 0
    while j <= num:
        j += 1
        print('*')

    i += 1
    print('')

# *
# *
# *
#
# *
# *
# *
#
# *
# *
# *

num = int(input('Please enter any Side of a Square: '))
print('Square Star Pattern')

i = 0

while i <= num:
    j = 0
    while j <= num:
        j += 1
        print('*', end=' ')    #This print statement append all stars
    i += 1
    print('')   #This print statement control cursor to new line

# * * *
# * * *
# * * *


# print('*', end=' ')
# The end parameter of print()function is used to
# set the value of the string to be appended at the end of the print() function.
# By default it's value is set to the newline character \n unless specified otherwise.



#using \n in last print statement
#then there is a line between stars

num = int(input('Please enter any Side of a Square: '))
print('Square Star Pattern')

i = 0

while i <= num:
    j = 0
    while j <= num:
        j += 1
        print('*', end=' ')

    i += 1
    print('\n')

# * * *
#
# * * *
#
# * * *
