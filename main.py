from time import time
tempo_inicial = time()

from argparse import ArgumentParser
from monlib import Monarca


# Define o argumento "-s" ou "--script" para usuários de linha de comando apontarem onde está o script que desejam executar.
argumentos = ArgumentParser(usage='monarca.py -s script.mc')
argumentos.add_argument('-s', '--script', required=True)
argumentos = argumentos.parse_args()

# Cria uma instância da classe geral Monarca() (onde estão todas as funções)
monarca = Monarca()

# Verifica se o arquivo indicado pelo usuário existe, e se sim, tenta abrir ele e por na variável script. Se não, dá um erro na tela.
try:
    script = open(argumentos.script, encoding='utf-8').readlines()
except Exception:
    monarca.erro(f'Arquivo {argumentos.script} não encontrado.')

# A variável c é o index da linha, e a variável linha contém o texto da linha em si. A cada laço é interpretada uma linha do script.
for c, linha in zip(range(0, len(script)), script):
    linha = linha.replace('\n', '') # Impede que a quebra de linha atrapalhe a leitura dos dados
    dlinha = linha.split(' ') # Para termos acesso tanto a linha inteira quanto a linha dividida.
    if linha == '\n' or linha.strip() == '' or dlinha[0] == '::info': # Checa se a linha é um comentário ou está vazia.
        continue                                                      # Se sim, a ignora e passa para a próxima.
    monarca.linha = c # Informa o index da linha para o monarca, a fim de apontar em qual linha ocorreu algum eventual erro.  
    # Verifica se o usuário quer iniciar uma variável
    if dlinha[0] == 'variável' and dlinha[2] == 'recebe':
         # Impede nome vazio para variáveis
        if dlinha[1] == '':
            monarca.erro('O nome da variável não pode ser nulo.')
        if any(i in dlinha[4:] for i in monarca.operações):
            dado = monarca.aritmetica(dlinha[4:])
            dado = monarca.converter_tipo(dado, dlinha[3])
        else:
            dado = monarca.converter_tipo(' '.join(dlinha[4:]), dlinha[3])
        monarca.variavel(operacao='add', nome=dlinha[1], tipo=dlinha[3], dado=dado)
    # Verifica se o usuário quer deletar uma variável
    elif dlinha[0] == 'deletar' and dlinha[1] == 'variável':
        monarca.variavel('del', dlinha[2])
    # Verifica se o usuário quer clonar o valor de uma variável
    elif dlinha[0] == 'clonar' and dlinha[1] == 'variável':
        monarca.clonar_valor(dlinha[2], dlinha[4])
    # Verifica se o usuário quer mostrar uma mensagem na tela
    elif linha[:17] == 'mostrar na tela: ' and linha[17:] != '':
        monarca.escrever(texto=linha[17:])
    elif dlinha[0] == 'entrada':
        if dlinha[2:] == '':
            inputmsg = 'vazio'
        else:
            inputmsg = ' '.join(dlinha[3:])
        nome = dlinha[1]
        monarca.input(inputmsg, nome)
    # Entrega um erro caso o usuário não digite nenhum comando conhecido pelo Monarca. Será ignorado caso seja uma linha vazia. 
    else:
        monarca.erro(f'Sintaxe inválida. Consulte a documentação.')
    # Vou adicionar mais depois, implementar as outras funções.
    #testar delete que ta na documentação

tempo_final = time()
print(f'\n\033[1;33mTempo de execução: {tempo_final-tempo_inicial:.4f} segundos.\033[m')
