from temporizador import Temporizador
from time import sleep #esto es para que vaya mas despacio cuando muestra el tiempo#
 
t = Temporizador()

t.iniciar([0,1,15]) #aqui se pone el valor al que quiere llegar el temporizador#

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.2)
    if tiempo == "00 : 00 : 00":
        break
    t.retroceder()


while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.2)
    if tiempo == "00 : 01 : 15":
        break
    t.avanzar()
