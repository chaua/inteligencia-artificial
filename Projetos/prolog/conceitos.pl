% -- CONCEITOS DE PROLOG --

% VARIAVEIS
% Sao lacunas de memoria que podem ou nao ser instanciadas 
% durante os ciclos do interpretador

% Sintaxe: variaveis sao todos os nomes iniciados por letra
% maiuscula
% Exemplo: X, Y, L, Nome, Arquivo

% CONSTANTES
% Sao porcoes fixas de memoria que armazenam valores

% Sintaxe: qualquer nomem iniciado por letra minuscula, entre aspas simples, ou que seja numerica
% Exemplo: x, y, nome, 'Nome'

% ESTRUTURAS - PREDICADOS
% Sao elementos que quando processados retornam um valor verdade

% Sintaxe: qualquer nome iniciado por maiusculo, minusculo, 
% simbolos especiais seguidos de parenteses
% Exemplo: livro('Inteligencia Artificial'), autor('Elaine', 'Rich')

% --- FATOS ---

homem(jose).
homem(mario).
homem(alberto).
homem(fabricio).
homem(joao).
homem(jonatas).
homem(marcos).

mulher(claudia).
mulher(silvia).
mulher(gertrudes).
mulher(ana).
mulher(marcia).

pai(joao, jose).
pai(joao, marcia).

pai(alberto, joao).
pai(fabricio, alberto).
pai(jonatas, fabricio).

mae(silvia, jose).
mae(silvia, marcia).

% REGRAS DE INFERENCIA

irmao(X, Y) :- 
	homem(X),
	pai(P, X),
	pai(P, Y),
	mae(M, X),
	mae(M, Y),
	not(X = Y).

irma(X, Y) :- 
	mulher(X),
	pai(P, X),
	pai(P, Y),
	mae(M, X),
	mae(M, Y),
	not(X = Y).

%gerou(X, Y) :-
%	pai(X, Y);
%	mae(X, Y).

gerou(X, Y) :-
	pai(X, Y).

gerou(X, Y) :-
	mae(X, Y).

ancestral(X, Y) :-
	gerou(X, Y).

ancestral(X, Y) :-
	gerou(A, Y),
	ancestral(X, A).





animal(gato).
animal(cachorro).

% Retorna todos os homens cadastrados na base
% listing(homem).

























