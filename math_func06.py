from math import tan,radians
 
def main(x,y):
  answer = x*tan(radians(y))
  return round(answer,2)