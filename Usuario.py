import time
class Usuario:

    identificacion = 0
    calificacion = 3
    _password = None
    nombre = None
    usuarios = {}
    date = None
    dickeys = []
    calificadores = 1     #Variable tipo contador
    
    def __init__(self,identificacion,nombre,_password):
        self.setIdentificacion(identificacion)
        self.setNombre(nombre)
        self.setPassword(_password)
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
        self.calificadores+=1
        self.calificacion = (self.calificacion+calificacion)/(self.calificadores)

    def getCalificacion(self):
        return self.calificacion

    def setDate(self):
        if self.date == None:
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