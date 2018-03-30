from Comentario import *
import time
class Articulo:

    iva = 0.19
    num_articulos = 0
    comentarios = []
    date=None
    tipo=None
    publicado=True
    arrendado=False

    def __init__(self,id,precio,nombre,tipo):
        self.setId(id)
        self.setPrecio(precio)
        self.setNombre(nombre)
        self.setDate()
        self.setTipo(tipo)

    def toString(self):
        srt = "id= " + str(self.id) +" precio de renta= "+str(self.precio_renta)+ " nombre= "+str(self.nombre)
        return srt

    @staticmethod
    def BuscarArticuloPorId(id_a_buscar,list_art = []):
        for art in list_art:
            if art.getId() == int(id_a_buscar):
                return art


    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id
    def setPrecio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return precio
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return nombre
    
    def setDate(self):
        self.date=time.asctime()

    def setTipo(self,tipo):
        self.tipo=tipo

#    def setComentario(self,comentario):
#        comentarios.append(self.comentario)
#    def getComentarios(self):
#        return comentarios

#    def setIva(self,iva):
#        self.iva = iva
#    def getIva(self):
#        return self.iva
#    def setNumArticulos(self,num):
#        self.num = num_articulos
#    def getNumArticulos(self):
#        return num_articulos
