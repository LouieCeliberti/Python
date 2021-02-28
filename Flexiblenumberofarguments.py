#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 21:07:18 2017

@author: louiemceliberti
"""

def numbers(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)
        
numbers(39)
numbers(5,9238,85)
numbers(4207,45486689)
numbers(2,683,461)      