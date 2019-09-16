---
layout: page
---

# Torre de Hanói

A torre de Hanói é um problema matemático composto por uma base com três pinos e discos de diferentes tamanhos de diâmetros. O problema começa com os pinos em uma torre de origem dispostos em ordem de tamanho, sendo o menor disco no topo. O objetivo é mover todos os discos do pino de origem até o pino de destino, obedecendo as seguintes regras:

- Somente um disco pode mover de cada vez.
- Cada movimento consiste em retirar o disco do topo de uma das torres e mover para outra.
- Nenhum disco pode ficar em cima de um disco menor.

{% include image.html url="/assets/trabalhos/hanoi.png" description="Configuração inicial da torre de Hanói." %}

Implemente algoritmos de busca cega e busca heurística para encontrar uma solução para este problema. O programa deverá receber o número de discos como entrada e imprimir os passos a serem executados para obter a solução.

Os seguintes algoritmos devem ser implementados:

- Busca em largura
- Busca em profundidade
- Busca de custo uniforme
- Busca gulosa
- A*

