#membuat function
def dataStat(x):
    a = sum(x) /len(x)
    b = max(x)
    c = min(x)
    value = [a, b, c]
    return value
x = [1, 2, 3, 4, 5]
print(dataStat(x))

