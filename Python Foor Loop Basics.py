#!/usr/bin/env python
# coding: utf-8

# ### For Loop

# In[5]:


for x in ['Thisara','Harshana','Abeywickrama']:
    print(x)


# In[52]:


for x in ['Thisara','Harshana','Abeywickrama']:
    print(x, end=' ')


# In[54]:


for x in range(1,5):
    print(x)


# In[13]:


for x in range(1,5):
    for y in range(1,3):
        print(y)
    print("\n")
    print(x)


# In[37]:


for x in range(1,5):
    print(x)
    for y in range(1,3):
        print(y)
    print("\n")


# ### Star Patterns

# In[18]:


for x in range(1,5):
    print('*')


# In[19]:


for x in range(1,5):
    print('*'*x)


# In[23]:


for x in range(5,1,-1):
    print('*'*x)


# In[24]:


for x in range(5,0,-1):
    print('*'*x)


# In[28]:


for x in range(5,1,-1):
    print(' '*x+'*')


# *****

# In[35]:


# Define the number of rows and columns in the matrix
rows = 5
cols = 5

# Use nested for loops to print stars
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")  # Print a star and a space
    print()  # Move to the next row after printing a line of stars


# In[38]:


for i in range(3):
    for j in range(3):
        print(i, j)


# ### Nested Loops

# In[39]:


counter = 0  # Initialize a counter

while counter < 3:  # The while loop continues while counter is less than 3
    for i in range(3):
        print(i)
    counter += 1  # Increment the counter at the end of each while loop iteration


# In[46]:


for x in "Thisara":
    print(x)


# In[49]:


name = 'Thisara'
for x in name:
    print(x)


# In[50]:


name = 'Thisara'
for x in name:
    print(x,end='')

