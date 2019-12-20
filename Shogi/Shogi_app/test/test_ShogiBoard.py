from django.test import TestCase

from Shogi_app.ShogiBoard import Board

class TestShogiBoard(TestCase):
    def setUp(self):
        self.init = "8l/1l+R2P3/p2pBG1pp/kps1p4/Nn1P2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L w Sbgn3p 124"
        self.board = Board(self.init)
        
    def test_all(self):
        # do check mate 
        self.board.valid_move('7d')
        self.board.valid_move('p*')
        self.assertEqual(self.board.is_checkmate, False)
        # do eat piece 
        self.board.do_move('9d9e')
        self.assertEqual(self.board.output_usi(), '8l/1l+R2P3/p2pBG1pp/1ps1p4/kn1P2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L b Sbg2n3p 125')
        # do promote move
        self.board.do_move('4b4a+')
        self.assertEqual(self.board.output_usi(), '5+P2l/1l+R6/p2pBG1pp/1ps1p4/kn1P2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L w Sbg2n3p 126')
        # do put piece 
        self.board.do_move('B*9a')
        self.assertEqual(self.board.output_territory(), 'GBBBBGBGG/GBGBBBBBG/GWBBGGBGG/WGBBGBBGW/BGBWGBGBB/WBGBGGBWG/BGWBBGWWG/BGGWWWWGG/GGBBGWWWW')
        self.assertEqual(self.board.output_usi(), 'b4+P2l/1l+R6/p2pBG1pp/1ps1p4/kn1P2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L b Sg2n3p 127')
        # do simple move
        self.board.do_move('1f1g')
        self.assertEqual(self.board.output_usi(), 'b4+P2l/1l+R6/p2pBG1pp/1ps1p4/kn1P2G2/P1P1P2P1/1PS5P/1KSG3+r1/LN2+p3L w Sg2n3p 128')
