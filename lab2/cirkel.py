class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    @property #read only för area
    def area(self):
        return 3.14 * self.radius * self.radius
    
    @property #read only för omkrets
    def perimeter(self): #
        return 2 * 3.14 * self.radius