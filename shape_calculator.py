# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:42:17 2023

@author: johan
"""
class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
  def set_width(self,width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'

    pic = '*' * self.width + '\n'
    pic = pic * self.height
    return pic



  
  def get_amount_inside(self, ob):
    return self.get_area() // ob.get_area()
    
class Square(Rectangle):

  def __init__(self, s):
    super().__init__(s, s)

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, s):
    self.width = s
    self.height = s
 
 