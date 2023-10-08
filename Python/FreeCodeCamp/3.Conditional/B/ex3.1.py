sh = (input('Enter hours: '))
sr = (input('Enter rate: '))
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40:
    print('Overtime')
    reg = fr * fh
    otp = (fh - 40) * (fr * 1.5)
    # print(reg, otp)
    xp = reg + otp
else:
    print('Regular')
    xp = fh * fr
print('Pay: $', xp)
