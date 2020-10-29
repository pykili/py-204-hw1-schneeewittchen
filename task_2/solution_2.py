user_input = input()
occurrences = 0
for letter in user_input :
 if user_input.count(letter) > occurrences :
   occurrences = user_input.count(letter)
   most_frequent_character = letter
print(most_frequent_character)
