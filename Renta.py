import sys
import datetime
from Mensaje import *
from Articulo import *
from Comentario import *
from Run import *
class Renta:

    id_rentas = 0 # contador ids rentas
    rentas = []
    disponible = "disponible"

    def __init__(self,articulo,arrendador,periodo,arrendatario=""):
        self.setId()
        self.setArticulo(articulo)
        self.setArrendador(arrendador)
        self.setPeriodo(periodo)
        self.setArrendatario(arrendatario)
        self.setIsDisponible(True)


    def BuscarRentaPorId(id_a_buscar,lista_rentas):
        for renta in Renta.rentas:
            if renta.getId() == int(id_a_buscar):
                return renta

    def toString(self):

        if self.getIsDisponible() == False:
            Renta.disponible = "no disponibles"
        if self.getArrendatario():
            arrendatario = self.getArrendatario().getNombre()
        else:
            arrendatario = "none"
        return "[ID:%s, Articulo:%s, Periodo(Dias):%s, Precio(xDia):%s, Estado:%s, Arrendador:%s, Arrendatario:%s]" % (str(self.getId()),self.getArticulo().getNombre(),self.getPeriodo(),self.getArticulo().getPrecio(),Renta.disponible,self.getArrendador().getNombre(),arrendatario)

    def setId(self):
        Renta.id_rentas+=1
        self.id = Renta.id_rentas
    def getId(self):
        return self.id
    def setArticulo(self,articulo):
         self.articulo = articulo
    def getArticulo(self):
         return self.articulo
    def setArrendador(self,arrendador):
         self.arrendador = arrendador
    def getArrendador(self):
         return self.arrendador
    def setPeriodo(self,periodo):
           self.periodo = periodo
           self.setFechaini()
           self.setFechafin(periodo)
    def getPeriodo(self):
           return self.periodo
    def setFechaini(self):
           self.fechaini = datetime.datetime.now()
    def getFechaini(self):
           return self.fechaini
    def setFechafin(self,periodo):
        aux = self.getFechaini()
        fechafin = aux + datetime.timedelta(days=int(periodo))
        self.fechafin = fechafin
    def getFechafin(self):
           return self.fechafin
    def setArrendatario(self,arrendatario):
         self.arrendatario = arrendatario
    def getArrendatario(self):
         return self.arrendatario
    def setIsDisponible(self,valor):
         self.isDisponible = bool(valor)
    def getIsDisponible(self):
         return self.isDisponible
    def getRentas():
         return Renta.rentas