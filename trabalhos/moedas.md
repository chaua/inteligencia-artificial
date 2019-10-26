---
layout: page
---

# Problema das moedas[^1]

São dados os seguintes elementos do domínio do problema:

- há 12 moedas de aparência visual idêntica;
- cada uma das 12 moedas está disposta em uma ordem inicial de apresentação;
- 11 delas tem o mesmo peso;
- 1 delas tem peso diferente, podendo ser mais leve ou mais pesada;
- há uma balança convencional de dois pratos de equilíbrio bilateral disponível para uso.

A descrição geral do que constitui a solução automática de uma instância de problema qualquer no domínio apresentado acima significa determinar, com a simulação de no máximo de 3 (três) utilizações da balança, as seguintes informações:

1. a posição inicial da moeda diferente;
2. o peso relativo da moeda diferente (se é mais leve ou mais pesada).

Implemente um programa em linguagem Prolog capaz de resolver instâncias de problema nesse domínio. O programa deve computar a solução por meio da simulação de uso da balança. A ativação do resolvedor deve ocorrer por meio do predicado ternário `moeda_diferente`. Ele deve permitir a instanciação da posição e do peso relativo ("Mais pesada" ou "Mais leve") da moeda diferente a partir de uma lista dinâmica com 12 valores inteiros positivos representando os pesos absolutos de cada uma
das 12 moedas. 

Para exemplificar o comportamento do predicado `moeda_diferente`, veja o que segue:

```
?- moeda_diferente([2,2,2,2,3,2,2,2,2,2,2,2], Posicao, Peso).
Posicao= 5
Peso= Mais pesada ?no
yes
```

[^1]: [Problema adaptado](http://www.inf.ufpr.br/alexd/ia/T1_IA_2015_2.pdf)