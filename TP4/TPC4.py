import random

lista_interna=[]

def criarlista(n):
    if len(lista_interna)!=0:
        lista_interna.clear()
    for num in range(1,n+1):
        x = random.randint(1,100)
        lista_interna.append(x)
    return lista_interna

def lerlista(n):
    if len(lista_interna)!=0:
        lista_interna.clear()
    for num in range(n):
        x=int(input(f"\nIntroduza o nº {num+1} a ser adicionado à lista:"))
        lista_interna.append(x)
    return lista_interna

def somalista(lista):
    soma=0
    for num in lista:
        soma=soma+num
    return soma

def medialista(lista):
    if len(lista)==0:
        return 0
    soma=somalista(lista)
    return soma/len(lista)

def maiorlista(lista):
    maior =lista[0]
    for num in lista:
        if num>maior:
            maior=num
    return maior

def menorlista(lista):
    menor =lista[0]
    for num in lista:
        if num<menor:
            menor=num
    return menor

def crescente(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return ("\nNÃO, a lista não está ordenada por ordem crescente.")
    return ("\nSIM, a lista está ordenada por ordem crescente.")

def decrescente(lista):
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            return ("\nNÃO, a lista não está ordenada por ordem decrescente.")
    return ("\nSIM, a lista está ordenada por ordem decrescente.")

def procura(lista):
    elemento=int(input("\nQue elemento quer procurar na lista?"))
    if elemento in lista:
        return (f"\nPosição: {lista.index(elemento)}")
    else:
        return -1

def menu():

    print("\n----------MENU----------")
    print("Opção 1 - Criar Lista")
    print("Opção 2- Ler Lista")
    print("Opção 3- Soma")
    print("Opção 4- Média")
    print("Opção 5- Maior")
    print("Opção 6- Menor")
    print("Opção 7- Ordenada por ordem crescente")
    print("Opção 8- Ordenada por ordem decrescente")
    print("Opção 9- Procura um elemento")
    print("Opção 0- Sair")


cond = True
while cond:
    menu()
    opcao=int(input("\nIntroduza a opção pretendida:"))
    
    if opcao==1:
        n=int(input("\nIntroduza o nº de elementos da lista que deseja criar:"))
        print(f"\nCriou a lista {criarlista(n)}. Esta é agora a sua lista interna.")
    elif opcao==2:
        n=int(input("\nQuantos números quer introduzir na lista?"))
        print(f"\nCriou a lista {lerlista(n)}. Esta é agora a sua lista interna.")
    elif opcao==3:
        print(f"\nA soma dos elementos da lista é {somalista(lista_interna)}.")
    elif opcao==4:
        print(f"\nA média dos elementos da lista é {medialista(lista_interna)}.")
    elif opcao==5:
        print(f"\nO maior elemento da lista é {maiorlista(lista_interna)}.")
    elif opcao==6:
        print(f"\nO menor elemento da lista é {menorlista(lista_interna)}.")
    elif opcao==7:
        print(crescente(lista_interna))
    elif opcao==8:
        print(decrescente(lista_interna))
    elif opcao==9:
        print(procura(lista_interna))
    elif opcao==0:
        cond=False
        print(f"\nLista interna: {lista_interna}")
        print("\nSaiu da aplicação!")
    else:
        print("\nOpção inválida.")