#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:55:14 2017

@author: louiemceliberti
"""

def sentence(name = 'Neil', verb = 'ran', distance = 500, miles = 'miles'):
    print(name,verb,distance,miles)
    
sentence()    
sentence(distance = 100,miles = 'feet')
sentence(name = 'Bill')
sentence(name = 'Sam',distance = 402,miles = 'meters')