# #Exemplo de como resolver a questão Questão 28, Capitulo 4 do livro Halliday

from vpython import *
bola = sphere(pos=vector(0,0,0), color=color.green, make_trail=True)
chao = box(pos=vector(50,0,0), size=vector(150,0.5,10))

v0=42
ang=radians(60)

vx=v0*cos(ang)
vy=v0*sin(ang)

bola.velocity=vector(vx,vy,0)

grafico = gdisplay(xtitle='x (m)', ytitle='altura (m)' )
bolapos = gcurve(graph=grafico)

t=0
dt=0.01
while t <= 5.5:
    rate(100)
    
    bola.pos.x = bola.pos.x + bola.velocity.x*dt
    
    bola.pos.y = bola.pos.y + bola.velocity.y*dt
    bola.velocity.y = bola.velocity.y - 9.8*dt
    
    bolapos.plot(bola.pos.x, bola.pos.y)

    t=t+dt
    
print(mag(bola.velocity), 'm/s')