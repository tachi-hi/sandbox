% Based on "7 languages in 7 weeks"

valid([]).
valid([Head|Tail]) :- fd_all_different(Head), valid(Tail).

sudoku(Mat, Solution) :-
	Solution = Mat,
	fd_domain(Mat, 1, 4),
	Mat = [A, B, C, D,
	       E, F, G, H,
	       I, J, K, L,
	       M, N, O, P], 
	Row1 = [A, B, C, D],
	Row2 = [E, F, G, H],
	Row3 = [I, J, K, L],
	Row4 = [M, N, O, P],
	Col1 = [A, E, I, M],
	Col2 = [B, F, J, N],
	Col3 = [C, G, K, O],
	Col4 = [D, H, L, P],
	Sq1 = [A, B, E, F],
	Sq2 = [C, D, G, H],
	Sq3 = [I, J, M, N],
	Sq4 = [K, L, O, P],
	valid([Row1, Row2, Row3, Row4, Col1, Col2, Col3, Col4, Sq1, Sq2, Sq3, Sq4]).

sudokuSample(Solution) :- 
sudoku([1,_,4,_,
        2,_,_,_,
        _,_,_,3,
        _,2,_,_], Solution).
