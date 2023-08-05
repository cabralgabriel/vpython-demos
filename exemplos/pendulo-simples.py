from vpython import *

# Configurando a cena
scene = canvas(title='Pêndulo Simples', width=700, height=500)

# Definindo as variáveis do pêndulo
length = 2   # comprimento do pêndulo em metros
angle = pi / 4   # ângulo inicial em radianos
angular_velocity = 0   # velocidade angular inicial
angular_acceleration = 0   # aceleração angular inicial
gravity = 9.81   # aceleração da gravidade em m/s^2
damping = 0.99   # amortecimento para evitar oscilações infinitas

# Criando o pêndulo
pivot = vector(0, 0, 0)
bob = sphere(pos=pivot + vector(length * sin(angle), -length * cos(angle), 0),
             radius=0.1, color=color.blue)
rod = cylinder(pos=pivot, axis=bob.pos - pivot, radius=0.05, color=color.red)

# Loop principal
dt = 0.01
while True:
    rate(1/dt)

    # Calculando a posição do pêndulo
    angular_acceleration = -gravity / length * sin(angle)
    angular_velocity += angular_acceleration * dt
    angular_velocity *= damping
    angle += angular_velocity * dt

    bob.pos = pivot + vector(length * sin(angle), -length * cos(angle), 0)
    rod.axis = bob.pos - pivot