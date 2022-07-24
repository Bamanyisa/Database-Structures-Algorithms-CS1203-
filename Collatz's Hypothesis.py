
c0 = int(input("Enter any natural number : ")) 
 
count = 0
while c0 != 1:
    if (c0 % 2) == 1: 
        c0 = 3 * c0 + 1
 
    else: 
        c0 = c0 // 2
    count += 1
    print(c0)
print("steps = ",count)
