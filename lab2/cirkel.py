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
             return self.radius == other.radius #kollar om radien är lika med den andra cirkeln
        
        # greater than/större än
        def __gt__(self, other):
             return self.radius > other.radius #kollar om radien är större än den andra cirkeln
        # less than/mindre än
        def __le__(self, other):
            return self.radius <= other.radius
        #större än eller lika med
        def __ge__(self, other):
            return self.radius >= other.radius
        
        def __repr__(self):# skriva ut för kodaren
            return f"Circle({self.x}, {self.y}, {self.radius})"
        
        def __str__(self):# skriv ut cirkelns position och radie för användaren
            return f"Cirkelns på position ({self.x}, {self.y}) med radie {self.radius}"
         
        def is_unit_circle(self): #kollar om det är enhetscirkel
            return self.radius == 1 and self.x == 0 and self.y == 0
            if self.radius <= 0:
                raise ValueError("Radien kan inte vara mindre än 0")

        
