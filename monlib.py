def escrever(linha):
    linha = linha.replace("escrever: ", "")
    print(linha)
def variavel(var):
    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
    var.update({linha[0]: linha[1]})
def somar(a, b):
    print(float(a) + float(b))