# question 1

# for i in range (2000, 3200+1):
#     if (i % 7 ==0) and (i % 5 != 0):
#         print(i, end=", ")
# cách này bị mắc dấu phẩy ở cuối

l=[]
for i in range(2000, 3200+1):
    if (i % 7 ==0) and (i % 5 !=0):
        l.append(i)
print(','.join(map(str, l)))