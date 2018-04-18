from Comentario import *
import time
from Usuario import *

class Articulo:

    iva = 0.19
    num_articulos = 0
    id_articulos = 0        #contador
    articles = {}
    veces_usado=0

    def __init__(self,precio,nombre,propietario):
        self._setId(Articulo.id_articulos)
        self.setPrecio(precio)
        self.setNombre(nombre)
        self.setPropietario(propietario)
        self.setDate()
        self.setTipo('NN')
        self.comentarios = []
        self.setPublicado(True)
        self.setArrendado(False)
        Articulo.AddArticles(self)

    def AddArticles(self):
        Articulo.articles.setdefault(self.getId,self)

    def toString(self):
        return "[ID:%s, Nombre:%s, Valor Renta Diaria:%s, Fecha De Creacion:%s, Tipo de Articulo:%s, Propietario:%s]" % (str(self.id),self.nombre,str(self.precio),str(self.date),self.tipo,self.propietario.getNombre())

    @staticmethod
    def BuscarArticuloPorId(id_a_buscar,list_art=[]):
        for art in list_art:
            if art.getId() == int(id_a_buscar):
                return art
    @staticmethod
    def BuscarArticuloPorNombre(nombre_a_buscar,list_art=[]):
        for art in list_art:
            if art.getNombre() == nombre_a_buscar:
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
    def setVecesUsado(self):
        self.veces_usado+=1
    def getVecesUsado(self):
        return self.veces_usado

    def MenosUso():
        from Mensaje import Mensaje
        _list = []
        Mensaje.ImprimirKey('NombreUsado')
        _name = str(input())
        for i in Articulo.articles:
            aux = Articulo.articles[i]
            if str(aux.getNombre()) == _name:
                if aux.getArrendado() == False:
                    _list.append(aux)
        _list.sort(key=lambda articulo: articulo.getVecesUsado(), reverse=False)
        _a = len(_list)
        for i in range(0,_a):
            obj = _list[i]
            aux1 = obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getTipo()
            aux4 = obj.getPrecio()
            aux5 = obj.getPropietario().getNombre()
            aux6 = obj.getVecesUsado()
            Mensaje.MenosUsos(aux1,aux2,aux3,aux4,aux5,aux6)

    def MejorPrecioArticulo():
        from Mensaje import Mensaje
        _list = []
        type = None
        Mensaje.ImprimirKey('tipoNombre')
        auxInt = int(input())
        if auxInt == 1:
            Mensaje.ImprimirKey('tipo')
            option = str(input())
            for i in Articulo.articles:
                aux = Articulo.articles[i]
                if str(aux.getTipo()) == option:
                    _list.append(aux)
        elif auxInt == 2:
            Mensaje.ImprimirKey('nombre')
            option = str(input())
            for i in Articulo.articles:
                aux = Articulo.articles[i]
                if str(aux.getNombre()) == option:
                    _list.append(aux)
        _list.sort(key=lambda articulo: articulo.getPrecio(), reverse=False)
        _a = len(_list)
        for i in range(0,_a):
            obj = _list[i]
            aux1 = obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getTipo()
            aux4 = obj.getPrecio()
            if (obj.getArrendado()) == False:
                aux5 = 'SI'
            elif (obj.getArrendado()) == True:
                aux5 = 'NO'
            aux6 = (obj.getPropietario()).getNombre()
            Mensaje.MejoresArticulos(aux1,aux2,aux3,aux4,aux5,aux6)
