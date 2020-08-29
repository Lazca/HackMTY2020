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
