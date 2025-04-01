import monlib
nlinha = 0 #esse nlinha é pra debug
var = {} #dicionário pras variaveis
script = open("codteste.txt").readlines()
for linha in script:
    nlinha += 1
    print(f"DEBUG - linha encontrada, buscando comandos na linha {nlinha}")
    if "escrever: " in linha:
        print("DEBUG - 'escrever' encontrado, dando replace()")
        monlib.escrever(linha)
    elif "variavel " in linha:
        print("DEBUG - 'variavel' encontrada")
        monlib.variavel(var, linha)
print(float(var["b"])+float(var["c"])) #print de debug pra ver se tava salvando as variáveis certinho


