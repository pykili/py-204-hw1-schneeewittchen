teststring=input()
a=''
for x in teststring:
    a= x+a
is_palindrom= a==teststring
print(is_palindrom)
