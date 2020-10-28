n = int(input())
sum = 0
denominator = 0
for i in range(1, n+1):
  user_input = input()
  if user_input == '' : 
    pass
  elif user_input == '0' :
    pass
  else :
    number = int(user_input)
    sum = sum + number
    denominator = denominator + 1
average = sum/denominator
print('Average is', average)
