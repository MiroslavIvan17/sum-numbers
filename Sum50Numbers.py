import random

class NumberGenerator: # vytvoril som si triedu na generovanie nahodnych cisel, ktore budu mat 50 cifier a budu moct byt kladne alebo zaporne
    def __init__(self, default_digits=50): # definoval som si default_digits ako parameter, ktory urcuje pocet cifier v generovanom cisle, natavil som to na 50 cifier ak sa nezada inak
        self.default_digits = default_digits # vytvoril som si instanciu triedy NumberGenerator

    def _generator(self, num_digits=None): # definoval som si metodu _generator, ktora generuje nahodne cislo s urcitym poctom cifier, ak sa nezada inak, tak sa pouzije default_digits
        final_number = "" # inicializoval som si prazdny string, do ktoreho budem pridavat finalne nahodne generovane cisla
        sub_number = "" # inicializoval som si prazdny string, do ktoreho budem pridavat jednotlive nahodne generovane jednociferne cisla, ktore budu tvorit finalne cislo
        if num_digits is None: # vytvoril som podmienku, ze ak je num_digits None 
                num_digits = self.default_digits # tak sa pouzije default_digits, ktory je nastaveny na 50 cifier
        for digits in range(1, num_digits+1): # vytvoril som cyklus, ktory prechadza od 1 po num_digits+1, aby som mohol generovat cisla s urcitym poctom cifier
            if digits == 1: # vytvoril som podmienku, ak je digits rovne 1, 
                sub_number = str(random.randint(1,9)) #tak sa generuje nahodne cislo od 1 do 9, aby sa zabránilo tomu, že by sa generovalo cislo s nulou na prvej pozicii
            else : # ak podmienka neplati, tak
                sub_number = str(random.randint(0,9)) # sa generuje nahodne cislo od 0 do 9, aby sa mohli generovat aj nuly na dalsich poziciach
            final_number += sub_number # pridavam jednotlive nahodne generovane jednociferne cisla do finalneho cisla ktore nam vytvori vysledne cislo s pozadovanym poctom cifier
        sign = random.choice(["+", "-"]) # generujem nahodny znak, ktory bude urcovat, ci bude cislo kladne alebo zaporne
        final_number = sign + final_number # pridavam znak na zaciatok finalneho cisla, aby som urcil, ci bude cislo kladne alebo zaporne
        return final_number # vraciam finalne cislo s pozadovanym poctom cifier a znakom, ktory urcuje, ci bude cislo kladne alebo zaporne
           
    def number_list(self, count): # definoval som si funkciu number_list, ktora generuje zoznam nahodnych cisel s urcitym poctom cifier, ktore budu moct byt kladne alebo zaporne
        items= [] 
        gen = NumberGenerator() # vytvoril som instanciu triedy NumberGenerator, aby som mohol pouzit funkciu _generator na generovanie nahodnych cisel
        for i in range(1, count+1): # vytvoril som cyklus, ktory prechadza od 1 po count+1, aby som mohol generovat cisla s urcitym poctom cifier
            number = gen._generator(i) # generujem nahodne cislo pomocou metody _generator
            items.append(number) # pridavam jednotlive nahodne generovane cisla do zoznamu items, ktory nam vytvori vysledny zoznam s pozadovanym poctom cifier a znakom, ktory urcuje, ci bude cislo kladne alebo zaporne
        #print(items), ak by sme chceli vidiet vygenerovane cisla, tak by sme odkomentovali tento riadok
        return items # vraciam zoznam nahodnych cisel    

class StringNumberAdder: # definoval som si triedu StringNumberAdder, ktora bude sluzit na sčítanie zoznamu cisel
    def __init__(self, numbers_list): # definoval som si konstruktor triedy StringNumberAdder, ktory prijima parameter numbers_list, ktory je zoznam cisel, ktore budeme scitat
        self.numbers = numbers_list # vytvoril som instanciu triedy StringNumberAdder, ktora bude obsahovat zoznam cisel, ktore budeme scitat

    def add_all(self): # definoval som si metodu add_all, ktora bude scitat vsetky cisla v zozname cisel
        if not self.numbers: # vytvoril som podmienku, ktora kontroluje, ci je zoznam cisel prazdny, ak ano
            return 0 #tak vracia 0
        max_length = max(len(num) for num in self.numbers) # zistil som dlzku najdlhsieho cisla v zozname cisel, aby som vedel, kolko cifier budem musiet scitat
        length_of_numbers = [] # vytvoril som prazdny zoznam, do ktoreho budem pridavat cisla s rovnakou dlzkou, aby som mohol scitat jednotlive cifry na rovnakej pozicii
        for num in self.numbers: # prechadzam cez vsetky cisla v zozname cisel
            if num.startswith("-"): # vytvoril som podmienku, ktora kontroluje, ci cislo zacina znakom "-", ak ano
                num = num[1:] # tak odstranim znak "-" z cisla, aby som mohol scitat jednotlive cifry na rovnakej pozicii
                length_of_numbers.append("-" + num.zfill(max_length-1)) # pridavam jednotlive cisla do zoznamu length_of_numbers, ktore budu mat rovnakú dlzku, aby som mohol scitat jednotlive cifry na rovnakej pozicii
            else: # ak podmienka nie je splnena, tak
                num = num[1:] # odstranim znak "+" z cisla, aby som mohol scitat jednotlive cifry na rovnakej pozicii
                length_of_numbers.append("+" + num.zfill(max_length-1)) # pridavam jednotlive cisla do zoznamu length_of_numbers, ktore budu mat rovnakú dlzku, aby som mohol scitat jednotlive cifry na rovnakej pozicii
        carry = 0 # inicializoval som premennu carry, ktora bude uchovavat zvysok pri zapisani jednocifernej jednotlivej pozicie
        positive_column_sum = [] # inicializoval som prazdny zoznam, do ktoreho budem pridavat jednotlive vysledky vypoctov, ktore budu kladne
        negative_column_sum = [] # inicializoval som prazdny zoznam, do ktoreho budem pridavat jednotlive vysledky vypoctov, ktore budu zaporne

        for i in range(max_length - 1, 0, -1): # vytvoril som cyklus, ktory prechadza cez jednotlive cifry na rovnakej pozicii od poslednej po prvu, aby som ich mohol scitat 
            column_sum = carry # inicializoval som premennu column_sum, ktora bude uchovavat vysledok scitania jednotlivej cifry na rovnakej pozicii a priradil som jej hodnotu carry
            for num in length_of_numbers: # prechadzam cez vsetky cisla v zozname length_of_numbers
                if num.startswith("-"): # vytvoril som podmienku, ktora kontroluje, ci cislo zacina znakom "-", ak ano
                    column_sum -= int(num[i]) # tak odcitam jednotlive cislo na rovnakej pozicii od column_sum
                else: # ak podmienka nie je splnena
                    column_sum += int(num[i])  # tak priratam jednotlive cislo na rovnakej pozicii k column_sum

            if column_sum < 0: # vytvoril som podmienku, ktora kontroluje, ci je column_sum mensi ako 0, ak ano
                calc = (abs(column_sum)) # tak vypocitam absolutnu hodnotu column_sum a priradim ju do premennej calc
                negative = calc % 10 # vlozim do premennej negative zvyšok po deleni 10, aby som zistil jednotkovú cifru
                negative_column_sum.append(str(negative)) # pridavam jednotlive vysledky vypoctov, ktore budu zaporne do zoznamu negative_column_sum
                positive_column_sum.append(str(0)) # pridavam 0 do zoznamu positive_column_sum
            else: # ak podmienka nie je splnena
                positive = column_sum % 10 # vlozim do premennej positive zvyšok po deleni 10, aby som zistil jednotkovú cifru
                positive_column_sum.append(str(positive)) # pridavam jednotlive vysledky vypoctov, ktore budu kladne do zoznamu positive_column_sum
                negative_column_sum.append(str(0)) # pridavam 0 do zoznamu negative_column_sum
    
            if column_sum < 0: # vytvoril som podmienku, ktora kontroluje, ci je column_sum mensi ako 0, ak ano
                calc = abs(column_sum) // 10 # vypocitam absolutnu hodnotu column_sum a delim ju 10, aby som zistil desiatkovú cifru
                carry = -calc # urobim z hodnoty carry negativnu naspat
            else: # ak podmienka nie je splnena
                carry = column_sum // 10 # vypocitam 
            
        while carry > 0: # ak je carry vacsie ako 0, tak
            digit = carry % 10 # vlozim do premennej digit zvysok po deleni 10
            positive_column_sum.append(str(digit)) # vlozim do posiive_column_sum hodnoty ktore budu v premennej digit
            negative_column_sum.append(str(0)) # vlozim do negative_column_sum hodnotu 0
            carry //= 10 # delim carry 10
        while carry < 0: # ak je carry mensie ako 0, tak
            digit = abs(carry) % 10 # vlozim do premennej digit zvysok po deleni 10 absolutnej hodnoty carry
            negative_column_sum.append(str(digit)) # vlozim do negative_column_sum hodnoty ktore budu v premennej digit
            positive_column_sum.append(str(0)) # vlozim do posiive_column_sum hodnotu 0
            carry = abs(carry) // 10 # delim absolutnu hodnotu carry cislom 10
            carry = -carry # urobim z hodnoty carry negativnu naspat
        
        decide= 0 # inicializoval som premennu decide, ktora bude uchovavat informaciu o tom, ci je vysledok kladny alebo zaporny
        positive_column_sum = list(reversed(positive_column_sum)) # upravil som premennu positive_column_sum tak, aby sa jednotlive cifry nachadzali v opacnom poradi
        negative_column_sum = list(reversed(negative_column_sum)) # upravil som premennu negative_column_sum tak, aby sa jednotlive cifry nachadzali v opacnom poradi
        
        for i in range(max_length): # vytvoril som cyklus, ktory prechadza cez jednotlive cifry na rovnakej pozicii od prvej po poslednu
            if int(positive_column_sum[i]) > int(negative_column_sum[i]): # vytvoril som podmienku, ktora kontroluje, ci je vacsie kladne cislo, ak ano
                decide = 1 # tak hodnota decide je 1
                break # ak je podmienka splnena ukonci sa cyklus
            elif int(negative_column_sum[i]) > int(positive_column_sum[i]): # vytvoril som podmienku, ktora kontroluje, ci je vacsie zaporne cislo, ak ano
                decide = 2 # tak hodnota decide je 2
                break # ak je podmienka splnena ukonci sa cyklus
        positive_column_sum = list(reversed(positive_column_sum)) # upravil som premennu positive_column_sum tak, aby sa jednotlive cifry nachadzali v opacnom poradi
        negative_column_sum = list(reversed(negative_column_sum)) # upravil som premennu negative_column_sum tak, aby sa jednotlive cifry nachadzali v opacnom poradi
        subtotal = [] # inicializoval som prazdny zoznam, do ktoreho budem pridavat jednotlive vysledky vypoctov, ktore budu kladne alebo zaporne

        for i in range(len(positive_column_sum)): # vytvoril som cyklus, ktory prechadza cez jednotlive cifry na rovnakej pozicii od prvej po poslednu
            if decide ==1: # podmienka ci kladne cislo je vacsie
                if positive_column_sum[i] == "0" and negative_column_sum[i] != "0": #ak je kladne 0 a zaporne nie
                    result = int(positive_column_sum[i]) - int(negative_column_sum[i]) +10 # odcitam kkladne od zaporneho a pridam 10
                    j = i+1 # index o 1 vacsi ako i 
                    if j < len(negative_column_sum): # ak je j mensie ako dlzka negative_column_sum
                        negative_column_sum[j] = str(int(negative_column_sum[j]) + 1) # pridam k zapornemu cislu 1
                    subtotal.append(str(result)) # pridavam jednotlive vysledky vypoctov do subtotal
                else: # ak podmienka nie je splnena
                    result = (int(positive_column_sum[i]) - int(negative_column_sum[i])) # odcitam zaporne od kladneho
                    subtotal.append(str(result)) # pridavam jednotlive vysledky vypoctov do subtotal

            else: #zaporne cislo je vacsie
                if negative_column_sum[i] == "0" and positive_column_sum[i] != "0": # ak je zaporne 0 a kladne nie
                    result = int(negative_column_sum[i]) - int(positive_column_sum[i]) +10 #
                    j = i+1 # index o 1 vacsi ako i
                    if j < len(positive_column_sum): # ak je j mensie ako dlzka positive_column_sum
                        positive_column_sum[j] = str(int(positive_column_sum[j]) + 1) # pridam ku kladnemu cislu 1
                    subtotal.append(str(result)) # pridavam jednotlive vysledky vypoctov do subtotal
                else:
                    result = (int(negative_column_sum[i]) - int(positive_column_sum[i])) # odcitam kladne od zaporneho
                    subtotal.append(str(result)) # pridavam jednotlive vysledky vypoctov do subtotal

        result_digits = "".join(reversed(subtotal)) # spojim jednotlive cislice do jedneho stringu v opacnom poradi ako boli ulozenev zozname subtotal
        result_digits = result_digits.lstrip("0") # odstranil som zlava vsetky nuly, aby som mal vysledok bez nul na zaciatku
        if decide == 2: # ak je vysledne cislo zaporne
            ten_digits = "-" + result_digits[:10] # tak napisem - pred cislo a vypisem prvych 10 cifier 
            print(ten_digits) # vypisem prvych 10 cifier vysledneho cisla
        else:
            ten_digits = result_digits[:10] # ak je vysledne cislo kladne, tak vypisem prvych 10 cifier vysledneho cisla
            print(ten_digits) # vypisem prvych 10 cifier vysledneho cisla
    
test = NumberGenerator() # vytvoril som instanciu triedy NumberGenerator, aby som mohol pouzit funkciu number_list na generovanie nahodnych cisel
filledList = test.number_list(50 ) # generujem zoznam 50 nahodnych cisel s 1 az 50 ciframi, ktore budu moct byt kladne alebo zaporne
adder = StringNumberAdder(filledList) # vytvoril som instanciu triedy StringNumberAdder, aby som mohol pouzit funkciu add_all na scitanie zoznamu cisel
result = adder.add_all() # volam funkciu add_all, ktora scita vsetky cisla v zozname cisel a vypise prvych 10 cifier vysledneho cisla
