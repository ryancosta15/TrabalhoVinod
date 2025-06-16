# Controle do tempo de execução do programa. No final do código tem um trecho que termina de calcular o tempo e imprime o resultado.
from time import time
tempo_inicial = time()

from argparse import ArgumentParser
from monlib import Monarca

# Define o argumento "-s" ou "--script" para usuários de linha de comando apontarem onde está o script que desejam executar.
argumentos = ArgumentParser(usage='monarca.py -s script.mc')
argumentos.add_argument('-s', '--script', required=True)
argumentos = argumentos.parse_args()

# Cria uma instância da classe geral Monarca(), onde estão todas as funções.
monarca = Monarca()

# Verifica se o arquivo indicado pelo usuário existe e, se sim, tenta abrí-lo e guardá-lo na variável script. Se não, dá um erro na tela.
try:
    script = open(argumentos.script, encoding='utf-8').readlines()
except Exception:
    monarca.erro(f'Arquivo {argumentos.script} não encontrado.')

# A variável c é o índice da linha, e a variável linha contém o texto da linha em si. A cada laço é interpretada uma linha do script.
for c, linha in zip(range(0, len(script)), script):     
    linha = linha.replace('\n', '') # Impede que a quebra de linha atrapalhe a leitura dos dados 
    if '::info' in linha:   # Ignora comentários
        índice = linha.find('::info')
        linha = linha[:índice]   
    dlinha = linha.split(' ') # Para termos acesso tanto a trechos inteiros da linha de texto quanto a palavras específicas em posições específicas, criamos duas variáveis, linha e dlinha.  
    if linha.strip() == '': # Checa se é uma linha vazia. Se sim, apenas pula para a próxima.
        continue    
    monarca.linha = c # Informa o índice da linha para o Monarca, a fim de apontar onde ocorreu algum eventual erro. 
    # Verifica se o usuário quer iniciar uma variável
    if len(dlinha) >= 3 and dlinha[0] == 'variável' and dlinha[2] == 'recebe': 
        # Impede nome vazio para variáveis
        if dlinha[1] == '':
            monarca.erro('O nome da variável não pode ser nulo.')
        elif dlinha[1] in monarca.keywords:
            monarca.erro(f"\"{dlinha[1]}\" é uma palavra reservada no Monarca.")               
        var = monarca.processar_variavel(dado=' '.join(dlinha[3:])) # Envia tudo o que vier depois de "recebe" para ser processado pela função.
        monarca.variavel(operacao='add', nome=dlinha[1], var=var)   
    # Verifica se o usuário quer deletar uma variável
    elif dlinha[0] == 'deletar' and dlinha[1] == 'variável':
        monarca.variavel('del', dlinha[2])
    # Verifica se o usuário quer clonar o valor de uma variável
    elif dlinha[0] == 'clonar' and dlinha[1] == 'variável':
        monarca.clonar_valor(dlinha[2], dlinha[4])      
     # Verifica se o usuário quer mostrar uma mensagem na tela
    elif linha[:17] == 'mostrar na tela: ' and linha[17:] != '':
        monarca.escrever(texto=linha[17:])     
    # Entrega um erro caso o usuário não digite nenhum comando conhecido pelo Monarca. Será ignorado caso seja uma linha vazia. 
    else:
        monarca.erro(f'Sintaxe inválida. Consulte a documentação.')   

tempo_final = time()
print(f'\n\033[1;33mTempo de execução: {tempo_final-tempo_inicial:.4f} segundos.\033[m')

##### LEMBRETES
# Checar como se comportam variáveis com nomes ou dados vazios


