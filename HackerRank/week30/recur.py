#!/bin/python

import sys


n = int(raw_input().strip())

# min(int, min(int, min(int, int)))

min_string = 'min(int, int)'

def add_min(next):
	if next < 2:
		return
	if next == 2:
		return min_string

	return 'min(int, {})'.format(add_min(next-1))

print add_min(n)