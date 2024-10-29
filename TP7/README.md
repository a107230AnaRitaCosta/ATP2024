# Relatório do tp7
## Data: 2024-10-23
## Autor: Ana Rita Costa - a107230

## Resumo:
O tpc7 consitiu na criação de uma aplicação que permite criar uma tabela meteorológica e consultar informações sobre a mesma.
É apresentado um menu ao utilizador e este terá de escolher qual a opção que deseja realizar:
    (1) Criar Tabela Meteorológica - são pedidas as informações que o utilizador deseja que estejam na tabela: data (dia, mês, ano), temperaturas mínima e máxima e precipitação. A aplicação cria uma lista com as informações dadas.
    (2) Consultar TEMPERATURA MÉDIA de cada dia - é feito o cálculo da temperatura média de cada dia e é apresentada ao utilizador.
    (3) Guardar tabela meteorológica num ficheiro - a tabela criada é guardada num ficheiro. Cada linha corresponde a uma data. Em cada linha, os elementos da data são separados por "-" e os restantes elementos são separados por "&".
    (4) Carrega tabela meteorológica de um ficheiro - a informação da tabela é carregada do ficheiro e novamente apresentada na forma de uma lista.
    (5) Consultar TEMPERATURA MÍNIMA mais baixa - é apresentada a menor temperatura registada no conjunto de dias.
    (6) Consultar AMPLITUDE TÉRMICA de cada dia - é feito o cálculo da diferença entre a temperatura máxima e a temperatura mínima de cada dia.
    (7) Consultar PRECIPITAÇÃO MÁXIMA e o seu dia - qual o dia e o valor da máxima precipitação registada.
    (8) Dias com precipitação superior a limite - é introduzido um limite de precipitação pelo utilizador e são mostrados os dias que tiverma uma precipitação superior a esse valor.
    (9) Nº de dias consecutivos de precipitação abaixo do limite - é introduzido um limite de precipitação pelo utilizador e é mostrado o nº de dias seguidos que tiveram menor precipitação.
    (10) Gráfico Temperatura Máxima e Mínima - é construído um gráfico que mostra as temperaturas máximas e mínimas de cada dia.
    (11) Gráfico pluviosidade - é construído um gráfico de barras que mostra a precipitação de cada dia
    (0) Sair da aplicação - a aplicação é encerrada.