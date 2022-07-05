import math

x, y, x1, y1, x2, y2 = map(int, input().split())
 
a = ( ((x - x1) * (x2 - x1)) + ((y - y1) * (y2 - y1)) ) / ( pow(x2 - x1, 2) + pow(y2 - y1, 2) )
if a < 0: a = 0

res = math.sqrt( pow((x1 - x) + (a * (x2 - x1)), 2) + pow((y1 - y) + (a * (y2 - y1)), 2) )
print("added smthng")
print("hehe")
