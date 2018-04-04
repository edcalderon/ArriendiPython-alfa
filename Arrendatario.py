from Usuario import *

class Arrendatario(Usuario):

    arrendatarios = []     #Lista de objetos

    def __init__(self):
        Usuario.__init__(self,nombre,_password)

    def _getArrendatarios():
        Arrendatario.arrendatarios.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendatario):
                Arrendatario.arrendatarios.append(Usuario.getUsuario(i))

    def mejoresArrendatarios():     #Retorna una lista con los mejores arrendatarios de manera descendente
        listado=[]
        Arrendatario._getArrendatarios()
        Arrendatario._Arrendatarios.sort(key=lambda arrendatario: arrendatario.calificacion , reverse=True)     #Ordena por el atributo calificacion
        for i in range(0,len(Arrendatario._Arrendatarios)):
            obj=Arrendatario.arrendatarios[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(int(aux2))
        return listado

    def AllGets(self):
        return super()._AllGets()
