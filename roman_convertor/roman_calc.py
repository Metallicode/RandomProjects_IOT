
##============= Project Solution =================#

##Values Dict
rv = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100}

##converts the roman number to int in one line ;)
def convert_to_int(r):
      return sum([rv[x] for x in r])-sum([rv[r[i]]*2 for i in range(len(r)-1) if rv[r[i]] < rv[r[i+1]]])






##============= Longer version... =================#
####Returns the total value to subtract 
##def value_to_sub(roman):
##      values_to_sub = []
##      for i in range(len(roman)-1):
##            if rv[roman[i]] < rv[roman[i+1]]:
##                  values_to_sub.append(rv[roman[i]]*2)
##      return sum(values_to_sub)
##
####converts the roman number to int
##def convert_to_int(roman):
##      total_sum = sum([rv[x] for x in roman])
##      return total_sum-value_to_sub(roman)





##============= Test (test is good if nothing prints..) =================#

all_roman_nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                  "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
                  "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
                  "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
                  "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
                  "LI", "LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", "LX",
                  "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX",
                  "LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", "LXXX",
                  "LXXXI", "LXXXII", "LXXXIII", "LXXXIV", "LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX", "XC",
                  "XCI", "XCII", "XCIII","XCIV", "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", "C"]

for i in range(len(all_roman_nums)):
      if i+1 is not convert_to_int(all_roman_nums[i].lower()):
            print(f"error with value: {i+1}   ===>  conversion returns: {convert_to_int(all_roman_nums[i].lower())}")


