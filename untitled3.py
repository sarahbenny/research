#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:58:48 201

@author: sarahbenny
"""
filename= open( 'file2.txt', 'r')
Zn_list=[]
Cl_list=[]
O_list=[]
H_list=[]

for line in filename:
    s=line.split()
    if s[0] == 'Zn':
        Zn_list.append(line)
        print(Zn_list)
        if s[0] == 'Cl':
             Cl_list.append(line)
             print(Cl_list)
        if s[0] == 'O':
             O_list.append(line)
             print(O_list)
        if s[0] == 'H':
            H_list.append(line)
            print(H_list)  