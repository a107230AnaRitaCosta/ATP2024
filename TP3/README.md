# Relatorio do tp3
## Data: 2024-09-25
## Autor: Ana Rita Costa - a107230

## Resumo:
O tpc3 consistiu no desenvolvimento em Python do código necessário para o jogo dos 21 fósforos.
O jogo tem dois modos: o jogador joga em primeiro lugar e, no segundo modo, o computador começa em primeiro. Neste jogo, quando o computador é o segundo a jogar, deve ganhar sempre o jogo e quando começa a jogar em primeiro lugar, se o utilizador cometer um erro de cálculo, o computador deve passar para a posição de vencedor e ganhar o jogo.

Como não tinha entendido a lógica do jogo e como poderia fazer o computador ganhar nestes casos, tive de realizar uma pesquisa sobre o Jogo dos Fósforos. Percebi que para que o computador ganhe, tem que retirar o nº de fósforos que são o resultado de 5-nºfósforos retirados pelo jogador na jogada anterior e que existem posições indesejáveis, sendo estas quando sobram 6, 11 e 16 fósforos, isto porque quando está resto 5 ou múltiplo de 5 (ou seja, uma unidade abaixo destes números indesejáveis), o computador pode retirar 4, o que faz com que consiga que sobre apenas um fósforo que terá de ser retirado pelo oponente. 

Quanto ao código, o jogador escolhe se quer ser ele a começar ou se prefere que seja o computador, escolhendo o modo 1 ou 2. Se for introduzido um modo diferente, a resposta é dada como inválida. Começa-se com 21 fósforos e quem tirar o último perde.

Quando o jogador é o primeiro a jogar (modo 1), deve escolher quantos fósforos deseja retirar (entre 1 e 4) para que depois o computador retire os fósforos resultantes da subtração do nº de fósforos retirados pelo utilizador a 5, e assim sucessivamente até que o nº de fósforos se esgote. A cada vez que alguém tira fósforos é mostrado o nº de fósforos retirados e quantos restam depois disso. 

Quando é escolhido o modo 2, o computador escolhe um nº aleatório entre 1 e 4 (através de um random.randint(1,4)) para retirar e logo em seguida o jogador retira também fósforos. Quando o jogador se enganar nas contas e o nº de fósforos restantes não for 6,11 ou 16, o computador retira 1 fósforo, o que faz com que o jogador fique numa posição vulnerável, ficando então com 6,11 ou 16 fósforos, o que faz com que o computador possa novamente retirar 5-nºfósforos retirados pelo jogador.
Assim, se o computador começar em segundo lugar ganha sempre, e se o jogador for segundo e se enganar nas contas, o computador também ganha. 
