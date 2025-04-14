from os import path
#Henrique Zan Grande, João Gabriel Pitol, Lucas Braga Schuck, Rafael Vargas Serenato


import requests
# --------- ANÁLISE LÉXICA COM MEF ---------

def lexer_mef(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue

        if expr[i] == '(':
            tokens.append(('ABREPAREN', '('))
            i += 1
        elif expr[i] == ')':
            tokens.append(('FECHAPAREN', ')'))
            i += 1
        elif expr[i:].startswith('\\leftrightarrow'):
            tokens.append(('OPBINARIO', '\\leftrightarrow'))
            i += len('\\leftrightarrow')
        elif expr[i:].startswith('\\rightarrow'):
            tokens.append(('OPBINARIO', '\\rightarrow'))
            i += len('\\rightarrow')
        elif expr[i:].startswith('\\wedge'):
            tokens.append(('OPBINARIO', '\\wedge'))
            i += len('\\wedge')
        elif expr[i:].startswith('\\vee'):
            tokens.append(('OPBINARIO', '\\vee'))
            i += len('\\vee')
        elif expr[i:].startswith('\\neg'):
            tokens.append(('OPUNARIO', '\\neg'))
            i += len('\\neg')
        elif expr[i:].startswith('true'):
            tokens.append(('CONSTANTE', 'true'))
            i += len('true')
        elif expr[i:].startswith('false'):
            tokens.append(('CONSTANTE', 'false'))
            i += len('false')
        elif expr[i].isdigit():
            lexema = expr[i]
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i].islower()):
                lexema += expr[i]
                i += 1
            tokens.append(('PROPOSICAO', lexema))
        else:
            return None  # erro léxico
    return tokens



# --------- PARSER LL(1) ---------

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def lookahead(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index][0]
        return None

    def eat(self, token_type):
        if self.lookahead() == token_type:
            self.index += 1
        else:
            raise SyntaxError(f"Esperado {token_type}, encontrado {self.lookahead()}")

    def parse_formula(self):
        la = self.lookahead()

        if la == 'CONSTANTE':
            self.eat('CONSTANTE')

        elif la == 'PROPOSICAO':
            self.eat('PROPOSICAO')

        elif la == 'ABREPAREN':
            self.eat('ABREPAREN')
            operador = self.lookahead()

            if operador == 'OPUNARIO':
                self.eat('OPUNARIO')
                self.parse_formula()
                self.eat('FECHAPAREN')

            elif operador == 'OPBINARIO':
                self.eat('OPBINARIO')
                self.parse_formula()
                self.parse_formula()
                self.eat('FECHAPAREN')

            else:
                raise SyntaxError(f"Operador inválido: {operador}")

        else:
            raise SyntaxError(f"Símbolo inesperado: {la}")

    def parse(self):
        self.parse_formula()
        if self.index != len(self.tokens):
            raise SyntaxError("Tokens restantes não processados")
        return True

# --------- VALIDAÇÃO ---------

def validar_expressao(expr):
    tokens = lexer_mef(expr)
    if not tokens:
        return False
    try:
        parser = Parser(tokens)
        return parser.parse()
    except:
        return False

# --------- LEITURA DO ARQUIVO ---------

def processar_conteudo(conteudo):
    linhas = conteudo.strip().split('\n')
    n = int(linhas[0])
    expressoes = linhas[1:n+1]
    for expr in expressoes:
        print('valida' if validar_expressao(expr.strip()) else 'invalida')

# --------- EXECUÇÃO ---------
#Mude o modo para url ou local conforme o necessario.

modo = 'url'  # ou 'local'

#Passe o caminho do arquivo usando / entre as pastas.
caminho_local = "C:/Users/lucas/Downloads/exemplo1.txt"  # Caminho no computador/Colab

#Para testar os 3 exemplos, apenas troque o link comentado
url = "https://raw.githubusercontent.com/Lucasbschuck/ArquivosParser/main/exemplo1.txt"
#url = "https://raw.githubusercontent.com/Lucasbschuck/ArquivosParser/main/exemplo2.txt"
#url = "https://raw.githubusercontent.com/Lucasbschuck/ArquivosParser/main/exemplo3.txt"

if modo == 'url':
    response = requests.get(url)
    if response.ok:
        processar_conteudo(response.text)
    else:
        print("Erro ao baixar arquivo:", response.status_code)
elif modo == 'local':
    try:
        with open(caminho_local, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            processar_conteudo(conteudo)
    except Exception as e:
        print("Erro ao ler arquivo local:", e)
