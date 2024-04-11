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


# In[ ]:





# In[ ]:




