"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time 
and constant space. In other words, find the lowest positive integer that does not exist
in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


// Personal notes //
I don't know if there is something here that I'm not seeing, or if python 
actually makes this a very simple problem to solve, but this was really easy.
Even though the problem was rated as hard.

Perhaps this is super inefficient for super large arrays where it would literally have to 
count 1 by 1 forever to get it. But then I'm not sure if there is some better way to figure
this out. 
"""


def missing_integer(arr):
    n = 1
    while True:
        if n not in arr:
            print(n)
            return n
        else:
            n += 1

missing_integer([3, 4, -1, 1])
missing_integer([1, 2, 0])
