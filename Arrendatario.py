from Usuario import *
from Mensaje import *
from Articulo import *

class Arrendatario(Usuario):

    arrendatarios = []     #Lista de objetos

    def __init__(self,nombre,_password,cedula,celular,direccion):
          Usuario.__init__(self,nombre,_password)
          self.setCedula(cedula)
          self.setCelular(celular)
          self.setDireccion(direccion)
          

    def toString(self):
         return "[Cedula:%s, Celular:%s, Dirreción:%s]" %(str(self.getCedula()),self.getCelular(),self.getDireccion())

    def setCedula(self,cedula):
         self.cedula = cedula
    def getCedula(self):
         return self.cedula
    def setCelular(self,celular):
         self.celular= celular
    def getCelular(self):
         return self.celular
    def setDireccion(self,direccion):
         self.direccion= direccion
    def getDireccion(self):
         return self.direccion

    def _getArrendatarios():
        Arrendatario.arrendatarios.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendatario):
                Arrendatario.arrendatarios.append(Usuario.getUsuario(i))

    def mejoresArrendatarios():     #Retorna una lista con los mejores arrendatarios de manera descendente
        listado=[]
        Arrendatario._getArrendatarios()
        Arrendatario.arrendatarios.sort(key=lambda arrendatario: arrendatario.calificacion , reverse=True)     #Ordena por el atributo calificacion
        for i in range(0,len(Arrendatario.arrendatarios)):
            obj=Arrendatario.arrendatarios[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(int(aux2))
        return listado

    def AllGets(self):
        return super()._AllGets()

    def MejorPrecioArticulo():
        _list=[]
        type=None
        Mensaje.ImprimirKey('tipoNombre')
        auxInt=int(input())
        if auxInt==1:
            Mensaje.ImprimirKey('tipo')
            option=str(input())
            for i in Articulo.articles:
                aux=Articulo.articles[i]
                if str(aux.tipo)==option:
                    _list.append(aux)
        elif auxInt==2:
            Mensaje.ImprimirKey('nombre')
            option=str(input())
            for i in Articulo.articles:
                aux=Articulo.articles[i]
                if str(aux.nombre)==option:
                    _list.append(aux)
        _list.sort(key=lambda articulo: articulo.precio, reverse=False)
        a=len(_list)
        for i in range(0,a):
            obj=_list[i]
            aux1=obj.nombre
            aux2=obj.tipo
            aux3=obj.precio
            if (obj.arredado)==False:
                aux4='SI'
            elif (obj.arredado)==True:
                aux4='NO'
            aux5=(obj.propietario).nombre
            Mensaje.MejoresArticulos(aux1,aux2,aux3,aux4,aux5)