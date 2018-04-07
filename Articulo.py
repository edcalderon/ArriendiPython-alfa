from Comentario import *
import time
from Usuario import *

class Articulo:

    iva = 0.19
    num_articulos = 0
    comentarios = []
    id_articulos = 0        #contador
    articles={}

    def __init__(self,precio,nombre,propietario):
        self._setId(Articulo.id_articulos)
        self.setPrecio(precio)
        self.setNombre(nombre)
        self.setPropietario(propietario)
        self.setDate()
        self.setTipo('NN')
        self.setPublicado(True)
        self.setArrendado(False)
        Articulo.AddArticles(self)

    def AddArticles(self):
        Articulo.articles.setdefault(self.getId,self)

    def toString(self):
        return "[ID:%s, Nombre:%s, Valor Renta Diaria:%s, Fecha De Creacion:%s, Tipo de Articulo:%s, Propietario:%s]" %(str(self.id),self.nombre,str(self.precio),str(self.date),self.tipo,self.propietario.getNombre())

    @staticmethod
    def BuscarArticuloPorId(id_a_buscar,list_art = []):
        for art in list_art:
            if art.getId() == int(id_a_buscar):
                return art

    def _setId(self,id_articulos):
        Articulo.id_articulos+=1
        self.id = Articulo.id_articulos
    def getId(self):
        return self.id
    def setPrecio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setPropietario(self,propietario):
        self.propietario = propietario
    def getPropietario(self):
        return self.propietario
    def setDate(self):
        self.date = time.asctime()
    def setTipo(self,tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def setPublicado(self,estado):
        self.publicado = estado
    def setArrendado(self,estado):
        self.arredado = estado
    def getArrendado(self):
        return self.arredado