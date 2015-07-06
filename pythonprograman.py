

#misma idea de antes pero  en python, (php era utril para mostrar en una ttabla html, pero aprender el lenguaje de cero es mucho tiempo)
#6 niveles, primeras 6 celdas un nivel,seungas 5 otro, etc
#Inicilizo las 21 celdas con el vallor 0 (valor asignado para celdas desconocidas)
import time
sinresolver = []
list=[0]*22 #22 entradas con 0s 
num=0
class Celda:
	def __init__(self,pos):
		self.pos = pos
		list[self.pos] = int(raw_input("Ingresa valor de celda " + str(num) + ": ") )
		num+= 1
		self.hijoizquierda=self.set_Hijo_izq()
		self.hijoderecha=self.set_Hijo_der()
		self.level= self.nivel()
		sinresolver.apend(self)
		
	def set_Hijo_izq(self):
		if (self.pos <=21 and self.pos >= 16):
                    	return 1
            	else:
                    	self.hijoi = self.pos + self.levell
                    	return self.hijoi


        def set_Hijo_izq(self):
                if (self.pos <=21 and self.pos >= 16):
                    	return 1
            	else:
                    	self.hijod = self.pos + self.level +1
                    	return self.hijod

	def calcular(self):
		
		if(list[self.pos]== 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] != 0):
	               	 list[self.pos] = list[self.hijoderecha] + list[self.hijoizquierda]

		elif(list[self.pos]!= 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] == 0):
	               		list[self.hijoizquierda] = list[self.pos] - list[self.hijoderecha]


		elif(list[self.pos]!= 0 and list[self.hijoderecha] == 0 and list[self.hijoizquierda] != 0):
	               	list[self.hijoderecha] = list[self.pos] - list[self.hijoizquierda]


		if(list[self.pos]!= 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] != 0):
	        	self.a = self.cacl()
	               	if(self.a == 1):
	                	return 1

                return 0
		
	
      	def calc(self):
               	 if (list[self.pos] == list[self.hijoderecha] + list[self.hijoizquierda]):
                        		return 1
               	else:
                       
            			print("Error, la pirámide no se puede resolver")
               		quit()
		
	def nivel(self):
		if(self.pos<2):
			self.nivel=1
		elif(self.pos<4):
			self.nivel=2
		elif(self.pos<7):
			self.nivel=3
		elif(self.pos<11):
			self.nivel=4
		elif(self.pos<16):
			self.nivel=5
		else:
			self.nivel=6
	
	
class Piramide:
	def __init__(self):
	
		start_time = time.time()
		self.ciclo()

  	
  	def ciclo(self):
  		#Tiempo de inicio de ejecucion
  		If(time.time() – Start_time)==30:
  		#Si la cola queda sin elementos o el tiempo llega a 30 segundos el programa finaliza
  			while True: 
				if not(self.sinresolver):
					self.imprimir()
		  			break
		  		else:
		  			self.primero=self.sinresolver[1]
		  			if(self.primero.calcular==1):
		  				self.sinresolver.remove(primero)
					else:
						self.a=self.sinresolver.pop(1)
						self.sinresolver.append(a)	
  				else:
  					print("No se puede resolver la pirámide")
  					quit()
  			
	def imprimir(self):
	 	print("La piramide completa")
		print(" " +" " +" " +" " +" " +" " +" " +" " +" " +" " +str(list[1]))

		print(" " +" " +" " +" " +" " +" " +" " +" " +" " +str(list[2])+ " " +str(list[3]))

		print(" " +" " +" " +" " +" " +" " +" " +str(list[4])+" " +  str(list[5])+" " +str(list[6]))
		print(" " +" " +" " +" " +" "+" " +str(list[7])+" " +  str(list[8])+" " +str(list[9])+" " +str(list[10]))
		print(" " +" " +" " +" " +" " +str(list[11])+" " +" " + str(list[12])+" " +" " +str(list[13])+" " +" " +str(list[14])+" " +" " +str(list[15]))
		print(" " +" " +" " +str(list[16])+ " " +" " +str(list[17])+" " +" " +str(list[18])+" " +" " +str(list[19])+" " +" " +str(list[20])+" " +" " +str(list[21]))
		tiempofinal=(time.time() - start_time))
		print("El programa finalizo en"+" "+tiempofinal+" segundos")	
		


print ("La piramide se ingresa desde arriba hacia abajo siendo la posicion numero uno la punta de la piramide:")


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

Celda16 = Celda(16)
Celda17 = Celda(17)
Celda18 = Celda(18)
Celda19 = Celda(19)
Celda20 = Celda(20)
Celda21 = Celda(21)
Pira=Piramide()




