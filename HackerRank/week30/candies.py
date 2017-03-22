#!/bin/python

import sys


# n,t = raw_input().strip().split(' ')
# n,t = [int(n),int(t)]
# c = map(int, raw_input().strip().split(' '))
# your code goes here


t = 4 # time
n = 8 # candies
c = [3, 1, 7, 5] # 

if n < 5:
	n = 5
if n > 100:
	n = 100
if t < 1:
	t = 1
if t > 100:
	t = 100

total_cadies_replaced = 0
candies_in_the_bowl = n


for index in range(0,t-1):
	candies_in_the_bowl = candies_in_the_bowl - c[index]
	if candies_in_the_bowl < 5:
		candies_to_be_replaced = n - candies_in_the_bowl
		candies_in_the_bowl = n 
		total_cadies_replaced = total_cadies_replaced + candies_to_be_replaced

		
print total_cadies_replaced


