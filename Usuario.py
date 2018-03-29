import time
class Usuario:

    identificacion = 0
    calificacion = 3
    _password = None
    nombre = None
    usuarios = {}
    date = None
    dickeys=[]
    calificadores=0     #Variable tipo contador
    
    def __init__(self,identificacion,nombre,_password):
        self.setIdentificacion(identificacion)
        self.setNombre(nombre)
        self.setPassword(_password)
        GuardarUsuario(identificacion,nombre,_password)
        self.setDate()
        Usuario._setUsuarios(self)
        Usuario._setDickeys(self)

    def setIdentificacion(self,identificacion):
        self.identificacion = identificacion

    def getIdentificacion(self):
        return self.identificacion

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setPassword(self,_password):
        self._password = _password

    def getPassword(self):
        return self._password

    def setCalificacion(self,calificacion):
        self.calificacion = calificacion

    def getCalificacion(self):
        return self.calificacion

    def setDate(self):
        self.date = time.asctime()

    def getDate(self):
        return self.date

    def _setUsuarios(self):
        Usuario.usuarios.setdefault(self.getIdentificacion(),self)

    def _setDickeys(self):       #Agrega las keys a una lista
        Usuario.dickeys.append(self.getIdentificacion())

    def getKeys():              #Retorna todas las keys de forma ordenada
        Usuario.dickeys.sort()
        return Usuario.dickeys

    def getUsuario(key):        #Retorna un usuario en especifico del diccionario
        return Usuario.usuarios[key]

A=Usuario(1,'a',3)
print(A.getIdentificacion(),A.getNombre(),A.getCalificacion(),A.getPassword(),sep='\n')
print(type(Usuario.usuarios))
print(type(Usuario.usuarios[1]))

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

class Arrendador(Usuario):
    def _init_(self,identificacion,nombre,_password):
        super()._init_(self,identificacion,nombre,_password)
