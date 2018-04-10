from Usuario import *
from Mensaje import *
from Renta import *

class Arrendador(Usuario):

    arrendadores = []     #Lista de objetos

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

    def _getArrendadores():
        Arrendador.arrendadores.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendador):
                Arrendador.arrendadores.append(Usuario.getUsuario(i))

    def PeoresArrendadores():     #Retorna una lista con los peores arrendadores
        from Mensaje import Mensaje
        Mensaje.ImprimirKey('PeoresArrendadores')
        _Users = {}
        _arrendadores=[]
        _Users=Usuario.GetAllUsuarios()
        for i in _Users:
            obj=_Users[i]
            if obj.isArrendador==True:
                _arrendadores.append(obj)
        _arrendadores.sort(key=lambda arrendador: arrendador.calificacion, reverse=False)     #Ordena por el atributo calificacion
        for i in range(0,len(_arrendadores)):
            obj = _arrendadores[i]
            aux1=obj.getId()
            aux2 = obj.getNombre()
            aux3 = obj.getCalificacion()
            Mensaje.IdNombreCalificacion(aux1,aux2,aux3)