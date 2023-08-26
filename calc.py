n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
print(n1, "+", n2, "=", n1+n2) ##Soma dos valores informados!
print(n1, "-", n2, "=", n1-n2) ##Subtração dos valores informados!
print(n1, "x", n2, "=", n1*n2) ##Multiplicação dos valores informados!

if n2==0:
    print("Não foi possível realizar a divisão por 0") 
else:
    print(n1, "/", n2, "=", n1/n2) 
