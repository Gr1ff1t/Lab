class OrdinaryFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def check_for_correctness(self):
        return self.numerator < self.denominator
    

o = OrdinaryFraction(6, 5)
print(o.check_for_correctness())  