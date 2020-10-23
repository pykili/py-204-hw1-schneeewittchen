teststring=str(input())
occurrences=0
for letter in teststring:
    double=letter*2
    if teststring.count(double)==2:
        occurrences=occurrences+1
if occurrences>=2 : occurred_twice='Yes'   
else: occurred_twice='No'
print(occurred_twice)
