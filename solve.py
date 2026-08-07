# question 1

# for i in range (2000, 3200+1):
#     if (i % 7 ==0) and (i % 5 != 0):
#         print(i, end=", ")
# cách này bị mắc dấu phẩy ở cuối

def q1():
    l=[]
    for i in range(2000, 3200+1):
        if (i % 7 ==0) and (i % 5 !=0):
            l.append(i)
    print(','.join(map(str, l)))

# question 2
def factorial(i):
    fact = 1
    for _ in range (1, i+1):
        fact *= _
    return fact

# question 3
def q3(i):
    d = dict()
    for i in range(1, i+1):
        d[i] = i**2
    return d

# q4
def q4():
    values = input()
    l = values.split(",")
    t = tuple(l)
    print(l)
    print(t)


if __name__ == "__main__":
    q4()