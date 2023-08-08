f = open('1.txt', 'r')



for i in range(3100):
    s = f.readline()
    m1 = s.split('\n')[0]
    m2 = m1.split('\t')
    

print(m2)

