"""
Medium difficulty

Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
and last element of that pair. For example, car(cons(3, 4)) returns 3, 
and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.

// personal note //
This was a bit of a doozy. I think I now grasp the inner functions a bit more and how
a returned function that wasn't called, maintains access to the variables that the 
outer function had. 

"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def first(a,b):
        print(a)
        return a
    
    f(first)


def cdr(f):
    def last(a,b):
        print(b)
        return b
    
    f(last)


car(cons(3, 4))

cdr(cons(3, 4))