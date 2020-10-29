from statistik import *
def pprint(*dData):
    print(*dData)
    print('rata- rata = ', average(*dData))
    print('nilai maks = ', maks(*dData))
    print('nilai min  = ', minimal(*dData))
pprint(5, 10, 4, 9, 30, 16, 2, 11)
pprint(81, 98, 12, 83, 45, 77, 69, 30, 56)
