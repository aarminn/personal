from math import floor

def sdev(s,d):
    txt = s.split(d)
    txt.sort()
    txt.reverse()
    if txt[0] != '':
        return False
    else:
        return True
    

str1 = 'ABABABAB'
str2 = 'ABAB'
tgd = ''
if len(str1) == len(str2) :
    if str1 == str2 :
        print(str1)
    exit
if len(str1) < len(str2) :
    ss = str1
    sl = str2
else :
    ss = str2
    sl = str1
lss = len(ss)
lsl = len(sl)
if sdev(ss,ss[0]):
        if sdev(sl,ss[0]):
            tgd = ss[0]
for td in range(1,floor(lss/2)+1):
    if sdev(ss,ss[0:td]):
        if sdev(sl,ss[0:td]):
            tgd = ss[0:td]
if sdev(sl,ss):
    tgd = ss
print(tgd)      

     