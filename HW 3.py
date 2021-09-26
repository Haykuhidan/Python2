#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Practical Problem1
list1= ['hello', 1, True] 
print(list1)
list1.append(input())
print(list1)


# In[2]:


#HW problem 1
list1= ['hello', 1, True,str(input()), int(input())] 
print(list1)


# In[3]:


#HW problem 2
list2=[2,4,5,7,9,10,2,6,8,7,5]
print(list2)
x=int(input())
list2.remove(x)
print(list2)


# In[5]:


#HW problem 3
list3=['apple',0,5,[1,2,2],'peach', 8, 10]
print(list3)
list3.pop(0) 
list3.pop(3)
list3.pop(3)
print(list3)


# In[6]:


#HW problem 4
list3=['apple',0,5,[1,2,2],'peach', 8, 10]
new_list=list3.copy()
new_list.pop(0) 
new_list.pop(3)
new_list.pop(3)
print(list3)
print(new_list)


# In[7]:


#problem 5
a=[1, 4, 5, 7, 8, -2, 0,-1]
print(a[3],a[5])
#or
import operator
a=[1, 4, 5, 7, 8, -2, 0,-1]
print(operator.itemgetter(3, 5)(a))

a_sorted=a.copy()
a_sorted.sort(reverse=True)
print(a_sorted)
print(a_sorted[1:3], "\n",a_sorted[2:6])

a_sorted.pop(2)
a_sorted.pop(2)
print(a_sorted)

b=["grapes", "Potatoes","tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted=b.copy()
b_sorted.sort()
c =[a[1:3]+b[4:6]]
print(c)


# In[ ]:




