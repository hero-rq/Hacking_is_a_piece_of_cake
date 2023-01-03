'''(lambda _, __, ___: _(_, __, ___))(lambda _, __, ___: chr(___ % __) + _(_, __, ___ // __), *(lambda _: _(_ - 1))(100))

f=lambda:[[int(c)for c in s.strip()]for s in open("life.txt")]
g=lambda m,x,y:sum(m[x+i][y+j]for i in(-1,0,1)for j in(-1,0,1)if(i or j)and m[x+i][y+j])
h=lambda m:[[g(m,x,y)in(3,2)and m[x]여기 처음 나오는 코드는 IOCCC 코드를 참고하였는데 처음에 이런 걸 시도했다가는 주화입마에 빠질 수 있으니 참고만 하시는 걸로 큐큐[y]or g(m,x,y)==3for y in range(len(m[x]))]for x in range(len(m))]
while 1:print"\n".join(" ".join(str(m)for m in n)for n in f())or"";f=h(f)
 

import turtle

def draw_branch(t, length):
    if length > 5:
        t.forward(length)
        t.right(20)
        draw_branch(t, length - 15)
        t.left(40)
        draw_branch(t, length - 15)
        t.right(20)
        t.backward(length)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
draw_branch(t, 100)
turtle.done()
'''

from PIL import Image

width, height = 800, 600

pixels = Image.new("RGB", (width, height), "white")

pixels = pixels.load()

max_iter = 256

viewport = (-2.0, -1.0, 1.0, 1.0)

pixel_width = (viewport[2] - viewport[0]) / width
pixel_height = (viewport[3] - viewport[1]) / height

for x in range(width):
    for y in range(height):
        real = viewport[0] + x * pixel_width
        imag = viewport[1] + y * pixel_height

        c = complex(real, imag)
        z = 0
        for i in range(max_iter):
            if abs(z) > 2:
                break 
            z = z**2 + c
        hue = int(i / max_iter * 360)
        saturation = 100
        value = int(i / max_iter * 100)
        color = (hue, saturation, value)
        pixels[x, y] = color

#pixels.save("mandelbrot.png")
