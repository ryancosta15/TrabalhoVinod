def escrever(linha):
    linha = linha.replace("escrever: ", "")
    print(linha)
def variavel(var, linha): #func pra definir variaveis
    linha = linha.replace("variavel ", "", ).replace(":", "").split(" ")
    var.update({linha[0]: linha[1]})
"""def somar(a, b):
    print(float(var["a"])+float(var["b"]))"""
#essa func de soma ta hardcoded pra 2 argumentos só, eu vi no google que posso usar *args pra definir
#mais de um, porem eu nao faço a menor ideia de como fazer o print() tambem usar o *args, isso aí
#eu deixo com vcs

#depois de sofrer tanto com a variavel() eu nao quero tocar nisso aqui tao cedo