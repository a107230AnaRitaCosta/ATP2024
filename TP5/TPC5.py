# Modelo:
#   Cinema = [Sala]
#   Sala = [nlugares, vendidos, filme]
#   nlugares = Int
#   vendidos = [lugar]
#   filme = String
#   lugar = int

def existeSala(cinema,novasala):
    cond=False
    for sala in cinema:
        if sala[2]==novasala[2]:
            cond=True
    return cond

def inserirSala(cinema, sala ): 
    if not existeSala(cinema,sala):
        cinema.append(sala)
    else:
        print("Já existe um sala a exibir esse filme!")
    return cinema

def listar( cinema ):
    print("\n---------Lista de Salas---------")
    for sala in cinema:
        print(f"\nNome do filme: {sala[2]} | Nº de lugares da sala: {sala[0]}")
    return

#   Sala = [nlugares, vendidos, filme]
def disponivel( cinema, filme_s, lugar ):
    cond=True
    for sala in cinema:
        if sala[2]==filme_s and lugar<=sala[0]:
            if lugar in sala[1]:
                cond=False
    return cond

def vendebilhete( cinema, filme_s, lugar):
    for sala in cinema:
        if filme_s == sala[2]:
            if disponivel(cinema,filme_s,lugar):
                sala[1].append(lugar)
                sala[1].sort()
            else:
                print("\nO lugar que escolheu já está ocupado.")
    return cinema

#   Sala = [nlugares, vendidos, filme]
def listardisponibilidades( cinema ):
    for sala in cinema:
        if sala[0]>len(sala[1]):
            lugaresdisponiveis=sala[0]-len(sala[1])
            print(f"\nA sala do filme {sala[2]} com capacidade para {sala[0]} lugares tem {lugaresdisponiveis} lugares disponíveis.") 
        else:
            print(f"\nA sala do filme {sala[2]} com capacidade para {sala[0]} lugares tem todos os lugares ocupados.")
    return


def listarsala(cinema, filme_s):
    for sala in cinema:
        if sala[2]==filme_s:
            print(f"\nA sala do filme {filme_s} tem {sala[0]} lugares e estão {len(sala[1])} ocupados.") 
    return

def removesala(cinema, filme_s):
    for sala in cinema:
        if filme_s==sala[2]:
            cinema.remove(sala)
            print(f"\nA sala do filme {sala[2]} foi removida.")
    return cinema

def menu():
    print("""\n----------MENU----------
    (1) Inserir Sala
    (2) Listar todas as salas 
    (3) Consultar se Sala / lugar disponível
    (4) Vender Bilhete
    (5) Ver disponibilidades
    (6) Listar Sala
    (7) Remover Sala
    (0) Sair
    """)

# Aplicação para gerir cinema

opcao = 1
cinema=[]
cond=True
while opcao != 0 and cond:
    menu()
    opcao = int(input("\nIntroduza uma opção: "))
    if opcao==1:
        filme_s=input("\nIntroduza o nome do filme:")
        nlugares=int(input("Introduza o nº de lugares da sala:"))
        nocupados=int(input("Introduza o nº de lugares ocupados/ bilhetes vendidos da sala:"))
        while nocupados>nlugares:
            print("\nO nº de lugares ocupados não pode ser superior à capacidade da sala!")
            nlugares=int(input("Introduza o nº de lugares da sala:"))
            nocupados=int(input("Introduza o nº de lugares ocupados/ bilhetes vendidos da sala:"))
        i=1
        vendidos=[]
        while nocupados>=i and nocupados<=nlugares:
            lugar=int(input(f"Introduza o {i}º lugar ocupado."))
            vendidos.append(lugar)
            i=i+1
        vendidos.sort()    
        sala1=[nlugares,vendidos,filme_s]
        cinema=inserirSala(cinema,sala1)
        print(cinema)
    elif opcao==2:
        listar(cinema)
    elif opcao==3:
        filme_s=input("Introduza o nome do filme:")
        condicao=True
        i=0
        while condicao==True and i<len(cinema):
            i=i+1
            for sala in cinema:
                if filme_s==sala[2]:
                    lugar=int(input("Introduza o lugar da sala:"))
                    print(disponivel(cinema,filme_s,lugar))
                    condicao=False
        if condicao==True:
            print("Esse filme não está em exibição neste cinema.")       
        
    elif opcao==4:
        filme_s=input("Qual o filme que deseja ver?")
        condicao=True
        i=0
        while condicao==True and i<len(cinema):
            i=i+1
            for sala in cinema:
                if filme_s==sala[2]:
                    lugar=int(input(f"Para que lugar da sala do filme {filme_s} quer comprar o bilhete?"))
                    print(f"O lugar {lugar} está agora ocupado.")
                    print(vendebilhete(cinema,filme_s,lugar))
                    condicao=False
        if condicao==True:
            print("Esse filme não está em exibição neste cinema. ")
  

    elif opcao==5:
        print(listardisponibilidades(cinema))

    elif opcao==6:
        filme_s=input("Qual o filme da sala que deseja receber as informações?")
        condicao=True
        i=0
        while condicao==True and i<len(cinema):
            i=i+1
            for sala in cinema:
                if filme_s==sala[2]:
                    listarsala(cinema,filme_s)
                    condicao=False
        if condicao==True:
            print("Esse filme não está em exibição neste cinema. ")
            
        
    elif opcao==7:
        filme_s=input("Nome do filme da sala para retirar:")
        print(removesala(cinema,filme_s))
    elif opcao!=0:
        print("Opção inválida!")
    elif opcao==0:
        cond=False
if opcao==0:
        print(f"Lista de salas:{cinema}")
        print("Saiu da aplicação. Até à próxima!")

  