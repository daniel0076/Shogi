'''
This file define the symbols and colors of the pieces and the relation 
about their promotion  
'''
DEFAULT_USI = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1"
COLORS = [b, w] = range(2)
COLORS_OUT = ['b', 'w']
SYMBOLS = [NONE, P, N, L, B, R, G, S, K, PRO_P, PRO_N, PRO_L, PRO_B, 
        PRO_R, PRO_S] = range(15)
PIECE_SYMBOLS = ['', 'p', 'n', 'l', 'b', 'r', 'g', 's', 'k', 
        '+p', '+n', '+l', '+b', '+r', '+s'] 
PROMOTED_PIECE = [NONE, P, N, L, B, R, G, S, K, P, N, L, B, R, S]
PIECE_PROMOTE = [NONE, PRO_P, PRO_N, PRO_L, PRO_B, PRO_R, NONE, 
        PRO_S, NONE, NONE, NONE, NONE, NONE, NONE, NONE] 
