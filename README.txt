Read Me do analisador Léxico e Sintático de Lógica Proposicional, passo a passo para a execução dos exemplos:

Este projeto implementa um analisador de expressões de lógica proposicional, utilizando:

- Análise léxica com Máquina de Estados Finitos (MEF)
- Análise sintática com parser LL(1)

-----------------------------

Formato da Entrada

O programa lê um arquivo .txt com o seguinte formato:

1. A primeira linha contém um número inteiro N, indicando quantas expressões devem ser analisadas.
2. As N linhas seguintes contêm as expressões lógicas a serem validadas.

Os 3 exemplos de conteúdo para testes estão no repositório junto ao código.

-----------------------------
Como Executar

No final do código Python, há uma configuração chamada "modo" que permite escolher de onde o arquivo será lido.

Altere o modo para 'url' para usar exemplos vindos de links do GitHub e para 'local' para exemplos vindos de um arquivo local.
 

1. Executar com arquivo local:

modo = 'local'
caminho_local = "C:\Users\SeuUsuario\Downloads\exemplo1.txt"

Atenção: use r"..." junto com a String do caminho do arquivo para evitar erros com as barras invertidas ou use \\ caso não use o r a frente.  

Se quiser testar com um exemplo seu por meio de um arquivo local é necessário apenas trocar o caminho do arquivo pelo seu e colocar o modo = 'local'.


2. Executar com arquivo hospedado no GitHub:

modo = 'url'
url = "https://raw.githubusercontent.com/SeuUsuario/SeuRepositorio/main/exemplo1.txt"

No código já estão os 3 exemplos criados por nós, para alternar entre os 3 exemplos de teste é só comentar o próximo e tirar o comentário do anterior.

Se quiser testar com um exemplo seu por meio de um link do arquivo no GitHub é necessário apenas trocar o link de um de nossos exemplos pelo seu e colocar o modo = 'url'.

-----------------------------
Saída Esperada

Para cada expressão, o programa imprime no terminal:

valida
invalida
valida
...

-----------------------------
Autores

Henrique Zan Grande  
João Gabriel Pitol  
Lucas Braga Schuck  
Rafael Vargas Serenato

-----------------------------
Observações

- O código foi testado com exemplos válidos e inválidos.
- Recomendado rodar via Google Colab (onde foi desenvolvido) ou Python 3.9+ localmente.
- Caso opte por usar URLs do GitHub para carregar os exemplos rodando localmente, é necessário instalar a biblioteca requests: pip install requests
