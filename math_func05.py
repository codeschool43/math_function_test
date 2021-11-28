from math import cos,radians
 
def main(x,y):
  answer = x*cos(radians(y))
  return round(answer,2)