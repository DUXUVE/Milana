class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    def input_data(self):
        self._numerator = int(input())
        self._denominator = int(input())

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def multiply(self, other: 'Fraction'):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def division(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator, other.numerator * self.denominator)
    
    def addition(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
    
    def subtraction(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
    
    