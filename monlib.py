# Organizei o código em classes, pra ficar mais organizado. Agora, por exemplo, ao invés de chamar a função escrever() - de forma avulsa - iremos chamar Monarca.escrever(). Isto também permite compartilhar informações entre as funções.

class Monarca:
    def __init__(self, linha=0):
        self.linha = linha
        self.variaveis = {}
        self.operações = ['mais', 'menos', 'vezes', 'dividindo']
        self.keywords = ['variável', 'recebe', 'deletar', 'clonar', 'mostrar na tela', 'mais', 'menos', 'vezes', 'dividindo']
        pass

    # Função de erro. Basta passar a mensagem de erro como argumento que ele vai reconhecer a linha do erro sozinho.
    def erro(self, mensagem=''):
        print('\033[1;33m='*10, 'Monarca', '='*10)
        print(f'\033[1;31m * Erro na linha {self.linha + 1}. \033[0m' + mensagem)
        exit()

    def processar_variavel(self, dado):
        try:
            expressao = []
            trecho = ''
            if dado.strip() == '':
                self.erro('O valor da variável não pode ser vazio.') 
            ### Primeira etapa da função
            # Nessa etapa, o Monarca quebra o dado recebido em diferentes partes e as armazena na lista "expressao".
            # A ideia é identificar o que é string, o que é número, o que é variável, etc.
            # Por exemplo, um dado "5 mais 5" eventualmente iria ficar {'5', 'mais', '5'}. Seriam dois valores numéricos e o operador "mais".
            # Outro exemplo: Um dado ""Meu nome é " nome", supondo que "nome" seja uma variável de valor "Carlos", ficaria armazenado como {'"Meu nome é "', 'Carlos'}.
            # A cada loop, um trecho é lido, interpretado e armazenado na lista "expressao".
            # O trecho lido também é apagado da variável "dado", então o loop abaixo roda enquanto houver informação na variável.
            while dado != '':
                if dado[0] == "\"" or dado[0] == "\'": # Checa se a expressão começa com aspa, ou seja, se há uma string logo no início. Se sim, checa se há outra aspa e caso haja armazena o trecho e o apaga da variável dado.
                    c = dado.find(dado[0], 1) # Índice da próxima aspa do par.
                    if c != -1: # Ou seja, se existe outra aspa para completar o par, já que seria -1 se não encontrasse.
                        expressao.append(dado[0:c+1]) 
                        dado = dado[c+1:]
                        continue
                    else:   # Se não existe par, aponta erro
                        raise Exception                 
                else: # Em caso de não começar com aspa. Ou seja, poderia ser um número, uma variável, um operador etc.                   
                    if "\"" in dado or "\'" in dado:                # Esse if...else checa se em dado momento aparecerá uma string. Se não aparecer, o código só lê tudo. Se aparecer, lê até o momento da string.
                        aspaDupla = dado.find("\"")
                        aspaSimples = dado.find("\'")
                        c = aspaDupla if aspaSimples == -1 or (aspaDupla != -1 and aspaDupla < aspaSimples) else aspaSimples
                        trecho = dado[0:c]                        
                        dado = dado[c:]
                    else:                    
                        trecho = dado[0:]
                        dado = ''                    
                    for palavra in trecho.split(): # Leitura do trecho. Checa e substitui as variáveis, checa a validade dos números, etc                        
                        if palavra in self.variaveis.keys():                          
                            palavra = self.variaveis[palavra]
                        elif all(i in {"0","1","2","3","4","5","6","7","8","9",","} for i in palavra) and palavra.count(",") <= 1: # Se o trecho for apenas números e vírgula e, havendo vírgula, houver apenas uma.                    
                            palavra = palavra.replace(",",".")  # Converte vírgula para ponto para poder ser lido nas operações.
                        elif not palavra in self.operações: # Se não for variável nem número, e também não for nenhuma operação, dá erro.
                            raise Exception
                        expressao.append(palavra)                       
            # Ao final desse loop while, uma expressão "Oi, meu nome é " nome " e eu tenho " 23,5 mais 5,5 " anos", supondo que nome seja uma variável de valor "Carlos",
            # ficaria uma lista ['"Oi, meu nome é "', '"Carlos"', '" e eu tenho "', '23.5', 'mais', '5.5', '" anos"']

            # Segunda parte da função, a etapa das operações
            i = 0            
            while 'vezes' in expressao or 'dividindo' in expressao:                                      
                if expressao[i] == 'vezes' or expressao[i] == 'dividindo':
                    num1 = expressao[i - 1]
                    num2 = expressao[i + 1]
                    match expressao[i]:
                        case 'vezes':                        
                            resultado = float(num1) * float(num2)
                        case 'dividindo':
                            resultado = float(num1) / float(num2)
                    expressao[i+1] = str(resultado)                   
                    expressao.pop(i - 1)                    
                    expressao.pop(i - 1)                                        
                else:
                    i += 1 
            i = 0
            while 'mais' in expressao or 'menos' in expressao:                                      
                if expressao[i] == 'mais' or expressao[i] == 'menos':
                    num1 = expressao[i - 1]
                    num2 = expressao[i + 1]
                    match expressao[i]:
                        case 'mais':                        
                            resultado = float(num1) + float(num2)
                        case 'menos':
                            resultado = float(num1) - float(num2)                    
                    expressao[i+1] = str(resultado)                 
                    expressao.pop(i - 1)                    
                    expressao.pop(i - 1)                                        
                else:
                    i += 1 
            
            # Terceira etapa: tipagem e finalização. Nesse ponto, se a expressão não retornar uma lista com um único elemento, será tratada como uma string. 
            # Também será tratada como string se tiver um único elemento envolto em aspas.

            # Converte ponto para vírgula
            for i, palavra in enumerate(expressao):                
                if all(c in {"0","1","2","3","4","5","6","7","8","9","."} for c in palavra):
                    expressao[i] = expressao[i].replace(".",",")

            if len(expressao) > 1 or expressao[0][0] == "\"" or expressao[0][1] == "\'":
                expressao = "\"" + ''.join(expressao).replace("\"",'').replace("\'", '') + "\""
                return expressao
            else:
                i = expressao[0].find(".")              
                if i != -1 and expressao[0][i + 1] == 0:
                    return expressao[0][0:i]
                else:
                    return expressao[0]
        except Exception:
            self.erro('Dado, variável ou operação não reconhecido(a).')      
    # def converter_tipo(self, dado, tipo=''):
    #     try:
    #         if tipo == 'inteiro':
    #             return int(dado)
    #         elif tipo == 'real':
    #             return float(dado)
    #         elif tipo == 'booleano':
    #             return bool(dado)
    #         elif tipo == 'texto':
    #             return dado
    #         else:
    #             self.erro(f'O tipo \033[1m\033[3m{tipo}\033[0m especificado não existe.')
    #     except Exception:
    #             self.erro(f'Dado impróprio para a conversão para o tipo \033[1m\033[3m{tipo}\033[0m.')

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

    # Função para inicializar ou deletar variáveis
    def variavel(self, operacao='', nome='', var=None):
        if operacao == 'add':
            self.variaveis.update({nome : var})
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

    # função para clonar o valor e o tipo de uma variável para a outra
    def clonar_valor(self, var1, var2):
        if var1 in self.variaveis.keys() and var2 in self.variaveis.keys():
            self.variaveis[var2] = self.variaveis[var1]
            self.vartipos[var2] = self.vartipos[var1]
