from Usuario import *

class Arrendador(Usuario):

   arrendadores = []     #Lista de objetos

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

   def _getArrendadores():
        Arrendador.arrendadores.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendador):
                Arrendador.arrendadores.append(Usuario.getUsuario(i))

   def peoresArrendadores():      #Retorna una lista con los peores arrendadres
        listado=[]
        Arrendador._getArrendadores()
        Arrendador._Arrendadores.sort(key=lambda arrendador: arrendador.calificacion)      #Ordena por el atributo calificacion
        for i in range(0,len(Arrendador.arrendadores)):
            obj=Arrendador.arrendadores[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(aux2)
        return listado
