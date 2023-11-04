test_T = "AbcDEFG"
test_F = "wXY__ Z"

import string

letters = string.ascii_letters 
print(letters)    
# 실행 결과 >>> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def check(string):
    for letter in string:
        if letter not in letters:
            return False
    return True

print(check(test_T))  # 결과 : True
print(check(test_F))  # 결과 : False

#---------------------------------------#

print(test_T.isalpha())
print(test_F.isalpha())

#---------------------------------------#

test_lower = "abcdef"
test_upper = "ZYXWVU"
test_mix = "AbCdE"

print(test_lower.islower())  # 결과 : True
print(test_upper.islower())  # 결과 : False
print(test_mix.islower())  # 결과 : False

print(test_lower.isupper())  # 결과 : False
print(test_upper.isupper())  # 결과 : True
print(test_mix.isupper())  # 결과 : False