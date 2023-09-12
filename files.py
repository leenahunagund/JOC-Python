# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:31:33 2023

@author: DELL
"""

with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("i am fine")
myfile.close()
# r, w , a , r+