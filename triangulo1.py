class triangulo:
        def __init__(self, base, altura): #el int es el constructor que se llama cuando el objeto se crea este tomra un parametro que lo utiliza para iniciar el atributo esta tomara dos parametros base y altura
                self.base = base
                self.altura = altura
        def calculr_area(self):
                return self.base * self.altura/2
        
base = float (input("ingrese base:"))
altura =  float (input("ingrese altura:"))

area= triangulo(base, altura)
resultado = area.calculr_area()
print ("la area es:", resultado ) 

#el constructor se crea automaticamente cuando se crea un objeto 
#elobjeto se crea cuando se llama a la clase como si fuera funcion  
# el constructor se ejecuta cundo se guarda en int la informacion metida
#para spasar de P.Estructurada a POO tenecitas agrupar los parametros en una clase con un int

#colocarle funcon y con puras funciones sin init  y sin constructor
#con funcion y sin init sumar y carcular area resultado