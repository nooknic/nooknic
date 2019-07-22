#!/usr/bin/env python
# coding: utf-8

# In[1]:


#นางสาว นีรชา ชุมมิน 362515241007 EE36241N
S=input("Username :")
P=input("Password :")
if S=="nook" and P=="1414":
    print("Welcome to chick Shop.")
else :
    print("Error ,please try again.")
A=30
L=80
P=40
M=90
B=50
print("-------------------Menu-------------------")
print("Welcome to chick Shop")
print("1. Apple 30 THB")
print("2. Lychee 80 THB")
print("3. Peach 40 THB")
print("4. Melon 90 THB")
print("5. Banana 50 THB")
chick=int(input("What do you want?(1-5) : "))
number=int(input("How many do you want? : "))
if chick==1:
    print("You order ",number," of Apple ",A*number, " THB")
elif chick==2:
    print("You order ",number," of Lychee  ",L*number, " THB")
elif chick==3:
    print("You order ",number," of  Peach  ",P*number, " THB")
elif chick==4:
    print("You order ",number," of Melon ",M*number, " THB")
elif chick==5:
    print("You order ",number," of Melon ",B*number, " THB")


# In[ ]:




