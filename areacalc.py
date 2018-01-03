"""This program calculates the area of either a circle or a triangle
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The area calculator is starting up..."

month = now.month
day = now.day
year = now.year
hour = now.hour
minute = now.minute
print '%s/%s/%s  %s:%s' % (month, day, year, hour, minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input ("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C':
  print "The radius of a circle is pi times the radius squared"
  sleep(1)
  radius = float(raw_input ("Input radius: "))
  area = pi * radius ** 2
  print "The pi is baking..."
  sleep(1)
  print 'The area of the circle is %.2f \n%s' % (area, hint)
elif option == 'T':
  print "The area of a triangle is base width times height devided by two"
  sleep(1)
  base = float(raw_input ("Input base: "))
  height = float(raw_input ("Input height: "))
  area = base * height / 2
  print "Uni Bi Trie..."
  sleep(1)
  print 'The area of the triangle is %.2f \n%s' % (area, hint)
else:
  print "I can only do (C)ircles or (T)riangles!"