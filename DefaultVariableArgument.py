#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:34:08 2017

@author: louiemceliberti
"""

def gender(sex = 'Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

gender('m')    
gender('f')
gender()
gender('f')
        