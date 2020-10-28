user_input = input()
alphabet = ''
for letter in user_input :
    if letter not in alphabet :
      alphabet = alphabet + letter
print(alphabet)
