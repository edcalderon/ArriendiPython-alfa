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

