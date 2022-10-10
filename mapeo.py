import numpy as np

class Graph:
    fuente = []
    objetivo = []
    ancho = []
    vertice = []

    undirected = 0

    def __init__(self, fuente=[], objetivo=[], ancho=[], direccion=True):
        self.fuente = np.array(fuente)
        self.objetivo = np.array(objetivo)
        self.ancho = np.array(ancho)
        self.direccion = direccion

        self.set_vertex()

    def print_r(self):
        print("fuente: ", self.fuente)
        print("objetivo: ", self.objetivo)
        print("ancho: ", self.ancho)
        print("Vertice: ", self.vertice)

    def set_vert(self):
        vertice = np.unique(self.fuente)
        vertice2 = np.unique(self.objetivo)
        self.vertice = np.unique(np.concatenate([vertice, vertice2]))
        return self.vertice

    def get_weight(self, n1, n2):
        return self.ancho[np.logical_and(self.fuente == n1, self.objetivo == n2)]

    def export(self):
        array_export = [(int(self.fuente[i]), int(self.objetivo[i]), self.ancho[i]) for i in range(self.fuente.size)]
        return array_export