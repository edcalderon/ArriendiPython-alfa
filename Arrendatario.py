from Usuario import * 

class Arrendatario(Usuario):
    _Arrendatarios=[]
    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)
    
    def _getArrendatarios():
        orderkeys=Usuario.getKeys();
        for i in orderkeys:
            if isinstance(Usuario.getUsuario(orderkeys[i]),Arrendatario):
                Arrendatario._Arrendatarios.append(Usuario.getUsuario(orderkeys[i]))

    def mejoresArrendatarios():
        Arrendatario._getArrendatarios()
        Arrendatario._Arrendatarios.sort(calificacion)
        for i in Arrendatario._Arrendatarios:
            aux1=super().getUsuario[Arrendatario._Arrendatarios[i]]
            string+=aux1.getNombre(),aux1.getCalificacion()


B=Arrendatario(2,'test','qwert')
B.setCalificacion(4)
C=Arrendatario(3,'test2','asdf')
C.setCalificacion(5)
#print('Mejores:',Arrendatario.mejoresArrendatarios())
print(type(Usuario.usuarios[2]))
print(isinstance(Usuario.usuarios[2],Arrendatario))
print(Usuario.usuarios.keys())
print(type(Usuario.usuarios[1]))
print('keys',Usuario.getKeys())