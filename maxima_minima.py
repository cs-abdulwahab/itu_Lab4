# Video  URL : https://youtu.be/MNNMS8Roh6g


maximum = -9999
v = 1
while v != -1:
    v = int(input('Enter a value = '))
    if v == -1:
        break

    if v > maximum:
        maximum = v

print(f' maximum is  = {maximum}')
