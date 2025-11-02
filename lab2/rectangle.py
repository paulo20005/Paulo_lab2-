class Rectangle:
    def __init__(self, x, y, width, height):
        if type(width) not in [int, float] or type(height) not in [int, float]:
            raise TypeError("Bredd och höjd måste vara nummer")
        if width <= 0 or height <= 0:
            raise ValueError("Bredd och höjd måste vara positiva")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property #read only för area
    def area(self):
        return self.width * self.height
  
    @property #read only för omkrets
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    #translate/flytta rektangel
    def translate(self, dx, dy):
        if type(dx) not in [int, float] or type(dy) not in [int, float]:
            raise TypeError("dx och dy måste vara nummer")
        self.x += dx
        self.y += dy

    #equal/lika med
    def __eq__(self, other):
        if not isinstance(other, Rectangle): return False #isinstance gör att rektangel kan bara jämföras med rektangel 
        return self.width == other.width and self.height == other.height

    #less than/mindre än
    def __lt__(self, other):
        if not isinstance(other, Rectangle): return False
        return self.area < other.area

    #greater than/större än
    def __gt__(self, other):
        if not isinstance(other, Rectangle): return False
        return self.area > other.area

    #less than or equal/mindre eller lika
    def __le__(self, other):
        if not isinstance(other, Rectangle): return False
        return self.area <= other.area

    #greater than or equal/större eller lika
    def __ge__(self, other):
        if not isinstance(other, Rectangle): return False
        return self.area >= other.area
    
    def __repr__(self):#skriva ut för kodaren
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"
    
    def __str__(self):#skriv ut rektangelns position, bredd och höjd för användaren
        return f"Rektangel på position ({self.x}, {self.y}) med bredd {self.width} och höjd {self.height}"
   
    #checkar om rektangeln är en kvadrat
    def is_square(self):
        return self.width == self.height
    