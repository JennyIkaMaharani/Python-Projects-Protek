file = open("d:/data2.txt", "r")
sum = 0
for data in file:
    try:
        sum = sum + int(data)
    except ValueError:
        print('Data tidak valid')
print(sum)
