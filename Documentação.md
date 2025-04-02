# Sintaxe Base

## Tipos Primitivos de Dados

Os tipos primitivos de dados presentas na linguagem Monarca podem ser listados em:

* **Inteiro**: Representa qualquer número no conjunto dos números inteiros. Passível de sofrer operações aritméticas.
* **Real**: Representa qualquer número no conjunto dos números reais. Passível de sofrer operações aritméticas.
* **Texto**: Representa qualquer caractere visual dentro do padrão UTF-8. Não está passível de sofrer operações aritméticas.
* **Lógico**: Representa operações lógicas ou seus resultados, que podem ser Verdadeiro ou Falso.

## Inicializar Variável

Para inicializar uma variável, basta seguir a seguinte sintaxe, inserindo (de acordo com a necessidade) o nome da mesma e seu valor:

```
variável [nome da variável] recebe [tipo primitivo] [dado]
```

Em uma aplicação real, esta sintaxe se pareceria com o seguinte exemplo:

```
variável idade recebe inteiro 30
variável nome recebe texto Monteiro
variável altura recebe real 1.60
variável gosta_de_paçoca? recebe lógico Verdadeiro
```

Nomes de variáveis não podem ter espaços, embora possam conter caracteres especiais.

# Funções Básicas

## mostrar na tela:

A função "***mostrar na tela:***"  só possui 1 parâmetro: o conteúdo a ser exibido. Os dados a serem exibidos na tela devem estar a 1 caractere de espaço (" ") de distância após o caractere de dois pontos ( : ). Exemplo:

```
mostrar na tela: "Olá Mundo em Monarca!"

# Saída:
# Olá Mundo em Monarca!
```

Esta função também pode ser usada referenciando-se uma variável no campo dos dados:

```
variável nome recebe texto Maria
mostar na tela: nome

# Saída:
# Maria
```

Além disto, é possível exibir texto direto e conteúdo de variável ao mesmo tempo:

```
variável meu_nome recebe texto Paulo
mostrar na tela: Olá, meu nome é meu_nome!

# Saída:
# Olá, meu nome é Paulo!
```

# Questionamentos previstos:

* > ***E se o usuário quiser usar uma palavra reservada da linguagem - como "variável" - em um texto sem que seja tratada como um comando?***

  ​	Por padrão, todos os comandos e palavras necessárias para o funcionamento de comandos são reservadas (incluindo nomes de variáveis) e não podem ser usadas em outro contexto, a não ser que sejam escritas com o prefixo " \ ". Por exemplo:

  ```
  variável nome recebe texto Alan
  mostrar na tela: A \variável \nome foi inicializada.
  
  # Saída:
  # A variável nome foi inicializada.
  ```

  Desta forma, as palavras "variável" e "nome" puderam ser utilizadas como texto sem serem interpretadas como comandos.
