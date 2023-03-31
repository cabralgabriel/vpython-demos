#Exemplo de como resolver a questão Questão 56, Capitulo 2 do livro Halliday

from vpython import *

bola1 = sphere(pos=vector(0,43.9,0), color=color.red, velocity=vector(0,0,0))
bola2= sphere(pos=vector(10,43.9,0), color=color.green, velocity=vector(0,-12.3,0))
agua = box(pos=vector(0,0,0), color=color.cyan,size=vector(50,0.5,15))
t=0
dt=0.01
scene.camera.follow(bola1) #camera acompanha a bola

#janelas dos graficos
grafico1 = gdisplay()
grafico2 = gdisplay()

#curvas
b1vel=gcurve(graph=grafico1, color=color.red)
b2vel=gcurve(graph=grafico1, color=color.green)

b1pos=gcurve(graph=grafico2, color=color.red)
b2pos=gcurve(graph=grafico2, color=color.green)


while bola1.pos.y >= agua.pos.y:
    rate(200)
    
    #queda da bola1
    bola1.velocity.y = bola1.velocity.y - 9.8*dt
    bola1.pos.y = bola1.pos.y + bola1.velocity.y*dt
    
    if t >= 1:
        bola2.velocity.y = bola2.velocity.y - 9.8*dt
        bola2.pos.y = bola2.pos.y + bola2.velocity.y*dt
        b2vel.plot(t,bola2.velocity.y)
        b2pos.plot(t,bola2.pos.y)

    t=t+dt
    b1vel.plot(t,bola1.velocity.y)
    b1pos.plot(t,bola1.pos.y)

    
print('a duracao da queda foi de', t, 'segundos')