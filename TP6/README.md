# Relatório do tp6
## Data: 2024-10-16
## Autor: Ana Rita Costa - a107230

## Resumo:
O tpc6 consistiu na criação de uma aplicação que coloca no monitor o seguinte menu de operações:
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 8: Guardar a turma em ficheiro;
    - 9: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação

Quando a opção 0 é escolhida, a aplicação é encerrada e é mostrada a turma ao utilizador.

A cada opção que é escolhida é mostrado o menu e se for escolhida uma opção que não existe, a opção introduzida é dada como inválida e é pedido para que o utilizador introduza novamente uma opção válida.

Para cada opção defini uma função que executa aquilo que o utilizador pediu:
    -Para a opção 1 (criar uma turma), é perguntado ao utilizador por quantos alunos a turma vai ser constituída. Depois disso, o programa vai perguntar ao utilizador as informações sobre cada aluno para que possam ser introduzidas na turma (nome,id e notas (notaTPC, notaProj e notaTeste)).
    -Para a opção 2 (inserir um aluno na turma), o programa verifica se o aluno que o utilizador quer inserir já se encontra na turma, através de uma outra função que criei para auxiliar este processo (função idexistealuno), que identifica o aluno através do seu id, uma vez que este é único para cada aluno, enquanto que pode haver pessoas com o mesmo nome. Se esse aluno não estiver na turma, as suas informações são então adicionadas à lista.  
    -Para a opção 3 (listar a turma), aparece no ecrã as informações de todos os alunos.
    -Para a opção 4 (consultar um aluno por id), se o id introduzido não corresponder a nenhum aluno da turma é dito isso ao utilizador, se o id realmente corresponder a um aluno, são mostradas as informações desse mesmo aluno no monitor.
    -Para a opção 5 (guardar a turma em ficheiro), a função criada permite a criação de um ficheiro no qual vão ser guardadas as informações dos alunos, ficando cada aluno numa linha e, dentro de cada linha, cada tipo de informação do aluno é separada por um carater.
    -Para a opção 6 (carregar uma turma dum ficheiro), é recuperada a informação contida no ficheiro e é novamente mostrada ao utilizador. Isto acontece porque a função faz com que se volte a juntar a informação toda, usando mais uma vez os diferentes carateres que identificam cada informação do aluno.

Utilizei a aplicação para criar uma turma de 5 alunos, que ficou guardada no ficheiro de nome turma_f.