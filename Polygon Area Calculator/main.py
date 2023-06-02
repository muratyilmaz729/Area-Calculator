# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:42:07 2023

@author: johan
"""
# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator


rect = shape_calculator.Rectangle(5, 10)
print("\n\nRectangle Description: ",rect.__str__())
print("\n\nRectangle Area", rect.get_area())
rect.set_width(3)
print("Rectangle's width is 3 now.")
print(rect)
print("\n\nRectangle Perimeter:",rect.get_perimeter())

sq = shape_calculator.Square(9)
print("\n\nNew Square object is created its side:9 and area:" ,sq.get_area())
sq.set_side(3)
print(sq)
print("\n\nThe square's side changed to 3. ITs diagonal length is:",round(sq.get_diagonal(),2))

print("\n\nRectangle's Picture with * representation:\n") 

print(rect.get_picture())

print("\n\nSquare's Picture with * representation:\n")
print(sq.get_picture())

print(f'\n\nOur rectangle can get {rect.get_amount_inside(sq) } 1 square specified inside ')