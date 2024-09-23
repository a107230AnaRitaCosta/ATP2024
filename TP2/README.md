# Relatorio do tp2
## Data: 2024-09-18
## Autor: Ana Rita Costa - a107230

## Resumo:
O tpc2 consistiu na criação de um programa para jogar o jogo "Adivinha o número".
O jogo tem duas modalidades:
   * o computador pensa num número entre 0 e 100 e o jogador tenta adivinhar, no menor número de tentativas.
   * o jogador pensa num número entre 0 e 100 e o computador tenta adivinhar,  no menor núemro de tentativas.

 MODALIDADE 1: Utilizei o comando random para que o computador gerasse um nº aleatório entre 0 e 100 que seria o nº em que ele tinha pensado. Se o palpite do utilizador for menor do nº gerado pelo computador, essa mensagem vai ser transmitida ao utilizador e o mesmo acontece se o nº for maior. Entretanto vão sendo contadas as tentativas utilizadas.
   
 MODALIDADE 2: Comecei por definir 0 como o número menor inicial e 100 como o número maior, sendo 0 as tentativas iniciais. Enquanto o nº menor for menor que o nº considerado o maior, o computador vai definir o seu palpite como sendo o ponto médio inteiro entre os números maior e menor estabelecidos. Isto permite chegar ao número pensado na menor quantidade de tentativas. Quando o computador acerta no nº pensado, isto significa que o menor é o mesmo que o maior, então encerra-se o ciclo e chega-se ao fim do jogo. Se o computador não acertar no nº, o jogador refere se o nº pensado é maior ou menor: 
    * se o nº pensado for menor que o dito pelo computador, define-se como maior o nº inserido pelo computador, de forma a diminuir o intervalo de números possíveis.
    * se o nº pensado for maior que o dito pelo computador, define-se como menor o nº inserido pelo computador, de forma a diminuir o intervalo de números possíveis. 

No final, quando o número é descoberto, em ambas as modalidades, o programa exibe qual o nº pensado e quantas tentativas foram utilizadas.

A realização deste tpc foi um pouco complicada porque exige muito tempo de pensamento para relacionar todos os passos para a realização correta do programa. A parte mais complicada para mim foi conseguir entender que condição deveria colocar no ciclo "while" ns modalidade 2, para que o programa funcionasse.
