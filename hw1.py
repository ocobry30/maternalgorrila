# Name: Bryan O'Connor
# Evergreen Login: Ocobry30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1

b = -5.86

c = 8.5408

import math

x1= (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

x2= (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print x1, x2


###
### Problem 2
###

print "Problem 2 solution follows:"

from hw1_test import a, b, c, d, e, f

print a, "\n", b, "\n", c, "\n", d, "\n", e, "\n", f, "\n"



###
### Problem 3
###

print "Problem 3 solution follows:"

print ((a and b) or (not c) and not (d or e or f)) 
 
 


###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
