
#es_parentesi

caso1:str = "((()))"
caso2:str = "(()"
caso3:str = "()()()"
caso4:str = "))(("
caso5:str = "(()())"

count1 = 0
count2 = 0

for par in caso5:

    if par=="(":
        count1 += 1
    if par==")":
        count2 += 1
        
if count1==count2:
    print("True")
else:
    print("False")

