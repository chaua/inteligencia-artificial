% Listas Dinamicas em Prolog

% [a, b, c, d, [e, f]]
% partes_de(lataria, [paralamas, portas, capo, porta_malas])
% [Cabeca | Cauda]
% [Primeiro | Resto]

% Numero de elementos
% num_elementos(Lista, Numero) 

num_elementos([], 0).

num_elementos([C | R], N) :-
	num_elementos(R, NR),
	N is NR + 1,
	!.

% Somatoria dos elementos de uma lista

somatoria([], 0).

somatoria([C | R], S) :-
	somatoria(R, SR),
	S is SR + C,
	!.

% Media dos valores de uma lista

media([], 0).

media(Lista, Media) :-
	num_elementos(Lista, N),
	somatoria(Lista, S),
	Media is S / N,
	!.


% Concatena duas listas
% concatenadas(L1, L2, L3). => L3 = L1 + L2

concatenadas([], L, L).

concatenadas([C | R], L2, [C | R2]) :-
	concatenadas(R, L2, R2),
	!.

% Pertence a
% pertence_a(Item, Lista).
% pertence_a(4, [1, 2, 3, 4]).

pertence_a(X, [X | _]).

pertence_a(X, [_, Cauda]) :-
	pertence_a(X, Cauda).

% Listificada: listifica todos os elementos da lista
% listificada([a, b], Y).
% Y = [[a], [b]].

listificada([], []).

listificada([X | Cauda1], [[X] | Cauda2]) :-
	listificada(Cauda1, Cauda2).














