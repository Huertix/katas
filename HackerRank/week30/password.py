#!/bin/python

import sys
import random

consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiou'


def generate_password(result):
    if not result:
        return list(consonants) + list(vowels)

    if len(result) <=1:
        new_result = []
        letters = consonants
        if result[0][-1] in consonants:
            letters = vowels

        for i in letters:
            new_result.append(result[0]+i)
        return new_result

    half = len(result)/2
    left =  generate_password(result[:half])
    right = generate_password(result[half:])
    return right + left
    


n = int(raw_input().strip())

if n < 1: n = 1
if n > 6: n = 6

letters = [consonants, vowels]
option = random.randint(0, 1)

result = []

for x in range(0, n):
    result = generate_password(result)
    option = not option

for item in result:
    print item










# # abc = string.lowercase
# consonants = 'bcdfghjklmnpqrstvwxz'
# vowels = 'aeiou'

# letters = [consonants, vowels]

# option = random.randint(0, 1)

# result = product(letters[option], letters[not option], repeat=n)

# for item in result:
#     print item







# result = itertools.izip_longest(consonants, vowels, '-')
# for i in result:
#     word = ''
#     for w in i:
#         word = word + w

#     print word


# def product(*args, **kwds):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = map(tuple, args) * kwds.get('repeat', 1)
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)

# def izip_longest(*args, **kwds):
#     # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
#     fillvalue = kwds.get('fillvalue')
#     counter = [len(args) - 1]
#     def sentinel():
#         if not counter[0]:
#             raise ZipExhausted
#         counter[0] -= 1
#         yield fillvalue
#     fillers = repeat(fillvalue)
#     iterators = [chain(it, sentinel(), fillers) for it in args]
#     try:
#         while iterators:
#             yield tuple(map(next, iterators))
#     except ZipExhausted:
#         pass

# def izip(*iterables):
#     # izip('ABCD', 'xy') --> Ax By
#     iterators = map(iter, iterables)
#     while iterators:
#         yield tuple(map(next, iterators))


# result = itertools.product(range(2), repeat=n)
# # result = itertools.izip_longest(consonants, vowels, '-')
# index = 0
# for i in result:
#     word = ''
#     for w in i:
#         word = word + str(w)

#     print word + ' => ' + str(index) 
#     index = index + 1


# if first in ('a', 'e', 'i', 'o', 'u'):

# original = raw_input('Enter a word:')
# word = original.lower()
# first = word[0]

# if len(original) > 0 and original.isalpha():
#     if first in 'aeiou':
#         print "vowel"
#     else:
#         print "consonant"
# else:
#     print "empty"