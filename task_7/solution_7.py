testword=str(input())
a=''
for x in testword:
    a= x+a
is_palindrom= a==testword
print(is_palindrom)
