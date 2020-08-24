% Exercicio 02

% FATOS
gato(tom).
rato(jerry).
passaro(piupiu).
minhoca(moli).

% REGRAS
animal(X) :- 
	gato(X).

animal(X) :- 
	rato(X).

animal(X) :- 
	passaro(X).

animal(X) :-
	minhoca(X).


gosta(X, Y) :-
	gato(X),
	passaro(Y).

gosta(X, Y) :-
	gato(X),
	rato(Y).

gosta(X, Y) :-
	passaro(X),
	minhoca(Y).

come(X, Y) :-
	gosta(X, Y).






