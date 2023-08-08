f = open('1_17.txt','r')
a = [int(x) for x in f]

tm = -1000000
for i in a:
    if i % 100 == 17 and i > tm:
        tm = i

k = 0
for i in range(1, len(a)-1):
    s3 = a[i - 1] + a[i] + a[i + 1]
    p = (len(str(abs(a[i - 1]))) == 3) + (len(str(abs(a[i]))) == 3) + (len(str(abs(a[i + 1]))) == 3)
    if s3 < tm and p == 1:
        k += 1

print(k)
