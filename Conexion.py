from Run import *
from Usuario import *
from Articulo import *

class Conexion:

	def setUsuariosBase():
		with open("usuarios.txt", "a+") as file:
			file.write("arriendi,god\n")
			file.write("arriendi2,god2\n")
			file.write("defaultUser1,pass1\n")
			file.write("defaultUser2,pass2\n")

	def cargarUsuarios():
		file = open("usuarios.txt","r")
		for line in file:
			x = line.split(',')
			user = Usuario(x[0],x[1].strip())
			Usuario.users.append(user)
			if x[0] is 'arriendi' or 'arriendi2':
				user.setIsArrendatario(True)
				user.setIsArrendador(True)

	def guardarUsuarios(user,passw):
		 with open("usuarios.txt", "a") as file:
			 srt = user+","+passw
			 file.write(srt+"\n")
			 file.close()

	def setArticulosBase():
		with open("articulos.txt", "a+") as file:
			file.write("30.000,TvFullHD,arriendi\n")
			file.write("999.000,PapelHigienicoTipleHojaMarcaArriendi,arriendi2\n")
			file.write("1000,bananoSinTerminar,defaultUser2\n")

	def cargarArticulos():
		from Run import Run
		with open("articulos.txt", "r") as file:
			for line in file:
				x = line.split(',')
				user = Usuario.BuscarUsuarioPorNombre(x[2].strip(),Usuario.users)
				run = Run()
				if user:
					articulo = Articulo(x[0],x[1],user)
					user.articulos.append(articulo)
					run.articulos.append(articulo)


	def guardarArticulos(precio,nombre,propietario):
		 with open("articulos.txt", "a") as file:
			 srt = precio+","+nombre+","+propietario
			 file.write(srt)

	def cargarRentas():
		from Renta import Renta
		from Run import Run
		file = open("rentas.txt","a+")
		for line in file:
			x = line.split(',')
			articulo = Articulo.BuscarArticuloPorNombre((x[0]),Run.articulos)
			arrendador = Usuario.BuscarUsuarioPorNombre(x[1].strip(),Usuario.users)
			arrendatario = Usuario.BuscarUsuarioPorNombre(x[3].strip(),Usuario.users)
			renta = Renta(articulo,arrendador,x[2],arrendatario)
			Renta.rentas.append(renta)
			arrendador.rentas.append(renta)
			arrendatario.rentas.append(renta)

	def guardarRentas(articulo,arrendador,periodo,arrendatario):
		 with open("rentas.txt", "a") as file:
			 srt = articulo+","+arrendador+","+periodo+","+arrendatario
			 file.write(srt)

	def cargarArrendador():
		from Run import Run
		from Usuario import Usuario
		file = open("Arrendador.txt","a+")
		for line in file:
			x = line.split(',')
			user = Usuario.BuscarUsuarioPorNombre((x[0]),Usuario.users)
			passw = Usuario.BuscarUsuarioPorNombre(x[1].strip(),Usuario.users)
			user = Arrendador(user,passw,x[2],x[3],x[4])
			Arrendador.arrendadores.append(user)

	def guardarArrendador(user,passw,cedula,celular,direccion):
		 with open("Arrendador.txt", "a") as file:
			 srt = user+","+passw+","+cedula+","+celular+","+direccion
			 file.write(srt+"\n")
