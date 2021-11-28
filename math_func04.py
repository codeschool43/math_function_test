from math import sin,radians
 
def main(x,y):
   answer = x*sin(radians(y))
   return round(answer,2)