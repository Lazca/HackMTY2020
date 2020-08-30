from Tables import *

class Control:

    def __init__(self, m, cm, max):
        self.ocupados=0;
        self.mesas=m;
        self.capacidad_mesa=cm
        self.capacidad_maxima=max

    def getCapacity(self):
        return self.ocupados

    def getMaxCapacity(self):
        return self.capacidad_maxima

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
        i=n
        print(self.capacidad_maxima)
        if i > self.capacidad_mesa:
            return 'grupo mayor a la capacidad maxima por mesa'

        if self.ocupados + n > self.capacidad_maxima:
            return 'capacidad maxima alcanzada'

        for mesa in self.mesas:
            print(mesa.getCapacity())
            if mesa.getCapacity() == 0:
                self.ocupados= self.ocupados  + i
                print('grupo sentado')
                mesa.setCapacity(i)
                return

    def vaciar_mesa(self,indice):
        self.ocupados-=self.mesas[indice].getCapacity()
        self.mesas[indice].clear()
