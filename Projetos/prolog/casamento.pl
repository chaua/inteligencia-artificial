% -- Exercicio - Casamento --

mulher(cassia).
mulher(ana).

homem(marcos).
homem(fabiano).
homem(silvio).

rico(marcos).
rico(ana).

bonito(marcos).
bonito(cassia).
bonito(fabiano).

forte(ana).
forte(fabiano).
forte(silvio).

amavel(silvio).

gosta(X, Y) :- 
	homem(X),
	mulher(Y),
	bonita(Y).

gosta(ana, X) :-
	homem(X),
	gosta(X, ana).

gosta(cassia, X) :-
	homem(X),
	amavel(X),
	rico(X).

gosta(cassia, X) :-
	homem(X),
	bonito(X),
	forte(X).

feliz(X) :-
	homem(X),
	rico(X).

feliz(X) :-
	homem(X),
	mulher(Y),
	gosta(X, Y),
	gosta(Y, X).

feliz(X) :-
	mulher(X),
	homem(Y),
	gosta(X, Y),
	gosta(Y, X).






