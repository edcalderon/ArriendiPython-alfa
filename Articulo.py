from Comentario import *
import time
from Usuario import *
class Articulo:

    iva = 0.19
    num_articulos = 0
    comentarios = []
    id_articulos = 0        #contador

    def __init__(self,precio,nombre,propietario):
        self._setId(Articulo.id_articulos)
        self.setPrecio(precio)
        self.setNombre(nombre)
        self.setPropietario(propietario)
        self.setDate()
        self.setTipo('NN')
        self.setPublicado(True)
        self.setArrendado(False)

    def toString(self):
        srt = "["+ "Id:"+str(self.id)+" Nombre:"+str(self.nombre)+" Renta mensual:"+str(self.precio)+" Fecha de creacion:"+str(self.date)+"\n Tipo de articulo:"+str(self.tipo)+" Propietario:"+str(self.propietario) +" ]"
        return srt

    @staticmethod
    def BuscarArticuloPorId(id_a_buscar,list_art = []):
        for art in list_art:
            if art.getId() == int(id_a_buscar):
                return art

    def _setId(self,id_articulos):
        Articulo.id_articulos+=1
        self.id = Articulo.id_articulos
    def getId(self):
        return self.id_usuario
    def setPrecio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setPropietario(self,propietario):
#        for usr in Usuario.users:
#            if usr == propietario:
                self.propietario = propietario
    def getPropietario(self):
        return self.propietario
    def setDate(self):
        self.date = time.asctime()
    def setTipo(self,tipo):
        self.tipo = tipo
    def setPublicado(self,estado):
        self.publicado = estado
    def setArrendado(self,estado):
        self.arredado = estado
