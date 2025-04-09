import math

class Calculator:
    def add(self, a,b):
        return a+b
    
    def substract(self, a,b):
        return a-b
    
    def multiply(self, a,b):
        return a*b
    
    def divide(self, a,b):
        if(b==0):
            raise ValueError("nie dziel przez 0")
        else:
            return a/b
        
    def delta(self, a, b, c):

        delta = b ** 2 - 4 * a * c

        if(delta < 0):
            raise ValueError("delta ujemna")
        elif(delta == 0):
            return -b / (2 * a)
        else:
            x1 = -b - math.sqrt(delta) / 2 * a
            x2 = -b + math.sqrt(delta) / 2 * a
            if(x1>0):
                return x1
            else:
                return x2