#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Problem1
def div(x,y):
    assert y!=0, "can't divide"
    return x/y

div(5,1)


# In[44]:


#Problem2
list1=[5,'a',0,2]
text1="The entry is: {}"
text2="The reciprocal of {} is"
for n in list1:
    try:
        print(text1.format(n))
        print(text2.format(n),1/n)
    except Exception as e:
        print("Oops!", e) 


# In[67]:


#Problem3
class person:
    def __init__(self,name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = int(age)
        self.gender = gender
        self.student = bool(student)
        self.__password = password
    def Greeting(self,second_person):
        text3 = "Welcome dear {}"
        print(text3.format(second_person.name))
    def Goodbye(self):
        print("Bye everyone")


# In[ ]:




