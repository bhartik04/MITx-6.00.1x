#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Fri Jun 25 15:38:11 2021
    
    @author: bhartikindra
    
    Problem: Given the balance and annualInterestRate,
    find the minimum monthly payment such that final debt is less than 0.
    
    Using Bisection method.

"""


balance=float(input('Enter Outstanding Balance:'))
annualInterestRate=float(input('Enter Annual Interest Rate: '))



def limits(l,u):
    return (l+u)/2


def debt(bal, mpr,air):
    """
        Returns remaining debt after an year
    """
    i=0
    while i<12:
        bal=(bal-mpr)*(1+air/12)
        i=i+1
    return bal
    

def compute(balance, annualInterestRate):
    """
        finds minimum monthly payment so that the final debt is less than 0
    """
    # start0 and end0 are lower and upper possible bounds for the Monthly payment.
    
    start0=balance/12
    end0=balance/12*(1+annualInterestRate)**12
    
    def ideal(start,end,total,air):
        guess=limits(start,end)
        x=debt(total,guess,air)
        
        if x>0:
            start=guess
            
            return ideal(start,end,total,air)
         
        elif x<=(-0.10):   
            end=guess
            return ideal(start,end,total,air)
            
        else:
             return str(round(guess,2))
      
     return ideal(start0,end0,balance,annualInterestRate)  
     
        
print(compute(balance,annualInterestRate))
        
