from Usuario import * 

class Arrendatario(Usuario):
    _Arrendatarios = []     #Lista de objetos
    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)
    
    def _getArrendatarios():
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendatario):
                Arrendatario._Arrendatarios.append(Usuario.getUsuario(i))

    def mejoresArrendatarios():     #Retorna una lista con los mejores arrendadres de manera descendente
        listado=[]
        Arrendatario._getArrendatarios()
        sorted(Arrendatario._Arrendatarios, key=lambda arrendatario: Arrendatario.calificacion)     #Ordena por el atributo calificacion
        for i in range(0,len(Arrendatario._Arrendatarios)):
            obj=Arrendatario._Arrendatarios[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(aux2)
        return listado
