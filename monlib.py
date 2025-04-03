def escrever(linha):
    linha = linha.replace("escrever: ", "")
    print(linha)
def variavel(var, linha): #func pra definir variaveis
    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
    var.update({linha[0]: linha[1]})
def variaveltipo(linha, var):
    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
    linh = linha.pop(1)  # se eu escrever "linha" o comando da um erro, se eu manter "linh" ele funciona. computadores me confudem muito
    var.update({linha[0]: linha[1], linha[2]:0,})