class Temporizador():
    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()
        self.parado = True #se agrega un estado para el temporizador en tk#

    def iniciar(self, valores): #el 0,1,2 son las posiciones en las q quiero q arranque y son las q mencione en usuario#
        self.hora.iniciar(valores[0])
        self.minuto.iniciar(valores[1])
        self.segundo.iniciar(valores[2])

    def retroceder(self):
        self.segundo.retroceder()
        if self.segundo.valor == self.segundo.tope:
            self.minuto.retroceder()
            if self.minuto.valor == self.minuto.tope:
                self.hora.retroceder()
                
    def reiniciar(self, valores):
        self.hora.iniciar(valores[0])
        self.minuto.iniciar(valores[1])
        self.segundo.iniciar(valores[2])

    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == 0:
            self.minuto.avanzar()
            if self.minuto.valor == 0:
                self.hora.avanzar()
        
          
    def mostrar_tiempo(self):
        return str(self.hora.mostrar_valor()) + " : " + str(self.minuto.mostrar_valor()) + " : " + str(self.segundo.mostrar_valor())


               
class UnidadTiempo():
    def __init__(self):
        self.valor = 0
        self.tope = 0

    def iniciar(self, valor):
        self.valor = valor

    def retroceder(self):
        self.valor -= 1
        if self.valor < 0:
            self.valor = self.tope

    def reiniciar(self, valor):
        self.valor = valor

    def avanzar(self):
        self.valor += 1
        if self.valor > self.tope:
            self.valor = 0
        

    def mostrar_valor(self):
        if self.valor < 10:
            return "0" + str(self.valor)
        return str(self.valor)

class Hora(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 23

class Minuto(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 59

class Segundo(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 59
