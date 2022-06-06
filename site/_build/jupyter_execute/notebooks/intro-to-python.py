#!/usr/bin/env python
# coding: utf-8

# # Intro to Python

# ## 1. Getting Started

# There are number of ways of running Python. This guide was written using Jupyter Notebook. To start, open the folder where Anaconda is installed and click "Jupyter Notebook". This will open local instance of Jupyter server in your browser (if not, point your browser to http://localhost:8888). 

# To start a new Python notebook, go to the right hand side, click "New", and then select "Python 3".

# ![](img/jupyter-01.png)

# You can enter your code at the "In" cell of a notebook. Clicking `Run` or typing `Shift` + `Enter` will evaluate the code and send the results to the corresponding "Out" block. 
# 
# To add a new cell, you can click `Insert` and then `Insert Cell Above` or `Insert Cell Below`. Alternatively, when an entire cell is highlighted (click outside the gray box where your cursor appears), you can enter `A` to insert a new cell above the current one or `B` to insert a new cell below the current one.
# 
# Finally, to delete a cell, you can click on `Edit` and then `Delete Cells`. Again, when a cell is highlighted with no cursor visible, you can also enter `D`+`D` to do the same thing.

# ![](img/jupyter-02.png)

# ## 2. Some Introductory Tips
# ### A. Commenting Code

# `#` begins a comment. Any text that comes after `#` will not be run. Comments are useful for explaining decisions in scripts for other users and your "future self". It can also be useful during debugging, where code is "commented out" but not deleted. 

# In[1]:


# this text is not run
b = 10 # but text before the start of the comment will be 
b


# Using triple quotes allows you to comment over multiple lines. This is particularly useful in writing clearly documented functions. More on functions later in this training:

# In[2]:


def triple(a):
    '''
    This function takes in a number as input
    and returns triple that number.
    '''
    return 3*a

triple(65)


# ### B. Getting Help

# `?` before or after an object will return information about the object. `??` will return a function's source code, if applicable.
# 
# Additionally, depending on your IDE, sometimes hovering your cursor over the function can similarly give you info about it.

# In[3]:


get_ipython().run_line_magic('pinfo', 'print')


# ## 3. Basic Operations, Variables, and Data Types
# ### A. Mathematical Operations

# Within a cell, you can execute simple mathematical operations:
# 
# | Operation | Description |
# |-----------|-------------|
# | x + y | 	sum of x and y |	  	 
# | x - y 	| difference of x and y | 	  	 
# | x * y  |	product of x and y 	 | 	 
# | x / y  |	quotient of x and y 	|  	 
# | x // y  | quotient of x and y rounded down to nearest whole number |
# | x % y |	remainder of x / y |
# | x ** y | x to the power of y |

# In[4]:


3+4


# In[5]:


10/5


# In[6]:


2**5


# ### B. Variables and Assignment

# - `=` is the assignment operator. An object created on the right side of an assignment operator is assigned to a name on the left side of an assignment operator. 
# 
# - Assignment operators are important for saving the consequences of operations and functions. Operations without assignment operators can be printed to the console but will not be saved.
# 
# - Here, we assign the value of 5 to a new variable `a` and can see that this value is saved.

# In[7]:


a = 5
a


# We can view the result of `a*4` by just printing the expression, but if we want to save it, we can assign it to a new variable, `b`.

# In[8]:


a*4


# In[9]:


b = a*4
b


# ### C. Printing Output

# In Jupyter Notebook, only the last unassigned value will be automatically printed to the console. To display other output within a cell, use the `print()` function.

# In[10]:


a
b


# In[11]:


print(a)
print(b)


# ### D. Data Types
# There are four basic data types in Python: integers, floating point numbers, strings, and booleans. We can check a variable's data type with the `type()` function.

# #### Integer (int) 
# Integers are used to store whole numbers. 

# In[12]:


x = 10
type(x)


# #### Floating Point (float) 
# Floats are used to store numbers with decimal values. 
# 
# The basic math operations above can be used with any numeric variables, that is, both `floats` and `ints`

# In[13]:


y = 3.14
type(y)


# In[14]:


x + y


# #### Strings 
# Strings are used to store text variables. 
# 
# String values are enclosed between either single (`'`) or double quotes (`"`). The sequence of characters in a string can be letters, numbers, special characters, or white space (space, tab, newline).

# In[15]:


astring = 'Hello World!'
type(astring)


# Triple quotes can be used to enclose long strings spanning multiple lines:

# In[16]:


long_string = '''
We can use triple quotes
To create strings
That span multiple lines
'''
print(long_string)


# #### Boolean (bool)
# Booleans are used to store True or False values. 

# In[17]:


x = True
type(x)


# ### E. Logical Expressions

# There are several comparison operators that result in Boolean values, depending on whether the statement is True or False:
# 
# | Operation | Description |
# |-----------|-------------|
# | == 	    | equals |
# | != 	    | does not equal |
# | < 	    | is strictly less than |
# | <= 	    | is less than or equal to |
# | > 	    | is strictly greater than |
# | >= 	    | is greater than or equal to |

# In[18]:


3 == 4


# In[19]:


3 < 4


# In[20]:


4 * 5 != 100


# There are also three main operators that can be applied directly to `bool` values:
# 
# | Operator      | Result                                           | 
# | ------------- |--------------------------------------------------|
# | x and y       | `True` if x and y are `True`, else `False`       |
# | x or y        | `True` if either x or y are `True`, else `False` |
# | not x         | `True` if x is `False`, `False` if x is `True`   |

# In[21]:


x = (5 > 4)
x


# In[22]:


y = (0 > 10)
y


# In[23]:


print(x and y)
print(x or y)
print(not x)


# The `bool`, `int`, `float`, and `string` types can also be used as functions to convert values of one type to another.

# In[24]:


float(5)


# In[25]:


str(5.0)


# ## 4. Additional Data Structures
# 
# Besides the four basic data types, there are a few important objects in Python that can store a collection of values.

# ### A. Lists and Tuples
# 
# - Lists and tuples are the most common and basic way to store a collection of values. Both can store any number of values of heterogeneous data types.
# 
# - Values in both lists and tuples are separated by commas and enclosed by square brackets `[]` for lists and parentheses `()` for tuples.
# 
# - In practice, lists and tuples are nearly identical, but the one key difference between them is mutability (more on that below).

# In[26]:


alist = [1, 2, 3, 4, 5]
atuple = (1, 'a', True)
print(alist)
print(atuple)


# #### Indexing
# - Indexing allows us to access specific values within a collection. We use square brackets to index a list. 
# 
# - In Python, indexing begins at 0. This means that the first value in a sequence has an index of 0, the second has an index of 1, and so on.

# In[27]:


my_list = [1, 2, 3, 4, 5]
my_list[0]


# We can also use negative numbers to traverse a list in reverse. -1 refers to the last item in a list, -2 the second-to-last, and so on.

# In[28]:


my_list[-1]


# #### Slicing
# 
# - Multiple values in a sequence can be accessed using slicing, according to the following syntax:
# 
# - `object_name[start:stop]`, where the start index is included, and the end index is excluded. Slicing a list will also return a list. 

# In[29]:


my_list[1:3]


# If we want the slice to start at the beginning of a list, we can simply omit the first index in the slice. In the example below, we access the first 3 elements in a list.

# In[30]:


my_list[:3]


# Similarly, we can omit the last index in a slice to continue until the end of the sequence:

# In[31]:


my_list[2:]


# ### Mutability
# - Lists are *mutable* objects, meaning that their values can be changed using the above operations of indexing and slicing.
# 
# - Tuples are *immutable* objects whose values can be accessed but not altered. You can see below that trying to reassign the second item in the tuple yields an error.
# 
# - Immutable objects like tuples (and strings!) allow programmers to make sure that assigned values aren't inadvertently overwritten. 
#     - In practice, tuples function nearly identically to lists. 
#     - You should feel free to widely make use of lists, but it's good to be aware of the distinction.

# In[32]:


new_list = [0, 0, 0]
new_list[1] = 100
new_list


# In[33]:


new_tuple = (0, 0, 0)
new_tuple[1]  = 100


# #### Other Useful List Operations

# | Operation      | Result                                           | 
# | ------------- |--------------------------------------------------|
# | `len()`      | Returns the length of the list       |
# | `sort()`        | Sorts the list |
# | `count(item)`         | Counts \# occurrences of item in list   |
# | `append(item)` | Adds item to the end of the list
# | `insert(index, item)` | Insert item at specific index in list |
# | item `in` list        | Returns True or False depending on whether item appears in list |

# In[34]:


my_list = [1, 4, 3, 2, 5, 3]
len(my_list)


# In[35]:


my_list.sort()
my_list


# In[36]:


my_list.count(3)


# In[37]:


my_list.append(1000)
my_list


# In[38]:


my_list.insert(0, 'new_item')
my_list


# Special mention to this last `in` operation, which can be widely used on lists, tuples, strings, and dictionaries (below):

# In[39]:


print(7 in my_list)
print(7 not in my_list)


# ### B. Dictionaries
# 
# - Dictionaries are used to store pairs of objects in a `key:value` format. They are created with curly brackets `{}`. While keys must be strings or numbers, values can be of any data type. 
# 
# - A simple dictionary might be used to store information such as the names of students in a class and their respective grades on a test:

# In[40]:


scores = {'Arvind': 94, 'Bob': 75, 'Camila': 100}


# We can access a value in a dictionary by indexing with its key. For example:

# In[41]:


scores['Arvind']


# We can also access all dictionary keys, values, or pairs with the `keys()`, `values()`, and `items()` functions.

# In[42]:


print(scores.keys())
print(scores.values())
print(scores.items())


# - More complex dictionaries can store lists of values. For example, if each student above has taken 3 tests in a semester, we can store that information in a list.
# 
# - This is a different format for storing data than a typical spreadsheet or dataframe style with rows and columns, but you can see how different Python objects can be combined in meaningful ways. 
# 
# - In practice, you will mostly use Pandas to work with datasets, but these data types and structures are the building blocks!

# In[43]:


scores = {'Arvind': [94, 80, 85], 'Bob': [75, 75, 81], 'Camila': [100, 93, 97]}
print(scores['Arvind']) # Get all of Arvind's scores
print(scores['Arvind'][0]) # Get Arvind's first test score


# ### C. Sets
# - Sets are the final structure used to store collections of data in Python, and are less commonly used than both lists and dictionaries.
# 
# - Unlike the other structures, sets are not ordered and duplicate values are not allowed. Sets are created with curly brackets as follows:

# In[44]:


aset = {'TECH', 'METRO', 'IBP'}
aset


# One useful application of a set is to obtain just the unique values in a list, by converting the list to a set.

# In[45]:


duplicates_list = ['TECH', 'METRO', 'IBP', 'METRO']
set(duplicates_list)


# In[46]:


float(5)


# In[47]:


str(5.0)


# ## 5. Control Flow

# ### A. `if`, `elif`, `else`

# The `if`, `elif` (i.e., `else`-`if`) and `else` statements are used to control the execution of code based upon a condition. The `if` statement checks the condition given, and executes the code if it evaluates to `True`.

# In[48]:


x = 7
if x < 10:
    print("x is less than 10")


# The `if` statement can be followed by an `else` statement that will execute if the condition given to `if` evaluates to `False`.

# In[49]:


y = 15
if y < 10:
    print("y is less than 10")
else:
    print("y is greater than 10")


# What if there are multiple conditions you wish to evaluate? You can nest `if`/`else` statements, but this can quickly become very messy and difficult to follow.

# In[50]:


z = 20
if z < 10:
    print("z is less than 10")
else:
    if z < 15:
        print("z is less than 15")
    else:
        print("z is greater than 15")


# Instead, your `if` statement can be followed by one or more `elif` statements. Once a `True` statement is reached, the execution of the `if`/`elif`/`else` block stops.

# In[51]:


z = 20
if z < 10:
    print("z is less than 10")
elif z < 15:
    print("z is less than 15")
elif z < 25:
    print("z is less than 25")
else:
    print("z is greater than or equal to 25")


# ### B. Loops

# #### For Loops

# The `for` statement allows you to iterate over, and do something with, each item in a sequence. For a simple example, iterate over a list of numbers, calculate the square, and store the results in a new list: 

# In[52]:


# First, we create the list we want to loop through
a = [1, 2, 3, 4, 5]
# Next, we create an empty list which we will add new values to
a_squared = []

# Here, we create the loop. "number" can be called anything and is just a name given to each value of a that we loop through
for number in a: 
    a_squared.append(number**2) # Adds the square of each original value of a to the new list

a_squared


# You can also make use of the `range()` function in Python to quickly generate an ordered sequence of numbers. Ranges can be included within the structure of a `for` loop like so:

# In[53]:


r = range(6)
for number in r:
    print(number)


# And to view all of the numbers in a range, we can call the `list` function:

# In[54]:


list(r)


# The `range` function takes three optional arguments: `start`, `stop`, and `step`. For instance, we can generate all multiples of 10 from 100 to 200 below. Note that like slicing above, the `stop` number is excluded, so we set `stop=201` to make sure 200 is included.

# In[55]:


tens = range(100, 201, 10)
list(tens)


# #### While Loops

# A `while` loop will iterate until a condition is met. Be careful, as it can be easy to write a `while` loop with a condition that is never met, leaving your code running indefinitely in an infinite loop.
# 
# In this case, we continually increment the value of `b` by 1 until the `while` condition is no longer met.

# In[56]:


b = 0
while b < 5:
    print("b is {}".format(b)) # format() takes one or more arguments, in this case b, and inserts them between brackets {} when printing.
    b += 1 # This is a more concise way of writing b = b + 1. We could do the same with any operator (-=, *=, /=, etc.)


# ### C. List and Dict Comprehension

# List comprehensions can provide a more concise way of coding a `for` loop. They are also often faster than `for` loops, due to their underlying implementation in Python.
# 
# Rewriting the prior `for` loop as a list comprehension:

# In[57]:


a = [1, 2, 3, 4, 5]

# Again, we can use any name instead of "number"; see for yourself what happens when we change "number" to anything else.
a_squared = [number**2 for number in a]

a_squared


# Conditional logic can also be added to list comprehensions. For instance, let's say we only want the words in a list that start with 's'.
# 
# Here's how we would do that with a traditional for loop:

# In[58]:


words = ['salamander', 'gecko', 'snake']
s_words = []

# This time, we use "word" to signify that we loop over every word in the list "words". As always, we can use any name we want in place of "word".
for word in words:
    if word.startswith('s'):
        s_words.append(word)

s_words


# The list comprehension version of this can be done in just one line!

# In[59]:


words = ['salamander', 'gecko', 'snake']
s_words = []

s_words = [word for word in words if word.startswith('s')]
s_words


# #### Dictionary Comprehension

# You can use similar syntax to create a dictionary as well. 

# In[60]:


a = [1, 2, 3, 4, 5]

squares_dict = {number:number**2 for number in a}

squares_dict[2]


# ## 6. Functions, Methods, and Modules

# ### A. Functions

# - Functions are collections of code that when called cause certain actions. They are one of the most important tools for your programming projects, as they make your work flexible, extensible, and replicable. 
# 
# - We define a function in Python using the `def` statement. What the function gives back is declared using the `return` statement. We'll take a simple math function and translate it to code:
# $$f(x, y, z) = x^3 + y^2 + z$$

# In[61]:


def simple_function(x, y, z):
    return x**3 + y**2 + z

simple_function(1, 2, 3)


# Functions in Python can have multiple return statements that depend on `if/elif/else` logic

# In[62]:


def greater_than_y(x, y):
    if x > y:
        return True
    else:
        return False
    
greater_than_y(5, 10)


# A function can also return multiple items.

# In[ ]:


def return_multiple(a, b, c):
    return a**3, b**2, c

return_multiple(2,3,4)


# We can unpack the results of this function into multiple variables.

# In[ ]:


a, b, c = return_multiple(2, 3, 4)

print("a is {}, b is {}, and c is {}".format(a, b, c))


# ### B. Methods
# 
# - Methods are a type of function that belong to certain objects or data structures. For instance, `sort()` is a method belonging to the `list` object.
# 
# - Methods are called using the following syntax:
# `object_name.method_name()` where any arguments of the method go inside the parentheses. Below are a few more examples of methods built into Python objects:

# In[ ]:


astr = 'Hello World!'
astr.lower()


# In[ ]:


astr.split(' ')


# In[ ]:


alist = [3, 2, 1]
alist.insert(4, 0)
alist


# ### C. Modules
# - Modules contain additional functions or sets of functions beyond what is included in base Python. Similar to libraries in R, there are modules in Python for almost everything: data import, wrangling, visualization, modeling, web scraping, text analysis, and much, much more. 
# 
# - We have to import modules before we can use them, typically at the top of a script or in the first cell of a Jupyter notebook. Once a module is imported, you can use all of its associated functions. Here is an example using the widely-used numpy module:

# In[ ]:


import numpy
numpy.arange(10)


# Modules can be given nicknames upon import so that we don't have to type out their full name every time we use a function. Certain modules have generally-agreed upon nicknaming conventions (e.g. numpy -> np, pandas -> pd), but you can pick any name you want.

# In[ ]:


import numpy as np
np.arange(10)

