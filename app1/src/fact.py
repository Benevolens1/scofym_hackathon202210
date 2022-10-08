import sys
""" 
#### factorial function example ### 
 fact n 
 n integer number
 commande_type fact
 args : n , positive integer 
 in  case of of negative return 0
"""

def factorielle(a):
    if a < 0:
        return 'undefined'
    p = a
    if a == 0:
        return 1
    for i in range(1, a):
        p *= i
    return p

def cmd_fact(n):
    return str(factorielle(n))