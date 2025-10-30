class Rectangle:
    def __init__(self, x, y, width, height):
        if type(width) not in [int, float] or type(height) not in [int, float]:
            raise TypeError("Bredd och höjd måste vara nummer")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # read-only för area
    @property
    def area(self):
        return self.width * self.height
  
    # read-only för omkrets
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    # translate/flytta rektangel
    def translate(self,dx,dy):
        if type(dx) not in [int, float] or type(dy) not in [int, float]:
            raise TypeError("dx och dy måste vara nummer")
        self.x += dx
        self.y += dy
    # equal/lika med
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height