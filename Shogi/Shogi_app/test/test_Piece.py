from django.test import TestCase

from Shogi_app.Piece import Piece

class TestPiece(TestCase):
    def setUp(self):
        self.piece = Piece(7, 0, '9e')

    def test_side(self):
        self.assertEqual(self.piece.sign_side(), -1)

    def test_is_promote(self):
        self.assertEqual(self.piece.is_promote(), True)

    def test_promote(self):
        self.assertEqual(self.piece.promote(), False)

    def test_front_symbol(self):
        self.assertEqual(self.piece.get_front_symbol(), 'g')

    def test_symbol(self):
        self.assertEqual(self.piece.get_symbol(), 'G')

