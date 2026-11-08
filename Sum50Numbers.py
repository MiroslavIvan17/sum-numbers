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
        sign = random.choice(["+", "-"]) 
        final_number = sign + final_number 
        return final_number
           
    def number_list(self, count):
        items= []
        gen = NumberGenerator()
        for i in range(1, count+1):
            number = gen._generator(i)
            items.append(number)
        #print(items)
        return items    

test = NumberGenerator()
filledList = test.number_list(50)

class StringNumberAdder:
    def __init__(self, numbers_list):
        self.numbers = numbers_list

    def add_all(self):
        if not self.numbers:
            return 0
        max_length = max(len(num) for num in self.numbers) 
        length_of_numbers = []
        for num in self.numbers:
            if num.startswith("-"):
                num = num[1:]
                length_of_numbers.append("-" + num.zfill(max_length-1))
            else:
                num = num[1:]
                length_of_numbers.append("+" + num.zfill(max_length-1))
        carry = 0
        reversed_digits = []
        for i in range(max_length - 1, 0, -1):
        #    if i == 0:
        #        break
            column_sum = carry
            for num in length_of_numbers:
                if num.startswith("-"):

                    column_sum -= int(num[i])
                    
                else:
                    column_sum += int(num[i])
                #print("vypisalo sucet" + str(column_sum))    
            current_digit = column_sum % 10
            reversed_digits.append(str(current_digit))
            carry = column_sum // 10
            #print("vypisalo carry" + str(carry))
        while carry > 0:
            
            reversed_digits.append(str(carry))
            carry //= 100
        
        result_digits = "".join(reversed(reversed_digits))
        print(result_digits)    
        return result_digits 
    
adder = StringNumberAdder(filledList)
result = adder.add_all()
