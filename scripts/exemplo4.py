from vpython import *
import math

t=1
dt=0.01

w = 2*pi/t #velocidade angular
r = 5 #raio da circunferencia

chao = box(pos=vector(0,-2,0), size=vector(20,1,20))
bola = sphere(pos=vector(r,0,0), color=color.red, make_trail=True)
scene.camera.follow(bola) #camera acompanha a bola


while True:
    rate(100)

    bola.pos.x = r*cos(w*t)
    bola.pos.z = r*sin(w*t)

    t=t+dt


