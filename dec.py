Letter = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.!?= ()'`+-1234567890:;'IXV><«»"
f = open('key.dat', 'r')
z = open('rascringe.txt', 'w')
pdm = {}
for line in f:
    if line[-1]=="\n":
        line = line[0:-1]
    ln = len(line)
    res = ""
    i = (ln - 1)
    while i >= 0:
        index = (ord(line[i]) % 98 - 64) 
        if(index < 0):
            index = (len(Letter) + index)
        res = res + Letter[index]
        pdm[Letter[index]] = line[i]
        i = (i - 1)

    z.write(res + "\n")
buk = 'A'
cuk = int(buk)
print(cuk)
f.close()
z.close()

