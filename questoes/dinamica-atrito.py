#Exemplo de como resolver a questão Questão 35, Capitulo 5 do livro Young

from vpython import *
chao = box(pos=vector(20,0,5), size=vector(100,1,20))
bloco = box(pos=vector(0,1,0), size=vector(5,1,2), color=color.red)
bloco2= box(pos=vector(0,1,10), size=vector(5,1,2), color=color.blue)
g=9.8

mi1=0.8
ax1=-mi1*g ##-fat=ma
bloco.velocity = vector(28.7,0,0)
bloco.ac = vector(ax1,0,0)

t1=0
dt=0.01

while bloco.velocity.x >= 0:
    rate(100)
    bloco.pos = bloco.pos + bloco.velocity*dt
    bloco.velocity = bloco.velocity + bloco.ac*dt
    t1=t1+dt
    
print ('carro 1 deslocou',bloco.pos.x, 'metros')

mi2=0.25
ax2=-mi2*g
v0=sqrt(2*mi2*g*bloco.pos.x) ##-mi*g substituido na eq de torricelli, v=0, isolar v0
bloco2.velocity = vector(v0,0,0)
bloco2.ac = vector(ax2,0,0)

t2=0

while bloco2.velocity.x >= 0:
    rate(100)
    bloco2.pos = bloco2.pos + bloco2.velocity*dt
    bloco2.velocity = bloco2.velocity + bloco2.ac*dt
    t2=t2+dt

print ('v0 carro 2',v0, 'm/s')