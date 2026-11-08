import random

class NumberGenerator:
    def __init__(self, default_digits=50):
        self.default_digits = default_digits

    def _generator(self, num_digits=None):
        final_number = ""
        sub_number = ""
        if num_digits is None:
                num_digits = self.default_digits
        for digits in range(1, num_digits+1):
           
            if digits == 1:
                sub_number = str(random.randint(1,9))
            else :
                sub_number = str(random.randint(0,9))
            final_number += sub_number
        sign = random.choice(["", "-"]) 
        final_number = sign + final_number 
        return final_number
           
    def number_list(self, count):
        items= []
        gen = NumberGenerator()
        for i in range(1, count+1):
            number = gen._generator(i)
            items.append(number)
        print(items)    

test = NumberGenerator()
test.number_list(50)