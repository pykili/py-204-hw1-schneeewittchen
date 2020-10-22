 for i in range(1, 101):
    a= 2*i-1
    left= sum(range(1, a+1, 2))
    right= i**2
    print(left==right)
