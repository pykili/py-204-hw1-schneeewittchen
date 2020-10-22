teststring=str(input())
symbols='абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz0123456789 ,.!?'
for letter in symbols:
    if letter in teststring:
        print(letter, end='') 
