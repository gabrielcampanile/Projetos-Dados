sval = '123'
ival = int(sval)
print(ival + 1)

name = input('Who are you? ')
print('Welcome,', name)

# Elevator floor conversion APP

inp = input('Europe Floor? ')
usf = int(inp) + 1
print('US floor', usf)


# Get the name of the file and open it
name = input('Enter file: ')
handle = open(name, 'r')
