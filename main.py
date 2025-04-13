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
    monarca.linha = c # Informa o index da linha para o monarca, a fim de apontar em qual linha ocorreu algum eventual erro. 
    dlinha = linha.split(' ') # Para termos tanto a linha inteira quanto a linha dividida.
    # Verifica se o usuário quer iniciar uma variável
    if dlinha[0] == 'variável' and dlinha[2] == 'recebe' and len(dlinha) >= 4:
        dado = monarca.converter_tipo(' '.join(dlinha[4:]), dlinha[3])
        monarca.variavel(operacao='add', nome=dlinha[1], dado=dado)
    # Verifica se o usuário quer deletar uma variável
    elif dlinha[0] == 'deletar':
        monarca.variavel('del', dlinha[2])
    # Verifica se o usuário quer mostrar uma mensagem na tela
    elif dlinha[0] == 'mostrar':
        monarca.escrever(linha)    
    # Entrega um erro caso o usuário não digite nenhum comando conhecido pelo Monarca. Será ignorado caso seja uma linha vazia. 
    elif linha != '\n':
        monarca.erro('Comando não identificado.')
    # Vou adicionar mais depois, implementar as outras funções.
    #testar delete que ta na documentação
