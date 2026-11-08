import random

class NumberGenerator:
    def __init__(self):
        self.random_numbers = []
    def generator(self, num_numbers=50):
        final_number = ""
        for i in range(1, num_numbers+1):
            if i == 1:
                number = str(random.randint(1,9))
            else :
                number = str(random.randint(0,9))
            
            
            final_number += str(number) 
            self.random_numbers.append(final_number)
        print(self.random_numbers)
skuska = NumberGenerator()
skuska.generator()