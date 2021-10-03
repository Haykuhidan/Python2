#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Problem 1
d={'name':'Armen', 'age': 15, 'grades': [10, 8, 8, 4, 6, 7]}
x=input()
d.get('weight',x)


# In[98]:


#Problem2
market={'dairy': ['yogurt', 'cheese'], 'fruits': ['banana', 'apple', 'orange', 'lemon','apple', 'banana', 'banana']}
market['candies']=['mars', 'kinder', 'twix']
list1=market['fruits']
list1.sort()
market['fruits']=set(list1)
market



# In[67]:


#Problem3
t1=(2, 'cat', 'a',-2, 'Anna')
t1_list=list(t1)
t1_list.remove('a')
t1=tuple(t1_list)
print(t1)

t2=(1,2,3,4,5)
t3=(t1[0],t1[1],t2[2],t2[3],t2[4])
print(t3[2])
t4= [(1,3,5), (8,9), ('Anna','Bob', 'Alice')]
print(t4[0][1])

