from Usuario import * 

class Arrendatario(Usuario):
    
    _Arrendatarios = []     #Lista de objetos

    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)

    def _getArrendatarios():
        Arrendatario._Arrendatarios.clear()
        orderkeys = Usuario.getKeys()
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(i),Arrendatario):
                Arrendatario._Arrendatarios.append(Usuario.getUsuario(i))
                
    def mejoresArrendatarios():     #Retorna una lista con los mejores arrendatarios de manera descendente
        listado=[]
        Arrendatario._getArrendatarios()
        Arrendatario._Arrendatarios.sort(key=lambda arrendatario: arrendatario.calificacion , reverse=True)     #Ordena por el atributo calificacion
        for i in range(0,len(Arrendatario._Arrendatarios)):
            obj=Arrendatario._Arrendatarios[i]
            aux1=obj.getNombre()
            aux2=obj.getCalificacion()
            listado.append(aux1)
            listado.append(int(aux2))
        return listado

    def AllGets(self):
        return super()._AllGets()