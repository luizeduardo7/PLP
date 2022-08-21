nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(mariana,9.0).
nota(cleuza,8.5).
nota(jose,6.5).
nota(jaoquim,4.5).
nota(mara,4.0).
nota(mary,10.0).

    
verify_student(X):-
    nota(X, A),
    A >= 0,
  	A =< 4.9,
    write('Reprovado').

verify_student(X):-
    nota(X, A),
    A >= 5.0,
  	A =< 6.9,
	write('Recuperação').

verify_student(X):-
    nota(X, A),
    A >= 7.0,
  	A =< 10.0,
	write('Aprovado').