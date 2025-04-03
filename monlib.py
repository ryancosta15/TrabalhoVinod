def escrever(linha):
    linha = linha.replace("escrever: ", "")
    print(linha)
#def variavel(var, linha): #func pra definir variaveis
#    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
#    var.update({linha[0]: linha[1]})
def variaveltipo(linha, var):
    nome = linha.split(' ')[1]
    tipo = linha.split(' ')[3][0:-1]
    dado = ' '.join(linha.split(' ')[4:])
    var.update({nome: [tipo, dado]})
