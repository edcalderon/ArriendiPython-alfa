from pathlib import Path
data_folder = Path("C:/")

def GuardarArticulo(id_articulo,precio,nombre,propietario):
	#GuardarArticulo(self.getId(),precio,nombre,propietario,"NN",True,False)
	id_articulo=str(id_articulo)
	precio=str(precio)
	nombre=str(nombre)
	propietario=str(propietario)
	guardar=open("baseA.txt","a")
	guardar.write(id_articulo)
	guardar.write(",")
	guardar.write(precio)
	guardar.write(",")
	guardar.write(nombre)
	guardar.write(",")
	guardar.write(propietario)
	guardar.write(",")
	guardar.write("NN")
	guardar.write(",")
	#True de Publicado
	guardar.write("True")
	guardar.write(",")
	#Flase de Arrendado
	guardar.write("False")
	guardar.write(",")
	guardar.write("\n")
	guardar.close()

def GuardarUsuario(id_usuarios,nombre,_password,IsArrendador):
	id_usuario=str(id_usuarios)
	nombre=str(nombre)
	IsArrendador=str(IsArrendador)
	_password=str(_password)
	#diccionario = { 'id_usuario':id_usuario,'nombre': nombre, '_password': _password, 'IsArrendador':IsArrendador}
	#diccionario=str(diccionario)
	guardar=open("baseU.txt","a")
	guardar.write(id_usuarios)
	guardar.write(",")
	guardar.write(nombre)
	guardar.write(",")
	guardar.write(_password)
	guardar.write(",")
	guardar.write("usuario")
	guardar.write(",")
	guardar.write(IsArrendador)
	guardar.write("\n")
	#guardar.write(diccionario)
	#guardar.write("\n")
	guardar.close()

def GuardarArrendador(id_usuarios,nombre,_password,IsArrendador,cedula,celular,direccion):
	ide=str(id_usuarios)
	nombre=str(nombre)
	_password=str(_password)	
	IsArrendador=str(IsArrendador)
	cedula=str(cedula)
	celular=str(celular)
	direccion=str(direccion)
	IsArrendador=str(IsArrendador)

	guardar=open("baseU.txt","a")
	guardar.write(ide)
	guardar.write(",")
	guardar.write(nombre)
	guardar.write(",")
	guardar.write(_password)
	guardar.write(",")
	guardar.write("Arrendador")
	guardar.write(",")
	guardar.write(cedula)
	guardar.write(",")
	guardar.write(celular)
	guardar.write(",")
	guardar.write(direccion)
	guardar.write(",")
	guardar.write(IsArrendador)
	guardar.write("\n")
	guardar.close()
	#f=  open("baseU.txt", "r")
    #lines = f.readlines() 
    #lines.remove("Line you want to delete\n")
    #with open("new_file.txt", "w") as new_f:
    #    for line in lines:        
    #        new_f.write(line)

	#fo = open("baseU.txt", "w")
	#position = fo.tell(id_usuarios);
	#line = fo.readline(id_usuarios)
	#print "Read Line: %s" % (id_usuarios)
	# Now truncate remaining file.
	#fo.truncate()

	'''
	matriz = open("baseU.txt",'r')   
	archivoN = matriz.read() 
	matriz.close()
	matriz = open("baseU.txt",'w')  
	for linea in archivoN:
		print(linea)
		if linea != id_usuario:
			matriz.write(linea)
	matriz.close()
	'''

	
			
