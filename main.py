import monlib

nlinha = 0 #esse nlinha é pra debug
var = {}
script = open("codteste.txt").readlines()
for linha in script:
    nlinha += 1
    print(f"DEBUG - linha encontrada, buscando comandos na linha {nlinha}")
    if "escrever: " in linha:
        print("DEBUG - 'escrever' encontrado, dando replace()")
        monlib.escrever(linha)
    elif "variavel " in linha:
        print("DEBUG - 'variavel' encontrada")
        monlib.variavel(linha)
print(float(var["a"]) + float(var["b"]))



