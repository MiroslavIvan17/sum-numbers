import random

class NumberGenerator:
    def __init__(self):
        self.stack_numbers = []

    def generator(self, num_digits):
        final_number = ""
        sub_number = ""
        
        for digits in range(1, num_digits+1):
            if digits == 1:
                sub_number = str(random.randint(1,9))
            else :
                sub_number = str(random.randint(0,9))
            final_number += sub_number
        sign = random.choice(["", "-"]) 
        final_number = sign + final_number 
        print(final_number)
        return
       # self.stack_numbers.append(final_number)
            
def number_list():
    list= []
    skuska = NumberGenerator()
    for i in range(1, 51):
        skuska.generator(i)
        list.append(skuska)
    

number_list()