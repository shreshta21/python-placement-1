from collections import namedtuple
import math

point=namedtuple('Point',['x','y'])

point1=point(1,2)
point2=point(4,6)

distance=math.sqrt((point2.x-point1.x)**2+(point2.y-point1.y)**2)
print("distance between point1 and point2:",distance)

