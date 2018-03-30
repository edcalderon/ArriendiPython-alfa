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
        if identificacion in Usuario.usuarios:
            print('Error')      #print temporal
        else:
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

    def _AllGets(self):
        atributos=[]
        aux1=self.getIdentificacion()
        aux2=self.getNombre()
        aux3=self.getPassword()
        aux4=self.getCalificacion()
        aux5=self.getDate()
        atributos.append(aux1)
        atributos.append(aux2)
        atributos.append(aux3)
        atributos.append(aux4)
        atributos.append(aux5)
        return atributos
