import math

def pythago(a,b):
    return math.sqrt(a*a + b*b)

class vector:
    def __init__(self,magnitude,direction):
        self.magnitude = magnitude
        self.direction = direction
        self.radian = self.direction * math.pi/180
        self.components = [self.magnitude * math.cos(self.radian), self.magnitude * math.sin(self.radian)]
    
    def __str__(self):
        return f"{self.magnitude} :  {self.direction}'"
    
    def negative(self):
        return vector(-1*self.magnitude, self.direction)

sample = vector(1, 0)

def add_vector(a,b):
    if type(a) != type(sample) or type(b) != type(sample):
        return None
    result_components = [a.components[0] + b.components[0], a.components[1] + b.components[1]]
    result = vector(pythago(result_components[0], result_components[1]), 180/math.pi * (math.atan(result_components[1]/result_components[0])))
    return result

def subtract_vector(a,b):
    return add_vector(a, b.negative())

A = vector(3, 0)
B = vector(6, 60)
print(subtract_vector(B, A))