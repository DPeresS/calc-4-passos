import os
import sys
def saudacao(n, hr): #função de saudação e hora
    os.system("cls")
    if(hr>12 and hr<=17):
        print("Boa tarde", n)
    elif(hr>17 and hr<=24):
        print("Boa noite", n)
    else:
        print("Bom dia", n)

def soma(a,b): #função soma
        resultado=a+b
        return print(a,"+",b,"=", resultado)
def subtracao(a,b): #função subtracao
                resultado=a-b
                return print(a,"-",b,"=", resultado)
def multiplicacao(a,b): #funcao multiplicacao
                resultado=a*b
                return print(a,"*",b,"=", resultado)
def divisao(a,b): #funcao divisao ok
                if b==0:
                    return print("Não foi possível realizar a divisão por 0") 
                else:
                    resultado=a/b
                    return print(a, "/", b, "=", resultado) 

def operacoes(op):
    match op:
        case 1:
            soma(n1,n2)
        case 2:
            subtracao(n1,n2)
        case 3:
            multiplicacao(n1,n2)
        case 4:
            divisao(n1,n2)
        case 5:
            sys.exit()


inicio = True
while(inicio==True or opcao>=1 and opcao<=4):
      print("")       
      print("Informe a opção desejada: ")
      print("(1) Adição             (2) Subtração")
      print("(3) Multiplicação      (4) Divisão")
      print("(5) SAIR")
      opcao=int(input("OPÇÃO: "))
      while(opcao<1 or opcao>5):
            opcao=int(input("Informe uma opção válida: "))
    


      if opcao==5:
           print("PROGRAMA ENCERRADO")
           sys.exit()
      
      n1=int(input("Digite um número: "))
      n2=int(input("Digite outro número: "))
      os.system("cls")
      operacoes(opcao)
      inicio = False
      
      





