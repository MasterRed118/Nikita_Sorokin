# -*- coding: utf-8 -*-
"""Untitled1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HjKbXdHDV8pAVdJlfof46Ily2eAeDivT
"""

# Задача 1 "even or odd"
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/python


a = int(input("ВВедите число: "))

if a == 0: 
   print ("0 по определению чётное число")

if (a % 2) == 0:
   print("Число чётное")
else:
   print ("Число нечётное")