x = int(input('x: '))

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All Done')

# NO ELSE

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
print('All Done')


# Multi-way

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')
print('All Done')
