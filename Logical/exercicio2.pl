remove([X|L],X,L).
remove([X1|L1],X,[X1|L2]):-
    remove(L1,X,L2).