---
layout: page
---

# Otimização

Uma empresa fabrica dois produtos: patinetes e monociclos. O lucro unitário dos patinetes é de \\$ 1.000,00 e dos monociclos é de \\$ 1.800,00. A empresa precisa de 20h para fabricar uma unidade de patinete e 30h para fabricar uma unidade de monociclo. O tempo anual para produção destes produtos é de 1.200h. A demanda esperada para cada unidade é de 40 unidade de patinetes e 30 unidade de monociclos. Qual é o plano de produção para que a empresa maximize o seu lucro nestes itens?

**Variáveis:**
- $p$: quantidade de patinetes
- $m$: quantidade de monociclos

**Restrições:**
- $20p + 30m \le 1200$
- $p \le 40$
- $m \le 30$
- $p, m \ge 0$

**Objetivo:** maximizar o lucro
- $L = 1000p + 1800m$

Implemente algoritmos de **busca local** para encontrar uma solução para este problema. Os algoritmos devem informar quais são as quantidades de patinetes e monociclos a serem produzidos para maximizar o lucro.

**Dois** dos seguintes algoritmos devem ser implementados:

- Hill climbing
- Busca Tabu
- Simulated Annealing

