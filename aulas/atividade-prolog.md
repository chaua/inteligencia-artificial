---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: false
---

# Atividade Prolog

## Exercício 1

Considere um pequeno sistema de conhecimento sobre pessoas, animais e preferências alimentares.

João tem um pássaro.\
Pedro tem um peixe.\
Maria tem uma minhoca.\
Tom é um gato.\
Tom é meu gato.\
Eu sou uma pessoa.\
Eu sou amigo de Tom.

Todo pássaro gosta de minhocas.\
Todo gato gosta de peixes.\
Todo gato gosta de pássaros.\
Uma pessoa gosta de seus amigos.\
Uma pessoa também é considerada amiga de quem é seu amigo.\
Tom come tudo aquilo de que gosta, exceto pessoas.

Represente essas informações em Prolog, criando fatos e regras que permitam consultar:

1. Quais animais cada pessoa possui.
2. Do que cada animal gosta.
3. Quem é amigo de quem.
4. O que Tom pode comer.

## Exercício 2

Considere as seguintes pessoas e características:

Cássia é artista e gosta de música.\
Marcos é programador e gosta de tecnologia.\
Ana é pesquisadora e gosta de ciência.\
Fabiano é atleta e gosta de esportes.\
Sílvio é professor e gosta de literatura.

Uma pessoa pode gostar de outra quando ambas compartilham algum interesse.\
Uma pessoa é considerada feliz quando gosta de alguém que também gosta dela.

Represente essas informações em Prolog e crie regras para determinar:

1. Quem gosta de quem.
2. Quem é feliz.

## Exercício 3

Considere uma base de conhecimento sobre jogadores, jogos e equipes de criação de conteúdo.

João joga **League of Legends**.\
Maria joga **League of Legends**.\
Joel joga **Fortnite**.\
Joel também joga **Minecraft**.

João participa da equipe **Dragões Digitais**.\
Maria participa da equipe **Dragões Digitais**.\
Joel participa da equipe **Pixel Masters**.

Carlos é treinador de **League of Legends**.\
Ana Paula é treinadora de **Minecraft**.\
Pedro é treinador de **Fortnite**.

Pedro trabalha com a equipe **Pixel Masters**.\
Ana Paula trabalha com a equipe **Dragões Digitais**.\
Carlos trabalha com a equipe **Dragões Digitais**.

Represente essas informações em Prolog e crie regras que permitam consultar:

1. Quais jogadores são treinados por determinado treinador.
2. Quais pessoas estão associadas a determinada equipe.
3. Quais jogos cada jogador joga.
4. Quais treinadores trabalham em determinada equipe.

## Exercício 4

Considere uma base de conhecimento sobre as notas finais de estudantes em uma disciplina.

João tirou nota 5,0.\
Maria tirou nota 6,0.\
Joana tirou nota 8,0.\
Mariana tirou nota 9,0.\
Cleuza tirou nota 8,5.\
José tirou nota 6,5.\
Joaquim tirou nota 4,5.\
Mara tirou nota 4,0.\
Mary tirou nota 10,0.

Crie uma regra em Prolog para classificar a situação de cada estudante de acordo com sua nota final.

Estudantes com nota igual ou maior que 7,0 são considerados **aprovados**.\
Estudantes com nota igual ou maior que 5,0 e menor que 7,0 ficam em **recuperação**.\
Estudantes com nota menor que 5,0 são considerados **reprovados**.

Represente essas informações em Prolog e crie uma regra que permita responder às seguintes perguntas:

1. Qual é a situação da Joana??- situacao(joana, X).
2. Qual é a situação do Joaquim?
3. Quais estudantes foram aprovados?
4. Quais estudantes ficaram em recuperação?
5. Quais estudantes foram reprovados?



