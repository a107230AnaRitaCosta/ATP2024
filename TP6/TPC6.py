
def idexistealuno(turma,id):
    cond=False
    for aluno in turma:
        if aluno[1]==id:
            cond=True
    return cond


def criarturma(turma):
    n_alunos=int(input("A turma vai ser constituída por quantos alunos?"))
    i=1
    while i<=n_alunos:
        nome=input("\nIntroduza o nome do aluno:")
        id=input("Introduza o id do aluno:")
        if not idexistealuno(turma,id):
            notaTPC=int(input("Introduza a nota do aluno no TPC:"))
            notaProj=int(input("Introduza a nota do aluno no projeto:"))
            notaTeste=int(input("Introduza a nota do aluno no teste:"))
            aluno=(nome, id, [notaTPC, notaProj, notaTeste])
            turma.append(aluno)
            i=i+1
        else:
            print("Esse aluno já está na turma!")
    return turma

def inseriraluno(turma,alunonovo):
    if not idexistealuno(turma,alunonovo[1]):
        turma.append(alunonovo)
    else:
        print("Esse aluno já está na turma!")
    return turma

def listarturma(turma):
    print("\n------Alunos da turma------")
    for aluno in turma:
        print(f"Nome: {aluno[0]} | id: {aluno[1]} | Notas- TPC: {aluno[2][0]}; Projeto: {aluno[2][1]}; Teste: {aluno[2][2]}")
    return

def consultarporid(turma,id):
    for aluno in turma:
        if id==aluno[1]:
            print(f"\nid: {aluno[1]} | Nome: {aluno[0]} | Notas- TPC: {aluno[2][0]}; Projeto: {aluno[2][1]}; Teste: {aluno[2][2]}")
    return 

def guardarturma(turma,nomef):
    file = open(nomef,"w")
    for aluno in turma:
        file.write(str(aluno[0]) + " | " + str(aluno[1]) + " | " + str(aluno[2][0]) + " @ " + str(aluno[2][1]) + " @ " + str(aluno[2][2]))
        file.write("\n")
    file.close()
        


def carregarturma(nomef):
    turma=[]
    file = open(nomef,"r")
    for line in file:
        identificacao=line.split(" | ")
        nome,id,notas=identificacao[0],identificacao[1],identificacao[2]
        nota=notas.split(" @ ")
        notaTPC,notaProj,notaTeste=nota[0],nota[1],nota[2]
        aluno=(nome,id,[int(notaTPC),int(notaProj),int(notaTeste)])
        turma.append(aluno)
    file.close()
    return turma


def menu():
    print("""\n----------MENU----------
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar a turma
    (4) Consultar um aluno por id
    (5) Guardar a turma em ficheiro
    (6) Carregar uma turma dum ficheiro
    (0) Sair da aplicação
    """)


opcao=1
turma=[]
cond=True
while opcao!=0 and cond:
    menu()
    opcao=int(input("\nIntroduza uma opção:"))
    if opcao==1:
        print(criarturma(turma))
    elif opcao==2:
        if turma!=[]:
            nome_n=input("\nIntroduza o nome do aluno para inserir na turma:")
            id_n=input("Introduza o id do aluno novo:")
            notaTPC_n=int(input("Introduza a nota do aluno novo no TPC:"))
            notaProj_n=int(input("Introduza a nota do aluno novo no projeto:"))
            notaTeste_n=int(input("Introduza a nota do aluno novo no teste:"))
            alunonovo=(nome_n, id_n, [notaTPC_n, notaProj_n, notaTeste_n])
            turma_n=inseriraluno(turma,alunonovo)
            print(turma_n)
        else:
            print("Tem de criar primeiro uma turma. Neste momento a turma está vazia.")
    elif opcao==3:
        listarturma(turma)
    elif opcao==4:
        id_n=input("\nIntroduza o id:")
        condicao=True
        i=0
        while condicao==True and i<len(turma):
            i=i+1
            for a in turma:
                if id_n==a[1]:
                    consultarporid(turma,id_n)
                    condicao=False
        if condicao==True:
            print("O id que introduziu não corresponde a um aluno da turma.")
            id=input("Introduza novamente o id:")

    elif opcao==5:
        guardarturma(turma,"turma_f.txt")
        print("A turma foi guardada num ficheiro de nome turma_f.")
    elif opcao==6:
        print(carregarturma("turma_f.txt") )
    elif opcao!=0:
        print("\nOpção inválida. Tente novamente.")
    elif opcao==0:
        cond=False
if opcao==0:
    print(f"\nTurma: {turma}")
    print("Saiu da aplicação!!")