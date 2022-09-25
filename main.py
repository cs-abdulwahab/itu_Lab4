# Video  URL : https://youtu.be/twlVxd42TRc

def isEven(x):
    return x % 2 == 0

no_of_evens = 0
no_of_odds = 0
v = 1
while v != -1:
    v = int(input('Enter a value = '))
    if v == -1:
        break

    if isEven(v):
        no_of_evens += 1
    else:
        no_of_odds += 1



print(f'  No of Evens are = {no_of_evens}')
print(f'  No of Odds are = {no_of_odds}')
