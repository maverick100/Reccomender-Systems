#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:13:07 2019

@author: abhijithneilabraham
"""
import csv
import random
import pandas as pd

x=[]

def get_id(n):
    print('enter all the customer ids')
    for i in range (n):
        x.append(input())
    return x

'''
print(get_id(m))  
'''
rating=[]

def get_rating():
    print('enter the ratings in range 1 to 10')#Let this print statement stay here for future uses when I dont use random numbers
    for i in range(1,10):
        
        print('enter the rating for question%d'%(i))
        a=random.randint(1,10) #generating random values for ratings
        if a<=10 and a>0:           
            rating.append(a)
        else:
            raise Exception('invalid rating.enter a value between 1 and 10')
    return rating
'''
print(get_rating())
'''
print('enter the number of customers')
m=int(input())
def customer_details():
    id=get_id()
    for customer in range(m):
        id_cust=id[customer]
        rat=get_rating()
        mf=random.randint(0,1)
        csv_columns={'id','rating','M/F'}
        with open('customer.csv','w',newline='') as csvfile:
            writer=csv.writer(csvfile,delimiter=',')
            
        
        
        
    