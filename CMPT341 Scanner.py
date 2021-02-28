# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

words = ["do", "else", "if", "while", None]
ch = ' '
id_name = [None]*100 

def syntax_error(): # method will print syntax error
    print("Syntax error\n")  
    
def next_ch():
    ch = getchar()
    
    
"""
"w" - writing; overwrites the entire file
"r" - reading a text file
"a" - appending to a new or existing file\
"rb" - reading a binary file
"wb" - writing to a binary file
"""    

"""
Tinyc input:
    i = 1;
    while(i<10)
        i=+1;
"""
def read_from_file():
    file = open("/Users/louiemceliberti/Documents/example.c", "r")
    while True:
        token = file.read(1)
        if not token:
            print("End of file")
            break
        print("character: ", token)
    """
    try:
        file = open("/Users/louiemceliberti/Documents/example.c", "r")
        for token in file.read(10):
            if not file.
    except Exception:
        print("cannot read from example.c")
        """

"""
def next_sym():
    switch={
        ' ': next_ch()
       # EOF: next_ch()
        '{': next_ch()
        '}': next_ch()
        '(': next_ch()
        ')': next_ch()
        '+': next_ch()
        '-': next_ch()
        '<': next_ch()
        ';': next_ch()
        '=': next_ch()
        }
    if ch >= '0' and ch <= '9':
        int_val = 0
        while ch >= '0' && ch <= '9':
            int_val *= 10 + (ch - '0')
            next_ch()
        sym = INT
    elif ch >= 'a' and ch <= 'z':
        i = 0
        while (ch >= 'a' and ch <= 'z') or ch == '_':
            id_name[i+=1] = ch
            next_ch()
        id[i] = '\0'
        sym = 0
        while words[sym] not None and strcmp(words[sym], id_name not 0):
            sym +=1 
        if words[sym] == None:
            if id_name[1] == '\0'
                sym = ID
        else:
            syntax_error()
    else:
        syntax_error()
        """
        
read_from_file()