# Relatorio do tp4
## Data: 2024-10-02
## Autor: Ana Rita Costa - a107230

## Resumo:
O tpc4 consistiu em criar uma aplicação em Python que coloca no monitor um menu e o utilizador escolhe uma das opções do menu,introduzindo o número correspondente. Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu. Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.

Defini uma condição "True", que enquanto não for refutada, ou seja, enquanto o utilizador não escolher a opção 0 para sair do programa, este mostra o menu e pergunta ao utilizador qual a opção que deseja realizar a seguir. A aplicação tem uma variável interna que guarda uma lista de números e que é mostrada quando é criada uma nova lista.
Cada opção corresponde a uma função criada com o nome da operação realizada:
* Na opção 1, é criada uma lista de números aleatórios entre 1 e 100 que será guardada na variável interna. Para isso o computador gera um conjunto de números aleatórios, tantos quantos o utilizador quiser que façam parte da lista. Se, quando esta opção for escolhida, já houver uma lista interna, esta lista já existente deve ser apagada e substituída pela lista agora criada.
* Na opção 2, o utilizador cria uma lista com os números que pretender. Se, quando esta opção for escolhida, já houver uma lista interna, esta lista já existente deve ser apagada e substituída pela lista agora criada.
* Na opção 3, é calculada a soma dos elementos na lista.
* Na opção 4, é calculada a média dos elementos na lista.
* Na opção 5, é calculado o maior elemento da lista.
* Na opção 6, é calculado o menor elemento da lista.
* Na opção 7, a aplicação indica se a lista está ordenada por ordem crescente, comparando cada elemento da lista com o elemento seguinte e vendo se este é maior. 
* Na opção 8, a aplicação indica se a lista está ordenada por ordem decrescente.
* Na opção 9, a aplicação procura um elemento na lista, se este estiver na lista, devolve a sua posição. Se o elemento escolhido não estiver na lista a aplicação devolve -1.

Esta aplicação é então produzida no terminal, sendo aberta a pasta na qual está o código em Python através do terminal. 