#!/usr/bin/env python
# coding: utf-8

# In[19]:


def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(i)
        elif isinstance(i, tuple):
            flat.extend(i)
        elif isinstance(i, (int, float)):
            flat.append(i)
        else:
            flat.append(i)
    return flat

def prod(flat):
    pro = 1
    for i in flat:
        pro *= i
    return pro


list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34)]
flattened_list = flatten(list1)
result = prod(flattened_list)
print("Product of all numbers in the flattened list:", result)


# In[25]:


def encrypt(msg):
    encrypted_msg = ""
    msg = msg.lower()
    for char in msg:
        if char.isalpha():
            shift = ord(char) - 97
            encrypted_char = chr(122 - shift)  
            encrypted_msg += encrypted_char
        elif char.isspace():
            encrypted_msg += "$"
        else:
            encrypted_msg += char
    return encrypted_msg

msg = input("Enter the message to encrypt: ")
encrypted_message = encrypt(msg)
print("Encrypted message:", encrypted_message)

# Q1. You are writing code for a company. The requirement of the company is that you create a python
function that will check whether the password entered by the user is correct or not. The function should
take the password as input and return the string “Valid Password” if the entered password follows the
below-given password guidelines else it should return “Invalid Password”.
Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.
# In[28]:


def password(msg):
    l, d, u, s = 0, 0, 0, 0
    for i in msg:
        if i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i.isupper():
            u += 1
        else:
            s += 1
    if u >= 2 and l >= 2 and s >= 3 and d >= 1:
        return True
    else:
        return False


password_str = input("Enter a password to check: ")
is_valid = password(password_str)
print("Is the password valid?", is_valid)


# In[ ]:


Q2. Solve the below-given questions using at least one of the following:
1. Lambda function
2. Filter function
3. Zap function
4. List Comprehension
B Check if the string starts with a particular letterY
B Check if the string is numericY
B Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-
B Find the squares of numbers from 1 to 10Y
B Find the cube root of numbers from 1 to 10Y
B Check if a given number is evenY
B Filter odd numbers from the given list.
[1,2,3,4,5,6,7,8,9,10-
B Sort a list of integers into positive and negative integers lists.
[1,2,3,4,5,6,-1,-2,-3,-4,-5,0]


# In[31]:


start = lambda x, y: x.startswith(y)


string = input("Enter a string: ")
letter = input("Enter the letter to check if the string starts with: ")

if start(string, letter):
    print("The string starts with the letter", letter)
else:
    print("The string does not start with the letter", letter)


# In[32]:


string = input("Enter a string: ")
st = map(lambda x: x.isdigit(), string)


if all(st):
    print("All characters in the string are digits.")
else:
    print("Not all characters in the string are digits.")


# In[33]:



fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]

fruits.sort(key=lambda x: x[1])

print("Sorted list of fruits by quantity:")
for fruit in fruits:
    print(fruit[0], ":", fruit[1])


# In[36]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


st = map(lambda x: x * x, lst)

result_list = list(st)

# Now, you can print or use the resulting list as needed
print(result_list)


# In[38]:


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


st = map(lambda x: x **(1/3), lst)

result_list = list(st)

# Now, you can print or use the resulting list as needed
print(result_list)


# In[42]:


start=lambda x: x%2==0
n=int(input("enter a numnber  "))
if start(n):
    print("true")
else: 
    print("false")


# In[44]:



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))


print("Odd numbers:", odd_numbers)


# In[51]:



numbers = [3, -7, 0, 9, -2, 5, -8, 4, -6, 1]
print(list(filter(lambda x: x > 0, numbers))+ list(filter(lambda x: x < 0, numbers)))


# In[ ]:




