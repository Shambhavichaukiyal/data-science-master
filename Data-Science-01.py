#!/usr/bin/env python
# coding: utf-8

# In[6]:


t1 =(1,2,3,45,5,2,3,2,2,2,2)
print(t1.count(2));


# In[7]:


t1 =(1,2,3,45,5,2,3,2,2,2,2)
print(t1.index(2));


# In[1]:


input_list = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
mylist = list(dict.fromkeys(input_list))
print(mylist)


# In[9]:


s1={1,2,3,4,5,67,7}
s2={2,3,5,68,9}
print(s1.union(s2))


# In[10]:


s1 = {1, 2, 3, 4, 5, 67, 7}
s2 = [2, 3, 5, 68, 9]
s1.update(s2)
print(s1)


# In[11]:


dict1={1:"cdfd",2:"jhj"}


# In[12]:


dict1


# In[13]:


dict1 = {1: {"k": "dff"}}


# dict1

# In[14]:


dict1


# In[15]:


dict1 = {'language': 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])

print(dict1)


# In[16]:


# Given dictionary
dict1 = {'language': 'Python', 'course': 'Data Science Masters', 'topics': ['Python', 'Machine Learning', 'Deep Learning']}

# Displaying view objects
keys_view = dict1.keys()
values_view = dict1.values()
items_view = dict1.items()

print("Keys view:", keys_view)
print("Values view:", values_view)
print("Items view:", items_view)


# In[17]:


def gy(*args):
    return args


# In[18]:


gy(1,2,3,4,5)


# In[19]:


def fibo(n):
    a = 0
    b = 1
    for i in range(0, n - 1):
        a, b = b, a + b
    


# In[3]:


for i in fibo(10):
    print(i)


# In[21]:


def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(0, n - 1):
        a, b = b, a + b
        print(b)


# In[22]:


fibo(6)


# In[23]:


def odd(n):
  list=[]
  for i in range(n):
     if(i%2!=0):
        list.append(i)
  return list
        


# In[24]:


odd(5)


# In[25]:


def eqq(*aoo):
  return aoo


# In[26]:


eqq([1,2,4,8,9])


# In[27]:


def wut(**kty):
    return kty

# Example usage
result = wut(a=1, b=2, c=3)
print(result)


# In[28]:


list=[2,4,6,8,10,12,14,16,18,20]
for i in range(len(list)):
   print(list[i])


# In[29]:


def prime(limit):
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Using the generator function to print the first 20 prime numbers
prime_gen = prime(1000)
for _ in range(20):
    print(next(prime_gen))


# In[30]:


a= lambda n,p:n**p
a(8,9)


# In[31]:


a= lambda n: n%2==0


# In[32]:


a(15)


# In[33]:


def sq(x):
  return x**2


# In[34]:


# Define the square function
def sq(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5, 6, 7]


result = list(map(sq, my_list))

print(result)


# In[35]:


l1=[1,2,3,5,6,7,8]
a = map((lambda n:n**2),l1)


# In[36]:


print(a)
for i in a:
  print(i)


# In[37]:


# List of tuples
data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# Sorting the list based on the integer value
sorted_data = sorted(data, key=lambda x: x[1])

# Printing the sorted list
print(sorted_data)


# In[38]:


# Given list of integers
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convert the list of integers into a tuple of strings using map and lambda
string_tuple = tuple(map(lambda x: str(x), integers))

# Print the resulting tuple
print(string_tuple)


# #Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
# ['python', 'php', 'aba', 'radar', 'level']
# 

# In[ ]:





# In[ ]:





# In[ ]:




