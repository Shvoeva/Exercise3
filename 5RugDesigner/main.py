rug_width = int(input('\nВведите ширину коврика: '))
rug_lenght = 3 * rug_width

if rug_width % 3 == 2:
    print((('\\' + '/') * (rug_lenght // 2)).rjust(rug_lenght, '/'))

for i in range(rug_width // 3):
    print(('~' * (rug_lenght // 2)).center(rug_lenght, '-'))
    print((('/' + '\\') * (rug_lenght // 2)).rjust(rug_lenght, '\\'))
    print((('\\' + '/') * (rug_lenght // 2)).rjust(rug_lenght, '/'))

if rug_width % 3 == 1 or rug_width % 3 == 2:
    print(('~' * (rug_lenght // 2)).center(rug_lenght, '-'))