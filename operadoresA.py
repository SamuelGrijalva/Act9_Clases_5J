print("Act 9 clases v2")
print("Samuel Grijalva Mat: 22308051281205")
#zona de class
class Operadores1205:
    #zona de funciones
    def suma1205(self,E,N):
        s1205=E+N
        print(f"La suma de {E} + {N} = {s1205}")
    def resta1205(self,E,N):
        s1205=E-N
        print(f"La resta de {E} - {N} = {s1205}")
    def multiplicacion1205(self,E,N):
        s1205=E*N
        print(f"La multiplicacion de {E} * {N} = {s1205}")
    def division1205(self,E,N):
        s1205=E/N
        print(f"La division de {E} / {N} = {s1205}")
    def modulo1205(self,E,N):
        s1205=E%N
        print(f"El modulo de {E} % {N} = {s1205}")    
    def exponente1205(self,E,N):
        s1205=E**N
        print(f"El exponente de {E} ** {N} = {s1205}")      
    def cociente1205(self,E,N):
        s1205=E//N
        print(f"El cociente de {E} // {N} = {s1205}")     
#zona de creacion del objeto
OperadorGrijalva=Operadores1205()

#zona de uso de objetos
print("Funcion Suma")
OperadorGrijalva.suma1205(5,4)
print("Funcion Resta")
OperadorGrijalva.resta1205(9,7)
print("Funcion Multiplicacion")
OperadorGrijalva.multiplicacion1205(3,7)
print("Funcion Division")
OperadorGrijalva.division1205(53,12)
print("Funcion Modulo")
OperadorGrijalva.modulo1205(53,4)
print("Funcion Exponente")
OperadorGrijalva.exponente1205(2,9)
print("Funcion Cociente")
OperadorGrijalva.cociente1205(12,4)