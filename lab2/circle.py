class Circle:
    def __init__(self, x, y, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Radius måste vara nummer")
        if radius <= 0:
            raise ValueError("Radius måste vara positiv")
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
        if not isinstance(other, Circle): return False
        return self.radius == other.radius #kollar om radien är lika med den andra cirkeln
    
    # greater than/större än
    def __gt__(self, other):
        if not isinstance(other, Circle): return False
        return self.radius > other.radius #kollar om radien är större än den andra cirkeln
    
    # less than/mindre än
    def __lt__(self, other):
        if not isinstance(other, Circle): return False
        return self.radius < other.radius #kollar om radien är mindre än den andra cirkeln
    
    # less than or equal/mindre eller lika
    def __le__(self, other):
        if not isinstance(other, Circle): return False
        return self.radius <= other.radius #kollar om radien är mindre eller lika med den andra cirkeln
    
    # greater than or equal/större eller lika
    def __ge__(self, other):
        if not isinstance(other, Circle): return False
        return self.radius >= other.radius #kollar om radien är större eller lika med den andra cirkeln
    
    def __repr__(self):# skriva ut för kodaren
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def __str__(self):# skriv ut cirkelns position och radie för användaren
        return f"Cirkel på position ({self.x}, {self.y}) med radie {self.radius}"
    
    #checkar om cirkeln är en enhetscirkel
    def is_unit_circle(self):
        return self.radius == 1 and self.x == 0 and self.y == 0
