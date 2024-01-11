#Sum the elements of a tuple in python


def sum_tuple(t):
    test=list(t)
    count=0
    for i in test:
        count=count+i
    return count

I=eval(input("Enter a tuple: "))
print(sum_tuple(I))
