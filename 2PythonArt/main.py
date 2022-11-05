symbol = 'O'
thickness = int(input('\n\tВведите толщину символа: '))

print('\n' + (symbol * thickness).center(thickness * 3))

for i in range((thickness - 1) // 2):
    print((symbol * thickness + ' ' * (2 * i + 2 - thickness % 2) + symbol * thickness).center(thickness * 3))

for i in range(thickness):
    print(symbol * thickness + ' ' * thickness + symbol * thickness)

for i in range((thickness - 1) // 2):
    print((symbol * thickness + ' ' * (thickness - i * 2 - 2) + symbol * thickness).center(thickness * 3))

print((symbol * thickness).center(thickness * 3))
