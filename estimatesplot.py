# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:01:20 2023

@author: DELL
"""
import matplotlib.pyplot as plt
import statistics 
Estimates=[100,1200,3422,748,666,1209,821,77,300,27,854,982]
y=[]
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(statistics.mean(Estimates),[5],'ro')
plt.plot(statistics.median(Estimates),[5],'bs')
plt.plot(Estimates,y,'r--')
plt.plot([100],[5],'g^')



