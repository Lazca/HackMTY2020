from Tables import *

class Control:

    def __init__(self, m, cm, max):
        self.ocupados=0;
        self.mesas=m;
        self.capacidad_mesa=cm
        self.capacidad_maxima=max

    def sentar_grupo(self,n):
        if n > self.capacidad_mesa:
            print('grupo mayour a la capacidad maxima por mesa')
            return

        if self.ocupados >= self.capacidad_maxima:
            print('capacidad maxima alcanzada')
            return

        for mesa in self.mesas:
            if mesa.getCapacity() == 0:
                self.ocupados+=n
                mesa.setCapacity(n)
                print('grupo sentado')
                return

    def vaciar_mesa(self,indice):
        self.ocupados-=self.mesas[indice].getCapacity()
        self.mesas[indice].clear()

print('test')
lista=getTableArrangement((0,0,20,15), 1.5, 1)
control=Control(lista,4,20)
control.sentar_grupo(4)
control.vaciar_mesa(0)
