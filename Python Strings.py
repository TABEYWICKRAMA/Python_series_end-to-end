word = "HelpMe"
print(word)

#Print specific letter in a word 
print(word[1])


#
#Note-------------------------------------------------------------------------------------------------------------------------------

#word[0] = "T" #update python strings are immutable, after creating we can not change. so this will give an TypeError

#Ways to Modify Python Strings

name = "Thisar"
name = name + 'a' #Character at end
print(name)

name1 = "Thsara"
name1 = name1[:2] + 'i' + name1[2:] #Character at specific pos
print(name1)

name2 = "hisara"
name2 = 'T' + name2 #Character at start
print(name2)

#-----------------------------------------------------------------------------------------------------------------------------------