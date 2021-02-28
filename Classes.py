#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:54:10 2017

@author: louiemceliberti
"""
studentlist = []

class Student:
    def addstudent(name):
        student = {"name":name}
        studentlist.append(student)
        
student = Student()
student.addstudent("baert")
print (studentlist)       
        