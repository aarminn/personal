str1 = 'ABABAB'
str2 = 'ABAB'
res = ''
tres = ''
if len(str1) == len(str2) :
    if str1 == str2 :
        print(str1)
    exit
if len(str1) < len(str2) :
    sx = str1
    sy = str2
else :
    sx = str2
    sy = str1
lenx = len(sx)
leny = len(sy)
for lx in range(1,lenx+1):
    for c2 in range(lenx-lx+1):
        for ly in range(leny-lx+1):
            if sx[c2:c2+lx] == sy[ly:ly+lx]:
                if len(sx[c2:c2+lx]) > len(tres):
                    tres = sx[c2:c2+lx]
print(tres)

        
