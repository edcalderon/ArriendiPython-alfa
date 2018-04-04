import sys
from Mensaje import *
from Articulo import *
from Comentario import *
from Run import *
class Renta:

    id_rentas = 0 # contador ids rentas
    rentas = []
    disponible = "disponible"

    def __init__(self,articulo,arrendador,periodo):
        self.setId()
        self.setArticulo(articulo)
        self.setArrendador(arrendador)
        self.setPeriodo(periodo)
        self.setIsDisponible(True)


    def BuscarRentaPorId(id_a_buscar,lista_rentas):
        for renta in Renta.rentas:
            if renta.getId() == int(id_a_buscar):
                return renta

    def toString(self):
        if self.getIsDisponible() == False:
            Renta.disponible = "no disponibles"
        srt = "[" + "Id renta:" + str(self.getId()) + " Articulo:"+ str(self.getArticulo().getNombre())+ " Periodo:"+ str(self.getPeriodo())+" Precio por dia:"+ str(self.getArticulo().getPrecio())+ " Estado:"+Renta.disponible+ "]"
        return srt

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
    def getPeriodo(self):
           return self.periodo
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
    def setIsDisponible(self,valor):
         self.isDisponible = bool(valor)
    def getIsDisponible(self):
         return self.isDisponible
