def isEven(x):
    return x % 2 == 0


v = 1
no_of_evens = 0
no_of_odds = 0

while v != -1:
    v = int(input('Enter Value'))
    if v != -1:
        if isEven(v):
            no_of_evens += 1
        else:
            no_of_odds += 1
    else:
        break

print(f'No of Evens are { no_of_evens }')
print(f'No of Odds are { no_of_odds }')