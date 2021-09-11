#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Variables
project = str('cake')
difficulty = int(5)
ingredients = ['flour','butter','sugar','eggs','cocoa powder','baking powder']
print('apples' in ingredients)
print('butter' in ingredients)
print('eggs' in ingredients or 'margarine' in ingredients)
print('eggs' in ingredients and 'margarine' in ingredients)

flour = 175
butter = 175
sugar = '100g'
eggs = 2
cocoa_powder = '1ts'
baking_powder = 0.5
print(type(flour))
print(type(butter))
print(type(sugar))
print(type(eggs))
print(type(cocoa_powder))
print(type(baking_powder))

print('flour -', flour)
print('butter -', butter)
print('sugar -', sugar)
print('eggs -', eggs)
print('cocoa_powder -', cocoa_powder)
print('baking_powder -', baking_powder)


# In[2]:


#Operators
a = 15
b = 8 
c = 2
x = 5*pow(a,2)-a*b + (a%2)- a/5
y = pow(b,3) + 3*a*b-10*c
print(x)
print(y)

