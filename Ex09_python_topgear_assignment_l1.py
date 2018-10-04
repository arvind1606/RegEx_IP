#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:48:11 2018

@author: arv
"""

import re

# Input String
input = '''
Interface		IP-Address	      OK? 	Method     Status	Protocol
 
FastEthernet0/0	192.168.1.242	  YES 	manual     up	     up 
FastEthernet1/0  unassigned	      YES 	unset      down 
Serial2/0        192.168.1.250	  YES 	manual     up	     up 
Serial3/0        192.168.1.233	  YES 	manual     up	     up 
FastEthernet4/0  unassigned	      YES 	unset      down	
FastEthernet5/0  unassigned	      YES    unset     down
'''

# Using Regular Expression
print ("\n\n\n")
for line in input.splitlines():    	
    matchObj = re.match( r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+(\w+\s?\w+?)+', line)
    if matchObj:
        print  (matchObj.group(1),",",matchObj.group(2),matchObj.group(3),"\n")
print ("\n\n\n" )