from Sum50Numbers import StringNumberAdder

class NumberTester:
    def __init__(self):
        pass

    
    def _generate_pattern(self, num_digits=50, number_choice=9, is_negative=True):                  # pomocna metoda na generovanie vzoru pre testy
        items = []
        sign = "-" if is_negative else "+"
        
        for i in range(1, num_digits + 1):
            number_str = sign + (str(number_choice) * i)
            items.append(number_str)
            
        return items

    def test1_all_negative_nines(self):                                                             # test 1: vsetky cisla su zaporne a zlozene zo samych deviatok    
        test_data = self._generate_pattern(num_digits=50, number_choice=9, is_negative=True)
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je -1111111111

    def test2_all_positive_ones(self):                                                              # test 2: vsetky cisla su kladne a zlozene zo samych jednotiek
        test_data = self._generate_pattern(num_digits=50, number_choice=1, is_negative=False)
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je 1234567901

    def test3_all_negative_fives(self):                                                             # test 3: vsetky cisla su zaporne a zlozene zo samych patiek
        test_data = self._generate_pattern(num_digits=50, number_choice=5, is_negative=True)
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je -6172839506
    
    def test4_zeros(self):                                                                          # test 4: sucet samych nul
        test_data = ["+000", "-00", "+0"]
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je 0

    def test5_alternating_signs(self):                                                              # test 5: striedanie kladnych a zapornych cisel (+100, -99, +50, -50)  
        test_data = ["+1000", "-999", "+10", "-9"]
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je 2

    def test6_carry_overflow(self):                                                                 # test 6: overenie prenosu cifier (carry)    
        test_data = ["+999", "+10", "+1"]
        adder = StringNumberAdder(test_data)
        return adder.add_all()                                                                      # ocakavany vysledok je 1010

# Spustenie testov 
if __name__ == "__main__":
    tester = NumberTester()
    
    result1 = tester.test1_all_negative_nines()
    print(f"Výsledok Testu 1 (záporné deviatky): {result1}")
    
    result2 = tester.test2_all_positive_ones()
    print(f"Výsledok Testu 2 (kladné jednotky): {result2}")
    
    result3 = tester.test3_all_negative_fives()
    print(f"Výsledok Testu 3 (záporné päťky): {result3}")

    result4 = tester.test4_zeros()
    print(f"Výsledok Testu 4 (nulové hodnoty): {result4}")
    
    result5 = tester.test5_alternating_signs()
    print(f"Výsledok Testu 5 (striedanie znamienok): {result5}")
    
    result6 = tester.test6_carry_overflow()
    print(f"Výsledok Testu 6 (pretečenie cifier / carry): {result6}")