from vpython import *

#Constantes
g = 9.8
ang = pi/4
v0 = 0
vz = v0*(cos(ang))
vy = -v0*(sin(ang))

t = 0
dt = 0.01

#Gera plano inclinado e chão
plano = box(pos=vector(0,0,0), size=vector(10,1,60))
plano.rotate(angle=ang)
chao = box(pos=vector(0,-21,30), size=vector(10,1,20))

#Gera bloco deslizante
bloco = box(pos=vector(0,21,-20), size=vector(2,1,3), color=color.red)
bloco.rotate(angle=ang)
bloco.velocity=vector(0,vy,vz)

while t < 100:
    rate(20)
    
    bloco.pos = bloco.pos + bloco.velocity*dt
    
    vy = vy - g*cos(ang)
    vz = vz + g*sin(ang)
    bloco.velocity=vector(0,vy,vz)
    
    if bloco.pos.y - bloco.size.z <= (chao.pos.y):
        break
    
    t=t+dt