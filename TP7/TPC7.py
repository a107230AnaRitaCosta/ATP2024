def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        tempmedia=(dia[1]+dia[2])/2
        meteo=(dia[0],tempmedia)
        res.append(meteo)
    return res

def guardaTabMeteo(t, fnome):
    file=open(fnome,'w')
    for dia_ in t:
        data,min,max,prec=dia_
        ano,mes,dia=data
        registo=f"{ano}-{mes}-{dia} & {min} & {max} & {prec}\n"
        file.write(registo) 
    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file=open(fnome,'r')
    for linha in file:
        linha=linha.strip()
        campos=linha.split('&')
        data,min,max,prec=campos
        ano,mes,dia=data.split('-')
        dia=((int(ano),int(mes),int(dia)),float(min),float(max),float(prec))
        res.append(dia)
    file.close()
    return res

def minMin(tabMeteo):
    minima=tabMeteo[0][1]
    for dia in tabMeteo[1:]:
        if dia[1]<minima:
            minima=dia[1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for dia in tabMeteo:
        amplitude=-dia[1]+dia[2]
        meteo=(dia[0],amplitude)
        res.append(meteo)
    return res

def maxChuva(tabMeteo):
    max_prec=tabMeteo[0][2]
    for dia in tabMeteo[1:]:
        if dia[2]>max_prec:
            max_prec=dia[2]
    return (dia[0],max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    for dia in tabMeteo:
        if dia[3]>p:
            res.append((dia[0],dia[3]))

    return res

def maxPeriodoCalor(tabMeteo, p):
    consec_local=0
    consec_global=0
    for dia in tabMeteo:
        if dia[3]<p:
            consec_local=consec_local+1
        else:
            if consec_local> consec_global:
                consec_global=consec_local
            consec_local=0
    if consec_local> consec_global:
                consec_global=consec_local
    return consec_global

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    datas=[f"{data[0]}-{data[1]}-{data[2]}" for data,*_ in t]
    temp_min=[min for _,min,*_ in t]
    temp_max=[max for _,_,max,_ in t]
    

    plt.plot(datas,temp_min,label="Temp Mínima")
    plt.plot(datas,temp_max,label="Temp Máxima")
    plt.xlabel('Data')
    plt.ylabel('Temperatura ºC')
    plt.title('Temperatura Mínima e Máxima')
    plt.legend()
    plt.show()

    return

def grafTabMeteoP(t):
    datas=[f"{data[0]}-{data[1]}-{data[2]}" for data,*_ in t]
    precs=[prec for _,_,_,prec in t]

    plt.bar(datas,precs)
    plt.xlabel('Data')
    plt.ylabel('Precipitação')
    plt.title('Pluviosidade')
    plt.show()

    return 


def menu():
    print("""\n----------MENU----------
    (1) Criar Tabela Meteorológica
    (2) Consultar TEMPERATURA MÉDIA de cada dia
    (3) Guardar tabela meteorológica num ficheiro
    (4) Carrega tabela meteorológica de um ficheiro
    (5) Consultar TEMPERATURA MÍNIMA mais baixa
    (6) Consultar AMPLITUDE TÉRMICA de cada dia
    (7) Consultar PRECIPITAÇÃO MÁXIMA e o seu dia
    (8) Dias com precipitação superior a limite
    (9) Nº de dias consecutivos de precipitação abaixo do limite
    (10) Gráfico Temperatura Máxima e Mínima
    (11) Gráfico pluviosidade
    (0) Sair da aplicação
    """)


tabela=[]
opcao=1
cond=True
while opcao!=0 and cond:
    menu()
    opcao=int(input("\nIntroduza uma opção:"))
    if opcao==1:
        n_dias=int(input("\nIntroduza o nº de dias de registos:"))
        i=1
        while i<=n_dias:
            ano=int(input("\nIntroduza o ano:"))
            mes = int(input("Introduza o mês:"))
            dia = int(input("Introduza o dia:"))
            data = (ano,mes,dia)
            temp_min = float(input("Introduza a temperatura mínima registada nesse dia:"))
            temp_max = float(input("Introduza a temperatura máxima registada nesse dia:"))
            prec = float(input("Intoduza a precipitação registada nesse dia:"))
            dia_= (data,temp_min,temp_max,prec)
            i=i+1
            tabela.append(dia_)
        print(tabela)
    elif opcao==2:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            print(medias(tabela))
    elif opcao==3:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            guardaTabMeteo(tabela, "tabelameteo.txt")    
            print("\nA tabela que criou foi guardada num ficheiro de nome: tabelameteo.txt.")  
    elif opcao==4:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            print(carregaTabMeteo("tabelameteo.txt"))
    elif opcao==5:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            print(minMin(tabela))
    elif opcao==6:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            print(amplTerm(tabela))
    elif opcao==7:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            print(maxChuva(tabela))
    elif opcao==8:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            p=float(input("\nIntroduza o limite p:"))
            print(diasChuvosos(tabela,p))
    elif opcao==9:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            p=float(input("\nIntroduza o limite p:"))
            print(maxPeriodoCalor(tabela,p))
    elif opcao==10:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            grafTabMeteo(tabela)
    elif opcao==11:
        if tabela==[]:
            print("\nNão há dados na tabela. Crie uma tabela usando a opção 1.")
        else:
            grafTabMeteoP(tabela)
    elif opcao!=0:
        print("\nOpção inválida. Tente novamente.")
    elif opcao==0:
        cond=False
if opcao==0:
    print("\nSaiu da aplicação!!")