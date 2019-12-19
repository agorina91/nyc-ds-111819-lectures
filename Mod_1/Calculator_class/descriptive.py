#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5

"""

# Your Turn:
# Now you are going to work with a partner to create a class. 
# Your class will construct a descriptive statistics calculator using our functions from earlier.

# Your class should have the following attributes:

# .data - where you will hold your data
# .length - that tells you the length of your data list
# .mean
# .median
# .variance
# .stand_dev
# Your class should have the following methods:

# .add_data() - which can take in  a list of values and extend the .data attribute
# .remove_data() accept a list of numbers and remove any of the numbers in that list from your object data


   #pass
# import math
# #, length, mean, median, variance, stand_dev

# class Calculator:
#     def __init__(self, data):
#         self.data = sorted(data)
#         self.length = len(data)
#         self.mean = self._mean()
#         self.median = self._median()
#         self.variance = self._variance()
#         self.stand_dev = self._stand_dev()
    
#     def add_data(self, new_data):
#         self.data.extend(new_data)
        
#     def remove_data(self, new_data):
#         for number in new_data:
#             if number in self.data:
#                 self.data.remove(number)
    
#     def _mean(self):
#         return sum(self.data)/self.length

#     def _median(self):
#         if self.length%2 == 0:
#             mid_left = self.data[self.length // 2 -1]
#             mid_right = self.data[self.length // 2 ]
#             avg = (mid_left + mid_right) / 2
#         else:
#             avg = self.data[self.length // 2] 
#         return avg

#     def _variance(self):
#          return sum([(x - self.mean)**2 for x in self.data])/(self.length-1)

#     def _stand_dev(self):
#          return self.variance**(0.5)

import math
#, length, mean, median, variance, stand_dev

class Calculator:
    def __init__(self, data):
        self.data = sorted(data)
        self.recalc()
    
    def add_data(self, new_data):
        
        self.data.extend(new_data)
        self.data = sorted(self.data)
        print(self.data)
        self.recalc()
        
    def remove_data(self, new_data):
        for number in new_data:
            if number in self.data:
                self.data.remove(number)
            
            
        self.recalc()
    
    def _mean(self):
        return sum(self.data)/self.length

    def _median(self):
        if self.length%2 == 0:
            mid_left = self.data[self.length // 2 -1]
            mid_right = self.data[self.length // 2 ]
            avg = (mid_left + mid_right) / 2
        else:
            avg = self.data[self.length // 2] 
        return avg

    def _variance(self):
         return sum([(x - self.mean)**2 for x in self.data])/(self.length-1)

    def _stand_dev(self):
         return self.variance**(0.5)
        
    def recalc(self):
        
        self.length = len(self.data)
        self.mean = self._mean()
        self.median = self._median()
        self.variance = self._variance()
        self.stand_dev = self._stand_dev()




