## Kakuro 
Jogo de somas em que o objetivo é preencher todo o tabuleiro

## Kakuro Data Sets
Na pasta "1_kakuro\datasets" foram gerados 51 tabuleiros válidos para o jogo.
Os valores possíveis a serem inseridos são delimitados por 1.5 * tamanho do tabuleiro

## Kakuro Backtracking

O único argumento para execução é o nome do arquivo do dataset para rodar o algoritmo

Exemplo
`python backtracking.py 3_1.txt`

Melhorias possíveis:
    Estrutura de vizinhos. Atualmente um vizinho é gerado alterando apenas um número do tabuleiro.
    Poderia ser alterado para selecionar uma das combinações de soma das linha / colunas


## Kakuro Local Bean Search

Exemplo
`python local_bean_search.py 3_1.txt 10 5 123`

Sendo:
3_1.txt = Nome do arquivo do dataset
10      = Número de feixes (k)
5       = Tempo limite (em segundos)
123     = Seed para decisões aleatórias

Melhorias possíveis:
    Estrutura de vizinhos. Atualmente um vizinho é gerado alterando apenas um número do tabuleiro.
    Poderia ser alterado para selecionar uma das combinações de soma das linha / colunas

## Reversi
Os argumentos para execução e testes são os mesmos do projeto original, com a adicção dos seguintes:
-s   Seed para decisões aleatórias           - Por padrão : 125
-c   Camadas utilizadas pelo MinimaxPlayer   - Por padrão : 3

Exemplo:
`python server.py advsearch.minimaxplayer advsearch.randomplayer -d 2 -p 0 -s 126 -c 4`
