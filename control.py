class Mesa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ocupantes=0;

        def get_ocupantes():
            return self.ocupantes

        def set_ocupantes(n):
            self.ocupantes=n

        def vaciar():
            self.ocupantes=0

class Control:

    def __init__(self, m, cm, max):
        self.ocupados=0;
        self.mesas=m;
        self.capacidad_mesa=cm
        self.capacidad_maxima=max

    def sentar_grupo(n):
        if self.ocupados >= self.capacidad_maxima:
            return

        for mesa in self.mesas:
            if mesa.get_ocupantes() == 0:
                self.ocupados+=n
                mesa.set_ocupantes(n)
                return

    def vaciar_mesa(int indice):
        self.ocupados-=self.mesas[indice].get_ocupantes()
        self.mesas[indice].vaciar()
