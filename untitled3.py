#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:58:48 2019

@author: sarahbenny
"""

filename= 'new3.txt'
infile= open(filename, 'r')
line= infile.readline()
Zn_list=[]
Cl_list=[]
O_list=[]
H_list=[]
for line in infile:
    s=line.split()
    for Zn in s:
        Zn_list.append(line)
        print Zn_list
for line in infile:
    l=line.split()
    for Cl in l:
        Cl_list.append(line)
        print Cl_list
for line in infile:
    a=line.split()
    for O in a:
        O_list.append(line)
        print O_list
for line in infile:
    u=line.split()
    for H in u:
        H_list.append(line)
        print H_list

    
   
    
    
    
       
   