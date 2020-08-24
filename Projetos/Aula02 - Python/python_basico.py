# -*- coding: utf-8 -*-
"""Aula02 - Python básico.ipynb
# Programação Python Básico 

## Variáveis

Uma variável é um nome que se refere a um valor. As variáveis são criadas assim que um valor é atribuído à elas. Em Python, as variáveis não estão amarradas à um único tipo de dados, e assim podem receber qualquer valor.
"""

x = 10 
print(x)

x = 'banana'
print(x)

"""## Tipos de dados 

O tipo de uma variável é definido a partir do valor atribuído à ela. A função  `type()` retorna o tipo do valor referenciado pela variável.

Os tipos básicos da linguagem são:

- `int`: valores inteiros
- `float`: valores reais em ponto flutuante
- `str`: cadeias de caracteres
- `bool`: valores booleanos (`True` ou `False`)
- `tupla`: tupla imutável de valores
- `list`: lista mutável de valores
- `dict`: vetor associativo
"""

x = 10 
print(type(x))

x = 10.0 
print(type(x))

x = '10' 
print(type(x))

x = "10" 
print(type(x))

x = 'Isso é uma frase'
print(type(x))

x = True
print(type(x))

x = (1, 2, 3, 4, 'jaca', False)
print(x)

x = [1, 2, 3, 4, 'jaca', False]
print(type(x))

x = {
    'nome': 'Homer Simpson',
    'idade': 40,
    'salario': 3_000.00,
}

print(type(x))

"""### Representação de números inteiros"""

# Representação em hexadecimal
x = 0xCAFE
print(x)

# Representação em binário
x = 0b0000_0100_0011 # binário
print(x)

"""### Conversão entre tipos numéricos"""

x = 10.0
y = 20

z = int(x)
print(x, type(x))
print(z, type(z))

z = float(y)
print(y, type(y))
print(z, type(z))

"""### Injeção de valores em strings"""

x = 10

print(f'x = {x}')
print(f'x = {x:5d}')
print(f'x = {x:05d}')

y = 13 / 40.23

print(f'y = {y}')
print(f'y = {y:.2f}')

"""## Operadores

### Operadores Aritméticos

| Operador | Descrição       |
|:--------:|-----------------|
| `+`      | Adição          |
| `-`      | Subtração       |
| `*`      | Multiplicação   |
| `/`      | Divisão real    |
| `//`     | Divisão inteira |
| `%`      | Resto           |
| `**`     | Potenciação     |
"""

x = 2 + 3
print(x)

x = 2 - 3
print(x)

x = 2 * 3
print(x)

x = 2 / 3
print(x)

x = 2 // 3
print(x)

x = 2 % 3
print(x)

x = 2 ** 3
print(x)

x = (2 - 3) * 4 ** 16
print(x)

x = 1 + 1 * 0
print(x)

"""### Operadores Relacionais

| Operador  | Descrição |
|:---------:|-----------|
| `==`      | Igualdade | 
| `!=`      | Diferença | 
| `>`       | Maior     | 
| `>=`      | Maior ou igual    | 
| `<`       | Menor     | 
| `<=`      | Menor ou igual    | 

### Operadores Lógicos

| Operador  | Descrição |
|:---------:|-----------|
| `or`      | ou lógico | 
| `and`     | e lógico  | 
| `not`     | negação   |

## Pacotes

A importação de pacotes pode ser realizada de três maneiras diferentes:

1. Importando o namespace:
```python
import random
```
1. Importando o namespace com outro nome:
```python
import random as rnd
```
1. Importando somente as funções que serão usadas:
```python
from random import randint
```
"""

import random

x = random.randint(1, 100)
print(x)

import random as rnd

x = rnd.randint(1, 100)
print(x)

from random import randint

x = randint(1, 100)
print(x)

"""## Estruturas de decisão

- `if`
- `if` / `else`
- `if` / `elif` / `else`
"""

x = randint(1, 100)

if x % 2 == 0:
    print(f'O numero {x} eh par')
else:
    print(f'O numero {x} eh impar')

x = randint(-100, 100)

if x > 0:
    print(f'O numero {x} eh positivo')
elif x < 0:
    print(f'O numero {x} eh negativo')
else:
    print(f'O numero {x} eh nulo')

x = randint(1, 100)

resultado = 'par' if x % 2 == 0 else 'ímpar'
print(f'O numero {x} eh {resultado}')

"""## Estruturas de repetição

- `for .. in`
- `while`

Para mudar o fluxo de execução de um laço podem ser usados os comandos:

- `continue`
- `break`
"""

# Imprime de 0 a 9
for i in range(10):
    print(i)

# Imprime de 5 a 9
for i in range(5, 10):
    print(i)

# Imprime de 5 a 20 de 3 em 3
for i in range(5, 20, 3):
    print(i)

lista_compras = ['banana', 'laranja', 'melancia', 'morango', 'abacaxi']

for item in lista_compras:
    print(item)

x = 0
while x < 10:
    print(x)
    x += 1

"""## Listas"""

lista = []
for i in range(10):
    lista.append(i)
print(lista)

lista = [i for i in range(10)]
print(lista)

lista = [0 for i in range(10)]
print(lista)

lista = [randint(1, 100) for i in range(10)]
print(lista)

# Adiciona um elemento ao final
lista.append(9999)
print(lista)

# Adiciona um elemento no inicio da lista
lista.insert(0, -9999)
print(lista)

# Remove um elemento do final da lista
lista.pop()
print(lista)

# Ordena a lista
lista.sort()
print(lista)

# Ordena em ordem descrescente
lista.sort(reverse=True)
print(lista)

# Quebra a lista em duas
sublista1 = lista[:5]
print(sublista1)

sublista2 = lista[5:9]
print(sublista2)

sublista3 = lista[5:]
print(sublista3)

# Acesso aos elementos
print(lista[2])
print(lista[-1]) # ultimo elemento

# Verifica se um elemento esta na lista
if 36 in lista:
    print('A lista possui o 36')

"""## Tuplas"""

tupla = (1, 2, 3)
print(tupla)

tupla[2] = 8

"""## Conjuntos"""

conjunto = {1, 2, 3, 3, 3, 4, 5}
print(conjunto)

conjunto = set([1, 2, 3, 3, 3, 4, 5])
print(conjunto)

"""## Dicionários"""

aluno = {
    'nome' : 'Joao',
    'matricula': 1234,
    'notas': [3, 4, 9]
}
print(aluno)

aluno['curso'] = 'Ciencia da Computacao'
print(aluno)

a = aluno['disciplinas'] # ERRO

a = aluno.get('disciplinas', 'Sem nome')
print(a)

"""## Classes"""

class Produto:
    """Representacao de um produto em estoque na loja. """
    
    def __init__(self, id = 0, nome = '', preco = 0, quantidade = 0):
        """Construtor da classe Produto."""
        
        # Todos os atributos sao publicos!
        #self.id = 0
        #self.nome = ''
        #self.preco = 0.0
        #self.qtde = 0
        
        # Declaracao de atributos protegidos
        #self._id = 0
        #self._nome = ''
        #self._preco = 0.0
        #self._qtde = 0
        
        # Declaracao de atributos privados
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__qtde = quantidade
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor.upper()
    
    @property
    def preco(self):
        return self.__preco
    
    def total(self):
        return self.__preco * self.__qtde
    
    def __str__(self):
        return f'| {self.id:04} | {self.__nome:15s} | {self.__preco:10.2f} |'

produto1 = Produto()
produto1.id = 1234
produto1.nome = 'Playstation 4'

print(produto1.id)
print(produto1.nome)

produto2 = Produto(2, 'Playstation 5')

print(produto2.id)
print(produto2.nome)

produto3 = Produto(id=7, 
                   preco=200.10, 
                   quantidade=10, 
                   nome='Joguinho')

print(produto3.id)
print(produto3.nome)

"""### Sobrecarga de operadores"""

class Ponto:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

p1 = Ponto(10, 3)
p2 = Ponto(2, 2)

p3 = p1 + p2

print(f'{p1} + {p2} = {p3}')

"""### Herança"""

class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
    
    def __str__(self):
        return f'{self._nome}: {self._salario:10.2f}'
        
class Programador(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario) # Chama o construtor da classe pai

zeh = Programador('Zeh', 3000)
print(zeh)

"""## Funções Lambda

Funções sem nome usadas pontualmente para alguma operação.
"""

soma = lambda x, y: x + y

print(soma(1, 2))

produtos = [
    Produto(1, 'camiseta', 12.99),
    Produto(2, 'calca', 23.99),
    Produto(3, 'bermuda', 13.99),
    Produto(4, 'luva', 3.99),
    Produto(5, 'furadeira', 439.99),
    Produto(6, 'oculos', 199.99),
]

for i in produtos:
    print(i)

produtos.sort(key=lambda x: x.nome)
for i in produtos:
    print(i)

produtos.sort(key=lambda x: x.preco)
for i in produtos:
    print(i)

produtos.sort(key=lambda x: x.preco, reverse=True)
for i in produtos:
    print(i)

"""## Referências bibliográficas

- [Apostila Python](https://www.ufsm.br/app/uploads/sites/679/2019/08/Apostila_Python_v_1.pdf)
"""
