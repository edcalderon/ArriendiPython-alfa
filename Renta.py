import sys
from Mensaje import *
from Articulo import *
from Comentario import *
class Renta:

    id_rentas = 0
    rentas = []

    def __init__(self,articulo,arrendador,fechaini,fechafin):
        self.setId(id_rentas)
        self.setArticulo(articulo)
        self.setArrendador(arrendador)
        self.setFechaini(fechaini)
        self.setFechafin(fechafin)

    def setId(self,id_rentas):
        Articulo.id_rentas+=1
        self.id = Renta.rentas
    def getId(self):
        return self.id
    def setArticulo(self,articulo):
         self.articulo = articulo
    def getArticulo(self):
         return articulo
    def setArrendador(self,arrendador):
         self.arrendador = arrendador
    def getArrendador(self):
         return arrendador
    def setFechaini(self,fechaini):
           self.fechaini = fechaini
    def getFechaini(self):
           return self.fechaini
    def setFechafin(self,fechafin):
           self.fechafin = fechafin
    def getFechafin(self):
           return self.fechafin
    def setArrendatario(self,arrendatario):
         self.arrendatario = arrendatario
    def getArrendatario(self):
         return arrendatario
