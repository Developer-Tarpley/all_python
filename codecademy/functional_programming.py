'''
Functional Programming in Python

An intro to functional programming in Python
Introduction

In this article, we will explore the concept of functional programming, including its differences from object-oriented programming.

This article is divided into the following sections:

    Introduction to functional programming
    Functional vs. object-oriented programming
    Declarative vs. imperative programming
    Writing functions in functional programming
    Using recursion instead of loops
    Passing functions as arguments to other functions
    Conclusion

Introduction to functional programming

Functional programming is a programming paradigm in which code is structured primarily in the form of functions. The origins of this programming style arise from a branch of mathematics known as lambda calculus, which is the study of functions and their mathematical properties. In contrast to the popular object-oriented and procedural approaches, functional programming offers a different way of thinking when solving a problem.

Let’s explore how to program solutions in a functional style using Python.
Functional vs. object-oriented programming

In object-oriented programming (OOP), you structure your code based on the concept of objects. In commonly used OOP languages (such as Java or C#), we create a template for an object using the keyword class, and we instantiate an object by using the keyword new. These objects contain fields that store data and methods that manipulate data. In this style, an object can be passed as an argument in the function of another object.

In functional programming, you create a solution by structuring code mainly using functions. Functions are “first-class citizens” in this paradigm, meaning we can use them to store and manipulate data (with limitations). Similar to objects in object-oriented programming, in functional programming, functions can be passed in as arguments to other functions and can be returned by other functions.
Declarative vs. imperative programming

Before we learn of the advantages functional programming offers, we must first discuss the differences between an imperative paradigm and a declarative paradigm.

Imperative programming solves a problem by describing the step-by-step solution. Imperative programming is concerned with “how to solve a problem.”

In contrast, declarative programming relies on the underlying framework or programming language to solve a problem. The programmer’s only task is to describe what problem they would like solved. Declarative programming is concerned with “what problem to solve.”

As an analogy, consider the example of obtaining a cup of coffee. Imperative programming would be the equivalent of you making the cup of coffee yourself by performing the following steps:

    Take out your coffee pot.
    Load the pot with the coffee grounds.
    Add water to the coffee pot.
    Place the coffee pot on the stove.
    Turn stove on.
    Wait until coffee is done.
    Pour coffee into a cup.
    Do you like sugar?
        If yes, add sugar.
        If no, do not add sugar.
    Drink coffee.

Declarative programming is the equivalent of going to your local coffee shop and telling the barista, “I’d like a cup of coffee with one teaspoon of sugar, please.” The barista prepares your coffee, gives you the cup, and you drink it without concerning yourself with the details of how it was made.

For a programming analogy, consider the example of having to sort a list in Python. Imperatively sorting the list would be you implementing a sorting algorithm like this:

lst = [8, 4, 14, 9, 12, 5, 7, 1, 10, 2, 3]

# Sort using Selection Sort algorithm
for i in range(len(lst)):
  min_idx = i
  for j in range(i+1, len(lst)):
    min_idx = j if lst[j] < lst[min_idx] else min_idx
  temp = lst[i]
  lst[i] = lst[min_idx]
  lst[min_idx] = temp

If we were to solve the list declaratively in Python, we would call the list.sort() function like so:

lst = [8, 4, 14, 9, 12, 5, 7, 1, 10, 2, 3]

list.sort(lst)

Which style a programmer follows might depend on their goals. If you are looking for concise code that gets you an answer efficiently, you might go with a more declarative approach. If you are working with other people and want to ensure that your code is easy to follow, you may choose a more imperative style.

OOP and procedural programming follow an imperative approach; functional programming follows a declarative approach.
Writing functions in functional programming.

As we said in the introduction to this article, the central concept in functional programming is that of a function; however, there are requirements that a function must adhere to when writing one. The first of these requirements is the function must be deterministic. That is, for any given input, the function must return the same output when provided with the same set of inputs. Let’s illustrate this with the following example of an add function:

def add(x, y):
  return x + y

This function will always return 7 if add(5, 2) is called.

Another of these requirements is that functions must be free of as many side effects as possible. A side effect is when a function alters some external variable. The goal is to minimize, not eliminate, side effects. It would be impossible to eliminate all side effects in a function because a program eventually must have an external effect to be useful.

A pure function is defined as a deterministic function with no side effect.

Consider this example:

ans = 0

def add(x, y): # This function has side effects
  ans = x + y

The add(x, y) function defined in this way has a side effect because it alters the external variable ans.

To make this a pure function, we should write this as:

ans = 0
def add(x, y): # This function has no side effects
  return x + y

ans = add(x, y)

Notice how the add(x, y) function no longer alters the ans variable during its execution. Also, the variables x and y only exist within the scope of the function. Operating on them allows the function to have no side effects.

For reusability, a function should always have all relevant parameters passed in and should not rely on global variables.

Consider the example of a function (app()) that replaces the first and last element of a list with 0:

lst = [1,2,3,4,5]

def app():
  ret = list(lst)
  ret[0] = 0
  ret[-1] = 0
  return ret

zero_list = app()

Writing a function in this way makes it dependent on an external list variable called lst. The function is not reusable as using it elsewhere requires lst to be defined externally. While it is not reusable, app() is still considered free of side effects as it reads, but does not modify, the variable lst. A better way to write the function would be to pass in the required list variable as an argument like so:

lst = [1,2,3,4,5]

def app(l):
  ret = list(l)
  ret[0] = 0
  ret[-1] = 0
  return ret

zero_list = app(lst)

The app(l) function is free of side effects and is now also reusable.

We care about pure functions because as our programs get more complex, we want to avoid incorrect alterations of external variables. For example, if we call functions from different threads running concurrently, we need to construct our functions carefully to avoid side effects. Following the functional programming paradigm is a great way to keep code clean and efficient and simplify testing.
Using Recursion Instead of Loops

To execute a section of code repeatedly, object-oriented programmers use a while loop or a for loop. Loops do not adhere to the functional programming style because they maintain an external counter which is altered from inside the loop (side effect!). In functional programming, we use recursion to execute code repeatedly. Recursive functions are typically written in the following style:

def recursive_function(n):
  # Base case to terminate recursion goes here
  # Call to recursive_function with new parameter goes here

The classic example of a recursive function is the computation of the nth Fibonacci number done like so:

def fib(n):
  if n <= 1:
    return 1
  return fib(n-1) + fib(n-2)

Passing functions as arguments to other functions

In traditional OOP, you can pass objects as arguments to a function. In functional programming, you can pass functions as arguments to other functions. This is known as treating functions as first-class citizens, a term you may often see in industry.

Let’s take a look at an example:

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def times3(a, b, function):
  return 3 * function(a, b)

add_then_times3 = times3(2, 4, add) # 18
sub_then_times3 = times3(2, 4, sub) # -6

This code defines a times3() function that multiplies the result of an add or subtract (sub) function by three and returns the value. The times3() function also allows the passing of any other function that accepts two parameters and returns an integer.

Functional programming promotes the concept of brevity when writing code. It is important to be concise and write functions in as few lines as possible as long as readability is maintained. We can also pass a function to another function by writing it in the argument using a lambda.

We can shorten the previous code using a lambda like so:

def times3(a, b, function):
  return 3 * function(a, b)

add_then_times3 = times3(2, 4, lambda x, y: x + y) # 18
sub_then_times3 = times3(2, 4, lambda x, y: x - y) # -6

This will output the same result as the verbose implementation from earlier. Lambdas are a great tool as they allow a programmer to write a function while maintaining the flow of ideas. A programmer is no longer required to stop, write a function elsewhere, and then resume work. A drawback of lambdas is that they are only suitable for implementing simple functions; it is not possible to write all functions as lambdas!
Conclusion

In summary, functional programming is a powerful paradigm that confers many advantages. In this paradigm, we structure solutions in the form of functions. Functional programming differs from object-oriented programming. It follows a declarative style as opposed to an imperative style leading to code that is shorter, easier to test, less prone to bugs, and well-suited for multithreading applications. Many languages allow for implementing the functional programming paradigm; one of the more popular ones is Python.
'''