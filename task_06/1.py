from turtle import *

speed(0)
left(90)
fillcolor("black")

begin_fill()
for i in range(7):
    fd(10 * 20)
    rt(120)
end_fill()

pu()

color("yellow")
count = 0
for x in range(11):
    for y in range(11):
        goto(x * 20, y * 20)
        dot(5)
        sc = getcanvas()
        if sc.find_overlapping(x * 20, -y * 20, x * 20, -y * 20):
            print(sc.find_overlapping(x * 20, -y * 20, x * 20, -y * 20))
            count += 1
        
done()
print(count)
