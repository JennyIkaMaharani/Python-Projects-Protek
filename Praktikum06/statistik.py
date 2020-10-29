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
    maksi = max(*dData)
    return maksi
def minimal(*dData):
    mini = min(*dData)
    return mini

