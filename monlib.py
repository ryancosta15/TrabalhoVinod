# Organizei o código em classes, pra ficar mais organizado. Agora, por exemplo, ao invés de chamar a função escrever() - de forma avulsa - iremos chamar Monarca.escrever(). Isto também permite compartilhar informações entre as funções.

class Monarca:
    def __init__(self, linha=0):
        self.linha = linha
        self.variaveis = {}
        pass

    # Função de erro. Basta passar a mensagem de erro como argumento, que ele vai reconhecer a linha do erro sozinho.
    def erro(self, mensagem=''):
        print('\033[1;33m='*10, 'Monarca', '='*10)
        print(f'\033[1;31m * Erro na linha {self.linha + 1}. \033[0m' + mensagem)
        exit()
    
    def converter_tipo(self, dado, tipo=''):
        try:
            if tipo == 'inteiro':
                return int(dado)
            elif tipo == 'real':
                return float(dado)
            elif tipo == 'booleano':
                return bool(dado)
            elif tipo == 'texto':
                return dado
            else:
                self.erro(f'O tipo \033[1m\033[3m{tipo}\033[0m especificado não existe.')
        except Exception:
                self.erro(f'Dado impróprio para a conversão para o tipo \033[1m\033[3m{tipo}\033[0m.')

    # Função usada pelo interpretador para entender automaticamente de que tipo são os dados escritos no código do usuário
    def tipo_de_dado(self, dado=''):
        # Verifica se é um inteiro
        if dado.isnumeric():
            return 'inteiro'
        # Verifica se é um número real.
        # Primeiro, se tiver um "." no dado, separa os dois lados do . em uma lista e verifica se ambos os lados são numéricos e não possuem nenhum caractere além de números.
        # Desta forma, se o dado for "12.5" ele se tornará "[12, 5]" para facilitar a verificação, afim de evitar erros como tentar converter "abc.6" em um número real, o que seria absolutamente incorreto.
        elif '.' in dado and (dado.split('.')[0].isnumeric() and dado.split('.')[1].isnumeric()):
            return 'real'
        # Aqui ficará a verificação que determinará se é uma expressão de lógica booleana: em desenvolvimento
        # Caso o dado não seja de nenhum dos tipos anteriores, o interpretador o assume como texto
        else:
            return 'texto' 

    # Função análoga ao print
    def escrever(self, texto):
        texto = texto.split(' ')
        for c in range(0, len(texto)):
            palavra = texto[c]
            if palavra[0] == '\\' and palavra[1:] in self.variaveis.keys():
                texto[c] = str(self.variaveis[palavra[1:]])
        texto = ' '.join(texto).replace('\\\\', '\\').replace('\n', '')
        print(texto)

    # Versão anterior preservada caso mudemos de ideia
    # def escrever(self, texto):
    #     texto = texto.split(' ')
    #     for c in range(0, len(texto)):
    #         palavra = texto[c]
    #         if palavra in self.variaveis.keys():
    #             texto[c] = str(self.variaveis[palavra])
    #     texto = texto[texto.index('tela:')+1:]
    #     texto = ' '.join(texto).replace('\\', '').replace('\n', '')
    #     print(texto)

    

    # Função para inicializar ou deletar variáveis
    def variavel(self, operacao='', nome='', dado=None):
        if operacao == 'add':
            self.variaveis.update({nome : dado})
        elif operacao == 'del':
            if nome in self.variaveis.keys():
                self.variaveis.pop(nome)
            else:
                self.erro(f'Variável \033[1m\033[3m"{nome}"\033[0m não existente.')

    # Função de operações aritméticas. Analisa primeiramente os operadores de multiplicação e divisão, depois os de adição e subtração.
    def aritmetica(self, expressao):
        total = 0
        
        # Continua rodando até que todos os operadores de multiplicação e divisão tenham sido substituídos pelos resultados numéricos de suas operações, para que só então as outras operações possam ser executadas.
        while 'vezes' in expressao or 'dividindo' in expressao:
            try:
                if 'vezes' in expressao:
                    n1 = expressao[expressao.index('vezes') - 1]
                    n2 = expressao[expressao.index('vezes') + 1]
                    resultado = float(n1)*float(n2)
                    # Substitui a operação pelo resultado.
                    expressao[expressao.index('vezes')+1] = resultado
                    expressao.pop(expressao.index('vezes'))
                    expressao.pop(expressao.index(n1))
                    total = resultado
                elif 'dividindo' in expressao:
                    n1 = expressao[expressao.index('dividindo') - 1]
                    n2 = expressao[expressao.index('dividindo') + 1]
                    resultado = float(n1)/float(n2)
                    # Substitui a operação pelo resultado
                    expressao[expressao.index('dividindo')+1] = resultado
                    expressao.pop(expressao.index('dividindo'))
                    expressao.pop(expressao.index(n1))
                    total = resultado
    
            except Exception:
                self.erro(f'Expressão aritmética mal formulada.')

        try:
            for c in range(0, len(expressao)):
                if expressao[c] == 'mais':
                    if c == 1:
                        total = float(expressao[c-1]) + float(expressao[c+1])
                        c += 1
                    else:
                        total += float(expressao[c+1])

                elif expressao[c] == 'menos':
                    if c == 1: 
                        total = float(expressao[c-1]) - float(expressao[c+1])
                        c += 1
                    else:
                        total -= float(expressao[c+1])
                                        
            return total

        except Exception:
            self.erro(f'Expressão aritmética mal formulada.')
