class BagelsGame:
    
    def __init__(self):
        self.DIGITS_QUANTITY = 3
        
    def showPresentation():
        print
        (
"""
Bagels, a deductive logic game.

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:

When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
"""
    )
        
    def generateMinAndMaxValue(self, digits_quantity : int = None) -> (int, int):       
        if digits_quantity is None:
            digits_quantity = self.DIGITS_QUANTITY
        
        elif not isinstance(digits_quantity, int) or digits_quantity < 0: 
            raise ValueError("The quantity digits must be a integer")
            
        min_number = 10 ** (digits_quantity - 1)
        max_number = 10 ** digits_quantity - 1
        
        return (min_number, max_number)     
