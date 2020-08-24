% fatorial.pl


% Base

fatorial(0, 1).

% Recursao

fatorial(X, FatX) :-
	Y is X - 1,
	fatorial(Y, FatY),
	FatX is X * FatY,
	!.	

