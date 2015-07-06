
#misma idea de antes pero  en python, (php era utril para mostrar en una ttabla html, pero aprender el lenguaje de cero es mucho tiempo)
#6 niveles, primeras 6 celdas un nivel,seungas 5 otro, etc
#Inicilizo las 21 celdas con el vallor 0 (valor asignado para celdas desconocidas)
list=[0]*21
#Cada celda tiene un booleano, si es ese booleano es true significa que el triangulo donde se encuentra ha sido resolvido,el ciclo seguira mientras existan ciclos false
class Celda:
	def __init__(self,pos):
		self.pos = pos
		list[self.pos] = int(raw_input("Ingresa valor de celda " + str(num) + ": ") )
		num+= 1
		self.calculable=false
		
	def set_Padre_izq(self):
		padre_izq=self.pos+self.nivel(self)
		return self.padre_izq
	def set_Padre_der(self):
		padre_der=self.pos+self.nivel(self)
		return self.padre_der
	def set_Hijo_izq(self):
	def set_Hijo_der(self):
	def calcular(self):
		
	def nivel(self):
		if(self.pos<2)
			self.nivel=1
		elif(self.pos<4)
			self.nivel=2
		elif(self.pos<7)
			self.nivel=3
		elif(self.pos<11)
			self.nivel=4
		elif(self.pos<16)
			self.nivel=5
		else 
			self.nivel=6
	
	
class Piramide:
	def __init__(self):
		resueltos=0
		i=0
  	
  	def ciclo(self):

 
  		

  		if(resueltos==15):
  			self.imprimir(self)
  		else:
  			if(i==15)
  				print("no es posible resolverla")
  			else:
  				i+=1
  				self.ciclo(self)

  			
	def imprimir(self):
	 	print("La piramide completa")
		print(" " +" " +" " +" " +" " +" " +" " +" " +" " +" " +str(list[1]))

		print(" " +" " +" " +" " +" " +" " +" " +" " +" " +str(list[2])+ " " +str(list[3]))

		print(" " +" " +" " +" " +" " +" " +" " +str(list[4])+" " +  str(list[5])+" " +str(list[6]))
		print(" " +" " +" " +" " +" "+" " +str(list[7])+" " +  str(list[8])+" " +str(list[9])+" " +str(list[10]))
		print(" " +" " +" " +" " +" " +str(list[11])+" " +" " + str(list[12])+" " +" " +str(list[13])+" " +" " +str(list[14])+" " +" " +str(list[15]))
		print(" " +" " +" " +str(list[16])+ " " +" " +str(list[17])+" " +" " +str(list[18])+" " +" " +str(list[19])+" " +" " +str(list[20])+" " +" " +str(list[21]))
				




Celda1 = Celda(1)
Celda2 = Celda(2)
Celda3 = Celda(3)
Celda4 = Celda(4)
Celda5 = Celda(5)
Celda6 = Celda(6)
Celda7 = Celda(7)
Celda8 = Celda(8)
Celda9 = Celda(9)
Celda10 = Celda(10)
Celda11 = Celda(11)
Celda12 = Celda(12)
Celda13 = Celda(13)
Celda14 = Celda(14)
Celda15 = Celda(15)

print "La piramide se ingresa desde arriba hacia abajo siendo la posicion numero uno la punta de la piramide"

