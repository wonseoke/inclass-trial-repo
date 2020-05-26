arr = [1,2,4,8,16]

def all_of_them(i):
    return True # same as ... return i == i

def equals_two(i):
    return i == 2

def greater_than_two(i):
    return i > 2

def really_big(i):
    return i > 102

filter(all_of_them, arr) #> <filter at 0x103fa71d0>

list(filter(equals_two, arr)) #> [2]
list(filter(greater_than_two, arr)) #> [4, 8, 16]
list(filter(really_big, arr)) #> []


print(list(filter(all_of_them, arr))) #> [1, 2, 4, 8, 16])