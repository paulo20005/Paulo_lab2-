class Circle:
    def __init__(self, x, y, radius):
        # Kontrollerar att radien är ett giltigt nummer
        if type(radius) not in [int, float]:
            raise TypeError("Radien måste vara ett nummer")
        self.x = x
        self.y = y
        self.radius = radius
        
    @property #read only för area
    def area(self):
        return 3.14 * self.radius * self.radius
    
    @property #read only för omkrets
    def perimeter(self): 
        return 2 * 3.14 * self.radius
    
    #translate/flytta cirkel
    def translate(self, dx, dy):
        if type(dx) not in [int, float] or type(dy) not in [int, float]: # om dx eller dy inte är nummer
            raise TypeError("dx och dy måste vara nummer")
        self.x += dx 
        self.y += dy


        # equal/lika med
        def __eq__(self, other):
             return self.radius == other.radius #kollar bara radien för att kolla om cirklarna är lika stora
        
        # greater than/större än
        def __gt__(self, other):
             return self.radius > other.radius #kollar om radien är större än den andra cirkeln
        # less than/mindre än
        def __le__(self, other):
            return self.radius <= other.radius
        #större än eller lika med
        def __ge__(self, other):
            return self.radius >= other.radius
        
