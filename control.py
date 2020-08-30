from Tables import *

class Control:

    def __init__(self, m, cm, max):
        self.ocupados=0;
        self.mesas=m;
        self.capacidad_mesa=cm
        self.capacidad_maxima=max

    def setMaxCapacity(self,n):
        self.capacidad_maxima=n

    def setTableCapacity(self,n):
        self.capacidad_mesa=n

    def updateTable(self,boundary, minDist, tableRadius,personWidth):
        self.mesas=getTableArrangement(boundary,minDist,tableRadius,personWidth)
        self.ocupados=0

    def getTables(self):
        return self.mesas

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
