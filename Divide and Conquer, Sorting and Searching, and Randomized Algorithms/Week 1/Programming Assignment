#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

def get_length(x):
    """multiply the original number with a power of 10 
    to turn its length into a power of 2, returns the number
    after multiplication as well as the length of the added zeros"""
    x = str(x)
    length = len(x)
    log_length = 2**math.ceil(math.log(length,2))
    len_diff = log_length - length
    full_num = int(x)*10**len_diff
    return full_num, len_diff


def mult(n1,n2):
    """the karatsuba multiplication for two integers 
    with the same length, and their lengths are a power of 2"""
    if len(n1)<2 and len(n2)<2:
        return int(n1)*int(n2)
    else:
        length = len(n1)
        len_2 = length//2
        a = n1[:len_2]
        b = n1[len_2:]
        c = n2[:len_2]
        d = n2[len_2:]
        return mult(a,c)*10**length+(mult(a,d)+mult(b,c))*10**len_2+mult(b,d)


def Karatsuba():
    """Karatsuba for any two integer"""
    k_num1 = input("Give me the first integer: ")
    k_num2 = input("Give me the second integer: ")
    
    num1 = abs(int(k_num1))
    num2 = abs(int(k_num2))
    
    if num1 >= num2:
        num1_tuple = get_length(num1)
        diff_4small = len(str(num1))-len(str(num2))+num1_tuple[1]
        num2_tuple = (num2*10**diff_4small,diff_4small)
    else:
        num2_tuple = get_length(num2)
        diff_4small = len(str(num2))-len(str(num1))+num2_tuple[1]
        num1_tuple = (num1*10**diff_4small,diff_4small)
    
    full_multi = mult(str(num1_tuple[0]),str(num2_tuple[0]))
    
    if (int(k_num1) < 0) is not (int(k_num2) < 0):
        return int(-full_multi/(10**(num1_tuple[1]+num2_tuple[1])))
    else:
        return int(full_multi/(10**(num1_tuple[1]+num2_tuple[1])))
