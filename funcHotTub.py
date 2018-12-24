#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:10:38 2018

@author: Laura
"""

# basic hot tub

from pulp import *

def hotTubFunc(c1=350):
    hotTubLP = LpProblem('Hot Tub LP',LpMaximize)
    
    # Variables
    xHydros = LpVariable('Hydros',0)
    xAquas = LpVariable('Aquas',0)
    
    # Objective
    hotTubLP += c1*xAquas + 300*xHydros, "Profit"
    
    # Constraints
    hotTubLP += 9*xAquas + 6*xHydros <= 1566, 'Labor'
    hotTubLP += 1*xAquas + 1*xHydros <= 200, 'Pumps'
    hotTubLP += 12*xAquas + 16*xHydros <= 2880, 'Tubing'
    
    # Solve
    hotTubLP.solve()
    
    # Display results
    print("Status:", LpStatus[hotTubLP.status])
    for variable in hotTubLP.variables():
        print(variable.name,"=",variable.varValue)
    print("Total Profit = ",value(hotTubLP.objective))    

    return(hotTubLP)

def hotTubTester(hotTubLP):
    # Known solution info
    TOL = 1e-4
    soln = {'status': 1,
            'variables': {122.0, 78.0},
            'objValue': 66100.0}
    errs = False
    
    varVals = {v.varValue for v in hotTubLP.variables()}
    if len(soln['variables']) != len(varVals):
        print("Incorrect number of variables."); errs = True
    elif max([abs(i-j) for (i,j) in zip(varVals,soln['variables'])]) > TOL:
        print("Some variables differ."); errs = True
    
    if soln['status'] != hotTubLP.status:
        print('Incorrect status.'); errs = True
    
    if abs(soln['objValue'] - value(hotTubLP.objective)) > 1e-4:
        print('Incorrect objective value.'); errs = True
    
    if not(errs):
        print('No errors!')
    
    