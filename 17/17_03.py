f = open('17.txt','r')
a = [int(x) for x in f]

tmin = 1000000
for i in a:
    if abs(i) % 10 == 6 and i < tmin:
        tmin = i

k = 0
smax = 0
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 6) + (abs(a[i + 1]) % 10 == 6)) == 1:
        if a[i] ** 2 + a[i+1] ** 2 < tmin ** 2:
            k += 1
            if a[i] ** 2 + a[i+1] ** 2 > smax:
                smax = a[i] ** 2 + a[i+1] ** 2 
print(k)
print(smax)

