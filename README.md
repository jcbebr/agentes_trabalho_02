## Kakuro 
Jogo de somas em que o objetivo é preencher todo o tabuleiro

https://www.kakuros.com/?s=3x3

## Kakuro Data Sets
Na pasta "1_kakuro\datasets" foram gerados 51 tabuleiros válidos para o jogo.
Os valores possíveis a serem inseridos são delimitados por 1.5 * tamanho do tabuleiro

## Kakuro Backtracking

O único argumento para execução é o nome do arquivo do dataset para rodar o algoritmo

Exemplo
`python backtracking.py 3_1.txt`

Executou somente até o tabuleiro 6x6

Melhorias possíveis:
    Estrutura de vizinhos. Atualmente um vizinho é gerado alterando apenas um número do tabuleiro.
    Poderia ser alterado para selecionar uma das combinações de soma das linha / colunas
    Validar vizinhos sem precisar alterar o tabuleiro. (Aplicações de restrição)
    

## Kakuro Local Bean Search

Exemplo
`python local_bean_search.py 3_1.txt 10 5 123`

Sendo:
3_1.txt = Nome do arquivo do dataset
10      = Número de feixes (k)
5       = Tempo limite (em segundos)
123     = Seed para decisões aleatórias

Nem sempre encontra o resultado completo.

Melhorias possíveis:
    Estrutura de vizinhos. Atualmente um vizinho é gerado alterando apenas um número do tabuleiro.
    Poderia ser alterado para selecionar uma das combinações de soma das linha / colunas

## Reversi
Os argumentos para execução e testes são os mesmos do projeto original, com a adicção dos seguintes:
-s   Seed para decisões aleatórias           - Por padrão : 125
-c   Camadas utilizadas pelo MinimaxPlayer   - Por padrão : 3

Exemplo:
`python server.py advsearch.minimaxplayer advsearch.randomplayer -d 5 -p 0 -s 126 -c 4`

Melhorias possíveis:
    Definir uma melhor regra para a utilidade, foi utilizada somente o número de peças da cor do jogador.
