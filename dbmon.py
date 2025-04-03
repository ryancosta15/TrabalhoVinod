def escrever(linha, nlinha):
    print(f"DEBUG - 'escrever' econtrado, executando .replace() na linha {nlinha}")
    linha = linha.replace("escrever: ", "")
    print(linha)
def variaveltipo(linha, var, nlinha):
    print(f"DEBUG - 'variavel' encontrado na linha {nlinha}, separando informações em listas")
    nome = linha.split(' ')[1]
    tipo = linha.split(' ')[3][0:-1]
    dado = ' '.join(linha.split(' ')[4:])
    print(f"DEBUG - informações separadas, atualizando o dicionário com a info")
    var.update({nome: [tipo, dado]})


#                   não apague!
#    print(f"DEBUG - 'variavel' encontrado, executando .replace() e .split() na linha {nlinha}")
#    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
#    print(f"DEBUG - .replace() e .split() executados com sucesso, removendo 'recebe' da linha {nlinha}")
#    linh = linha.pop(1)  # se eu escrever "linha" o comando da um erro, se eu manter "linh" ele funciona. computadores me confudem muito
#    print(f"DEBUG - 'recebe' removido, adicionando nome, tipo, e dados da variável encontrada na linha {nlinha} ao dicionário")
#    var.update({linha[0]: linha[1], linha[2]:0,})