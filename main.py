from argparse import ArgumentParser
from monlib import Monarca

# Define o argumento "-s" ou "--script" para usuários de linha de comando apontarem onde está o script que desejam executar.
argumentos = ArgumentParser(usage='monarca.py -s script.mc')
argumentos.add_argument('-s', '--script', required=True)
argumentos = argumentos.parse_args()

# Cria uma instância da classe geral Monarca() (onde estão todas as funções)
monarca = Monarca()

#Verifica se o arquivo indicado pelo usuário existe, e se sim, tenta abrir ele e por na variável script. Se não, dá um erro na tela.
try:
    script = open(argumentos.script, encoding='utf-8').readlines()
except Exception:
    monarca.erro(f'Arquivo {argumentos.script} não encontrado.')

# A variável c é o index da linha, e a variável linha contém o texto da linha em si.
for c, linha in zip(range(0, len(script)), script):
    monarca.linha = c # Informa o index da linha para o monarca, afim de apontar em qual linha ocorreu algum eventual erro.
    # Verifica se o usuário quer iniciar uma variável
    if linha.split(' ')[0] == 'variável':
        linha = linha.split(' ')
        dado = monarca.converter_tipo(''.join(linha[4:]), linha[3])
        monarca.variavel(operacao='add', nome=linha[1], dado=dado)
    # Verifica se o usuário quer deletar uma variável
    elif linha.split(' ')[0] == 'deletar':
        linha = linha.split(' ')
        monarca.variavel('del', linha[2])
    elif linha.split(' ')[0] == 'mostrar':
        monarca.escrever(linha)
    # Vou adicionar mais depois, implementar as outras funções.
    #testar delete que ta na documentação
