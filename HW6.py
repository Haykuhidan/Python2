#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Problem 1
def max(*args):
    if len(args)!=0:
      for arg in args:
        maxx=args[0]
        if maxx < arg:
            maxx=arg
      return maxx
    else:
        print("No numbers given")
        


# In[16]:


#Problem 2
def dec2(a):
    def final(*args,**kwargs):
        return a(*args,**kwargs)+", it's me"
    return final

def dec1(a):
    def final():
        return("<u> "+a()+" </u>")
    return final
@dec1
@dec2

def HI():
    return("Hi")
HI()


# In[25]:


#Problem 3
def my_range(n):
    my_list=range(0,n+1)
    for i in my_list:
        yield (i)
    print('there are no values left')

