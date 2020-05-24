Lists - Learn Python - Free Interactive Python Tutorial

- [Welcome](http://learnpython.org/en/Welcome)  /

- Lists

Get started learning Python with [DataCamp's](https://www.datacamp.com/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials) free [Intro to Python tutorial](https://www.datacamp.com/courses/intro-to-python-for-data-science/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials). Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. [Start Now](https://www.datacamp.com/courses/intro-to-python-for-data-science/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials)!

 [** Previous Tutorial](http://learnpython.org/en/Variables_and_Types)  [Next Tutorial **](http://learnpython.org/en/Basic_Operators)

# Lists

* * *

Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

- [script.py](http://learnpython.org/en/Lists)
- [IPython Shell](http://learnpython.org/en/Lists)

-
1
2
3
4
5
6
7
8
9
10
11

mylist  =  []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

# prints out 1,2,3

for  x  in  mylist:
 print(x)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 **
[Powered by DataCamp](https://www.datacamp.com/)
Accessing an index which does not exist generates an exception (an error).

- [script.py](http://learnpython.org/en/Lists)
- [IPython Shell](http://learnpython.org/en/Lists)

-
1
2

mylist  =  [1,2,3]
print(mylist[10])

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 **
[Powered by DataCamp](https://www.datacamp.com/)

## Exercise

In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator `[]`. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

- [script.py](http://learnpython.org/en/Lists)
- [IPython Shell](http://learnpython.org/en/Lists)

-
1
2
3
4
5
6
7
8
9
10
11
12

numbers  =  []
strings  =  []
names  =  ["John", "Eric", "Jessica"]

# write your code here

second_name  =  None

# this code should write out the filled arrays and the second name in the names list (Eric).

print(numbers)
print(strings)
print("The second name on the names list is %s"  %  second_name)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 **
[Powered by DataCamp](https://www.datacamp.com/)

* * *

This site generously supported by [DataCamp](https://www.datacamp.com/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials). DataCamp offers online interactive [Python Tutorials](https://www.datacamp.com/courses/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials) for Data Science. Join **over a million** other learners and get started learning Python for data science today!

 [** Previous Tutorial](http://learnpython.org/en/Variables_and_Types)  [Next Tutorial **](http://learnpython.org/en/Basic_Operators)