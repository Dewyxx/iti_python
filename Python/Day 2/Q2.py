number = int(input("Enter your number: "))

Multiply_table = []

for i in range(1, number+1):
    list = []
    for j in range(1, i+1):
        list.append(i*j)
    Multiply_table.append(list)

print(Multiply_table)
   
    
        