from board import * 
import unittest

class BoardTests(unittest.TestCase):

	def setUp(self):
		self.b = Board()

	def test_empty_returns_0(self):
		self.assertEqual(self.b.GetWinner(), 0)

	def test_verticle_simple(self):
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_verticle_mixed(self):
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_verticle_mixed_no_win(self):
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.assertEqual(self.b.GetWinner(), 0)

	def test_horizontal_simple(self):
		self.b.Move(1, 2);
		self.b.Move(1, 3);
		self.b.Move(1, 4);
		self.b.Move(1, 5);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_horizontal_mixed(self):
		self.b.Move(1, 0);
		self.b.Move(2, 2);
		self.b.Move(2, 3);
		self.b.Move(2, 4);
		self.b.Move(2, 5);
		self.b.Move(1, 5);
		self.assertEqual(self.b.GetWinner(), 2)

	def test_horizontal_mixed_no_win(self):
		self.b.Move(1, 0);
		self.b.Move(2, 2);
		self.b.Move(2, 3);
		self.b.Move(1, 4);
		self.b.Move(2, 5);
		self.b.Move(1, 5);
		self.assertEqual(self.b.GetWinner(), 0)

	def test_back_slash_main_diagnol(self):
		self.b.Move(1, 5);
		self.b.Move(2, 4);
		self.b.Move(1, 4);
		self.b.Move(1, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_back_slash_above_main_diagnol_above(self):
		self.b.Move(2, 5);
		self.b.Move(1, 5);
		self.b.Move(1, 4);
		self.b.Move(2, 4);
		self.b.Move(1, 4);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 3);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_back_slash_below_main_diagnol_above(self):
		self.b.Move(1, 3);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(1, 1);
		self.b.Move(1, 1);
		self.b.Move(1, 1);
		self.b.Move(2, 0);
		self.b.Move(1, 0);
		self.b.Move(2, 0);
		self.b.Move(1, 0);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_forward_slash_main_diagnol(self):
		self.b.Move(1, 0);
		self.b.Move(2, 1);
		self.b.Move(1, 1);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.assertEqual(self.b.GetWinner(), 1)


	def test_forward_slash_below_main_diagnol(self):
		self.b.Move(1, 1);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(1, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(2, 4);
		self.b.Move(2, 4);
		self.b.Move(2, 4);
		self.b.Move(1, 4);
		self.assertEqual(self.b.GetWinner(), 1)

	def test_forward_slash_above_main_diagnol(self):
		self.b.Move(1, 0);
		self.b.Move(2, 0);
		self.b.Move(2, 1);
		self.b.Move(1, 1);
		self.b.Move(2, 1);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(1, 2);
		self.b.Move(2, 2);
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.b.Move(1, 3);
		self.b.Move(2, 3);
		self.b.Move(2, 3);
		self.assertEqual(self.b.GetWinner(), 2)


if __name__ == '__main__':
	unittest.main()

