#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:40:46 2017

@author: louiemceliberti
"""
def readfile():
    try:
        file = open("Student.txt","a")
        file.write("Hello World \n")
        file.close()
    except Exception:
        print("error")
        
readfile()        