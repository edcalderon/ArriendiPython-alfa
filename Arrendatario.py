from Usuario import *
from Mensaje import *
from Articulo import *
from Renta import *

class Arrendatario(Usuario):

    arrendatarios = []     #Lista de objetos

    def __init__(self,nombre,_password,cedula,celular,direccion):
        Usuario.__init__(self,nombre,_password)
        self.setCedula(cedula)
        self.setCelular(celular)
        self.setDireccion(direccion)


    def toString(self):
         return "[Cedula:%s, Celular:%s, Dirreción:%s]" % (str(self.getCedula()),self.getCelular(),self.getDireccion())

    def setCedula(self,cedula):
         self.cedula = cedula
    def getCedula(self):
         return self.cedula
    def setCelular(self,celular):
         self.celular = celular
    def getCelular(self):
         return self.celular
    def setDireccion(self,direccion):
         self.direccion = direccion
    def getDireccion(self):
         return self.direccion

    def _getArrendatarios():
        Arrendatario.arrendatarios.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendatario):
                Arrendatario.arrendatarios.append(Usuario.getUsuario(i))

    def AllGets(self):
        return super()._AllGets()

    def mejoresArrendatarios():     #Retorna una lista con los mejores arrendatarios de manera descendente
        from Mensaje import Mensaje
        Mensaje.ImprimirKey('MejoresArrendadtarios')
        _Users = {}
        _arrendatarios=[]
        _Users=Usuario.GetAllUsuarios()
        for i in _Users:
            obj=_Users[i]
            if obj.isArrendatario==True:
                _arrendatarios.append(obj)
        _arrendatarios.sort(key=lambda arrendatario: arrendatario.calificacion, reverse=True)     #Ordena por el atributo calificacion
        for i in range(0,len(_arrendatarios)):
            obj = _arrendatarios[i]
            aux1=obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getCalificacion()
            Mensaje.IdNombreCalificacion(aux1,aux2,aux3)

    def CalificarArrendatario():
        from Mensaje import Mensaje
        Mensaje.ImprimirKey('MejoresArrendadtarios')
        _Users={}
        _Users=Usuario.GetAllUsuarios()
        for i in _Users:
            obj=_Users[i]
            if obj.isArrendatario==True:
                aux1=obj.id
                aux2=obj.nombre
                aux3=obj.calificacion
                Mensaje.IdNombreCalificacion(aux1,aux2,aux3)
        Mensaje.ImprimirKey('Calificar')
        _id=int(input())
        _user=Usuario.getUsuario(_id)
        Mensaje.ImprimirKey('NuevaCalificacion')
        _calificacion=int(input())
        _user.setCalificacion(_calificacion)
        aux1=_user.nombre
        aux2=_user.calificacion
        aux3=_user.calificadores
        Mensaje.Calificacion(_id,aux1,aux2,aux3)
