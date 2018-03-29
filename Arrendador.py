from Usuario import * 

class Arrendador(Usuario):
    _Arrendadores = []     #Lista de objetos
    
    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)

    def _getArrendadores():
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendador):
                Arrendador._Arrendadores.append(Usuario.getUsuario(i))

    def mejoresArrendadores():      #Retorna una lista con los mejores arrendadres de manera descendente
        Arrendador._getArrendadores()
        sorted(Arrendador._Arrendadores, key=lambda arrendador: Arrendador.calificacion)     #Ordena por el atributo calificacion
        for i in range(0,len(Arrendador._Arrendadores)):
            obj=Arrendador._Arrendadores[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(aux2)
        return listado
