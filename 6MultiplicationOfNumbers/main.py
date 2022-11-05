numer = int(input('\n\tВведите число: '))

if numer:
    multiplication = 1
else:
    multiplication = 0

while numer:
    if numer % 10:
        multiplication *= (numer % 10)
    numer //= 10

print(f'\t{multiplication=}')