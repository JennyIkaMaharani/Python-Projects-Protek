def sum(*dData):
    jum = 0
    for data in dData:
        jum += data
    return jum
def average(*dData):
    n = 0
    for data in dData:
        n += 1
    rata = sum(*dData) / n
    return rata
def maks(*dData):
    maksi = average(*dData)
    for num in dData:
        if maksi > num:
            maksi = maksi
        else:
            maksi = num
    return maksi
def minimal(*dData):
    mini = average(*dData)
    for number in dData:
        if mini < number:
            mini = mini
        else:
            mini = number
    return mini
