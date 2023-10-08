astr = 'Hello Bob'

try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'

try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# Sample

rawstr = input('Enter a number: ')

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
