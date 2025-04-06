# Organizei o código em classes, pra ficar mais organizado. Agora, por exemplo, ao invés de chamar a função escrever() - de forma avulsa - iremos chamar Monarca.escrever(). Isto também permite compartilhar informações entre as funções.

class Monarca:
    def __init__(self, linha=0):
        self.linha = linha
        self.variaveis = {}
        pass

    # Função de erro. Basta passar a mensagem de erro como argumento, que ele vai reconhecer a linha do erro sozinho.
    def erro(self, mensagem=''):
        print('='*10, 'Monarca', '='*10)
        print(f'Erro na linha {self.linha}. ' + mensagem)
    
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
                self.erro(f'O tipo {tipo} especificado não existe.')
        except Exception:
                self.erro(f'Dado impróprio para a conversão para o tipo {tipo}.')

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
            if palavra in self.variaveis.keys():
                texto[c] = str(self.variaveis[palavra])
        texto = texto[texto.index('tela:')+1:]
        texto = ' '.join(texto).replace('\\', '').replace('\n', '')
        print(texto)

    # Função para inicializar ou deletar variáveis
    def variavel(self, operacao='', nome='', dado=None):
        if operacao == 'add':
            self.variaveis.update({nome : dado})
        elif operacao == 'del':
            if nome in self.variaveis.keys():
                self.variaveis.pop(nome)
            else:
                self.erro(f'Variável "{nome}" não existente.')

    # Função de somar, pega qualquer argumento dado e soma todos. Ainda não implementado.
    def somar(self, numeros):
        numeros = numeros.split(' + ')
        total = 0
        for n in numeros:
            try:
                total += int(n)
            except ValueError:
                self.erro(f'Tipo inválido para soma: {self.tipo_de_dado(n)}')
        return total
