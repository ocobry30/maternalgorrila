# Name: Bryan O'Connor
# Evergreen Login: ocobry30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2



###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"
from hw2_test import n

i = 0
sum = 0

while(i <= n):
    sum = sum + i
    i = i + 1 
    
print sum

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

nom = 2.0
rep = 0.0

while(nom < 10):
    rep = 1 / nom
    print rep
    nom = nom + 1

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (0, n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
factorial = 1

for i in range (1, n+1):
    factorial = factorial * i
    
print n,   

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"


lines = 10


for i in range (0, lines):
    factorial = 1
    n = lines - i
    for j in range (1, n + 1):
        factorial = factorial * j
        
    print factorial

    
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
    
n = 10
ln = 0.0

for i in range (1, n + 1):
    factorial = 1.0
    for j in range (1, i + 1):
        factorial = factorial * j
        
    ln = ln + (1 / factorial)
    
ln = ln + 1

print ln

##colab josh alejandro kevin

###reflection: my canopy acts messed up sometimes but my terminal worked I dont understand
