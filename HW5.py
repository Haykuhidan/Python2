#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1
d = {"name": "Armen", "age": 15, "grades": [10,8, 8, 4, 6, 7] } 
mean = sum(d["grades"])/len(d["grades"])
if mean > 7:
    print("Good job!")
else: print("You need to wrok more")
    


# In[2]:


#Problem 2
list1=[x**2 for x in range(1,51)]
print(list1)


# In[3]:


#Problem 3
list2=['a', 'abc', 'xyz', 's','aba', '1221']
listnew=[x for x in list2 if len(x)>=2 if x[0]==x[-1]]
print(len(listnew))


# In[4]:


#Problem 4
list1 = [1, 3, 5, 7, 9, 11, 13, 15] 
list2 =[4, 6, 14, 11, 8, 16]
for x in list1:
    print(x)
    if x == x in list2:
        break


# In[ ]:


#Problem 5
menu= ['ice cream', 'chocolate', 'apple crisp','cookies']

while True:
    desert=str(input())
    if desert not in menu:
        print("Please choose another desert")
        continue
    else: 
        print("Your desert will arrive in 10 minutes")
        break


# In[ ]:




