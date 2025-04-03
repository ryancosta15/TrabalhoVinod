import monlib
nlinha = 0 #esse nlinha é pra debug
#nvar = {} #nome das variaveis
#tvar = {} #tipo das variaveis (int, float, str e bool
#dvar = {} #dado das variaveis (texto/valor)
var = {}
script = open("teste monarca.txt").readlines()
for linha in script:
    nlinha += 1
    print(f"DEBUG - linha encontrada, buscando comandos na linha {nlinha}")
    if "escrever: " in linha:
        print("DEBUG - 'escrever' encontrado, dando replace()")
        monlib.escrever(linha)
    elif "variavel " in linha:
        print("DEBUG - 'variavel' encontrada")
        monlib.variaveltipo(linha, var)
#print(float(var["b"])+float(var["c"]))
# #print de debug pra ver se tava salvando as variáveis certinho


