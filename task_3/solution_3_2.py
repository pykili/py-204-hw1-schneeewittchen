string1 = input()
string2 = input()
string3 = input()
string4 = input()
string5 = input()
string6 = input()
string7 = input()
string8 = input()
string9 = input()
string10 = input()
big_string = string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8 + string9 + string10
alphabet = ''
for letter in big_string:
  if letter not in alphabet :
    alphabet = alphabet + letter
print('the alphabet is', alphabet)
