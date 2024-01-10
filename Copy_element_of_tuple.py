#Copy Specific elements from one tuple to a new tuple.

Tuple = eval(input("Enter first tuple: "))
n = int(input("Enter the element you want to copy: "))
T2=()
for i in  Tuple:    
    if i == n:
        T2=T2+(i,)
print(T2)        
