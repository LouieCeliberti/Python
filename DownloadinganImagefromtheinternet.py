#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:27:15 2017

@author: louiemceliberti
"""

import random
import urllib.request

def downloadingaimage(url):
    filename = random.randrange(1,20)
    fullname = str(filename) + ".jpg"
    urllib.request.urlretrieve(url,fullname)
    
    downloadingaimage("https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F3%2F30%2FJava_programming_language_logo.svg%2F1200px-Java_programming_language_logo.svg.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJava_(programming_language)&docid=ty8cA0ylPEPayM&tbnid=hJjpV1kl6bvcUM%3A&vet=10ahUKEwjJzIH447zWAhVj7YMKHZLDBr8QMwhnKAAwAA..i&w=1200&h=2200&safe=active&client=safari&bih=1019&biw=1920&q=java&ved=0ahUKEwjJzIH447zWAhVj7YMKHZLDBr8QMwhnKAAwAA&iact=mrc&uact=8")