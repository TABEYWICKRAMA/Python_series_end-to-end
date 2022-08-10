names = ["Thisara","Kavishka","Amaya","Supun","Abeywickarama"]
print(names)
print(names[0])
print(names[0:2])
names[0] = 'thisa'
print(names)


# ['Thisara', 'Kavishka', 'Amaya', 'Supun', 'Abeywickarama']
# Thisara
# ['Thisara', 'Kavishka']
# ['thisa', 'Kavishka', 'Amaya', 'Supun', 'Abeywickarama']



#List methods

no = [1,2,3,4,5]
print(no)
# [1, 2, 3, 4, 5]

no.append(6)
print(no)
# [1, 2, 3, 4, 5, 6]

no.insert(1,10)
print(no)
# [1, 10, 2, 3, 4, 5, 6]
#insertion is happening from beginning

no.remove(1)
print(no)
# [10, 2, 3, 4, 5, 6]
# index zero will be deleted

no.pop()
print(no)
# [10, 2, 3, 4, 5]
# deleting indexes from the end

#remove all the items
no.clear()
print(no)
# []


no = [1,2,3,4,5,6,7,8,9,10,5]
print(10 in no)
#True

print(11 in no)
#False

print(len(no))
#11

print(no.count(5))
#2


#Sort the List
no.sort()
print(no)
# [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]


#reverse the List
no.reverse()
print(no)
# [10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1]


#Copy the List
copy_no = no.copy()
no.append(77777)
print(no)
print(copy_no)
# [10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 77777]
# [10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1]


#-----------------------------------

num = [1,2,3,4,5]
for item in num:
    print(item)

#output
# 1
# 2
# 3
# 4
# 5


i = 0
while i < len(num):
    print(num[i])
    i += 1

#output

# 1
# 2
# 3
# 4
# 5


numbers = range(5)
print(numbers)

#output
# range(0, 5)

for number in numbers:
    print(number)

#output
# 0
# 1
# 2
# 3
# 4



for number in range(5,10,2):
    print(number)


#output
# 5
# 7
# 9

for number in range(5):
    print(number)

#output
# 0
# 1
# 2
# 3
# 4


#write a program to find a largest number in a list

# no = [0,1,2,3,4,5,6,7,8,9,10]
#
# i = 0
# min = 0
# max = 0
#
# while(i <= len(no)):
#      if min < no[i] :
#          min = no[i]
#      elif max > no[i]:
#          max = no[i]
#
# i += 1
# print('min ', min )
# print('max' , max)


# num = [0,1,2,33]
# min = num[0]
# max = num[0]
#
# #print(len(num))
#
# #x = len(num)
#
# for i in num:
#     if min <= i[i]:
#         min = i[i]
#         print('min')
#     else:
#         max = i[i]
#         print('max')
#
#
# print('min', min)
# print('max', max)

#-------------------------------------------------- official answer
numbers = [3,6,2,100,8,4]
max = numbers[0]
min = numbers[0]
for number in numbers:
    if number > max:
        max = number
    else:
        min = number
print('max is ', max)
print('min is ', min )

print('\n')

#2D Lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][1])
#5

matrix[1][1] = 33

print(matrix[1][1])
#33


for row in matrix:
    for item in row:
        print(item)

# 1
# 2
# 3
# 4
# 33
# 6
# 7
# 8
# 9

#write a program to remove the duplicates in a List

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# [2, 4, 6, 3, 1]













