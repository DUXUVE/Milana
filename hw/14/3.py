class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents
    
    def set_amount(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    
    def display(self):
        return f"{self.dollars}.{self.cents:02d}"