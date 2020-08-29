class Mesa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ocupantes=0;

    def get_ocupantes(self):
        return self.ocupantes

    def set_ocupantes(self,n):
        self.ocupantes=n

    def vaciar(self):
        self.ocupantes=0

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
            if mesa.get_ocupantes() == 0:
                self.ocupados+=n
                mesa.set_ocupantes(n)
                print('grupo sentado')
                return

    def vaciar_mesa(indice):
        self.ocupados-=self.mesas[indice].get_ocupantes()
        self.mesas[indice].vaciar()
