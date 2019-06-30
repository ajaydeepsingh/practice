#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def returnFirst(c, d):
        return c
    return pair(returnFirst)

def cdr(pair):
    def returnLast(c, d):
        return d
    return pair(returnLast)



# driver code

print(car(cons(12,23)))
print(cdr(cons(12,23)))
