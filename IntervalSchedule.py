#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 07:52:43 2023

@author: moumenshobaky
@Subject:Interval scheduling solving with greedy algorithm
"""
import random;
intervals = []

for i in range(0,20):
    x = random.randint(1,100);
   
    y= random.randint(x,100);
    intervals.append((x,y));

x = 0;
i = 0;

for pair in intervals :
 
    x = intervals[i][0]
    for j in range(intervals.index(pair),len(intervals)):
     
        if(intervals[i][1] > intervals[j][1]):
            temp = intervals[j]
            intervals[j] = intervals[i]
            intervals[i] = temp
 
    i = i +1;  

#following the notations of the book
R = intervals;

A = [];
i = 0;
j = 0
while len(R) > 0:
   
    if (len(A) > 0 and R[0][0] < A[i-1][1]):
      
        R.remove(R[0])
        j = j +1
        continue
    A.append(R[0])
    R.remove(R[0])
    i =i +1
    j = j+1
    
