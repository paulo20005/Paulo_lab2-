from circle import Circle
from rectangle import Rectangle

circle1 = Circle(x=0, y=0, radius=1) # unit circle
circle2 = Circle(x=1, y=1, radius=1)
rectangle = Rectangle(x=0, y=0, width=1, height=1)

print(circle1 == circle2) # True
print(circle2 == rectangle) # False

circle1.translate(5, 3) # moves its center 5 points in x and 3 points in y

try:
    circle1.translate("THREE", 5) # raise TypeError with an appropriate message
except TypeError as e:
    print(f"TypeError: {e}")

circle3 = Circle(x=0,y=0,radius=3) # a circle with center 0,0 with radius 3
print(circle3 >= circle1) # True

try:
    rectangle2 = Rectangle(x=0,y=0,width=3, height="5") # raise TypeError
except TypeError as e:
    print(f"TypeError: {e}")