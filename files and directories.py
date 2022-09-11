from pathlib import Path

path = Path("ecommerce")
print(path.exists())

#If this directory is there then,
#True


path = Path("emails")
print(path.mkdir())

#this will create a directory


# path = Path("emails")
# print(path.rmdir())
# #This will delete directory


path = Path()
for file in path.glob('*.py'):
    print(file)
#This will show all the python files in this directory


# built_in_modules.py
# car_game.py
# classes.py
# cold_day.py
# dice.py
# dictionary.py
# Exception.py
# files and directories.py
# Foor Loop.py
# function.py
# guessing_game.py
# inheritance.py
# kg vs pounds.py
# Lists.py
# logical_operaters AND,OR,NOT.py
# main.py
# modules.py
# name_length_validation.py
# sum two numbers.py
# tuples.py
# Unpacking.py
# while loop.py


