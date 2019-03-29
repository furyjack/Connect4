import  unittest
from  board import  Board
class GameTest(unittest.TestCase):
    def testHeuristics(self):
        board_state = Board()
        board_state.state[0][0] = 0
        board_state.state[0][1] = 0
        board_state.state[0][2] = 0
        board_state.state[0][3] = 0
        board_state.state[1][0] = 1
        board_state.state[0][4] = 1
        board_state.state[0][6] = 1
        board_state.print_board()
        self.assertEqual(board_state.calc_score(0) + board_state.calc_score(1), 0)
        # board_state.state[0][0] = 1
        # board_state.state[0][3] = 0
        # board_state.print_board()
        # self.assertEqual(board_state.calc_score(0) + board_state.calc_score(1), -3999)
        # board_state.state[0][3] = 1
        # board_state.print_board()
        # self.assertEqual(board_state.calc_score(0) + board_state.calc_score(1), 0)
        # board_state.state[1][2] = 1
        # board_state._print()
        # self.assertEqual(board_state.calc_score(0) + board_state.calc_score(1), 1)
        # board_state.state[1][1] = 0
        # board_state._print()
        # self.assertEqual(board_state.calc_score(0) + board_state.calc_score(1), 0)
        print("Passed all tests")


    def checkWin(self):
        board_state = Board()
        board_state.state[0][0] = 0
        board_state.state[0][1] = 0
        board_state.state[0][2] = 0
        board_state.state[0][3] = 0
        board_state._print()
        self.assertEqual(board_state.check_win(0, 0,0), 1)
        self.assertEqual(board_state.check_win(0, 0, 1), 1)
        self.assertEqual(board_state.check_win(0, 0, 2), 1)
        self.assertEqual(board_state.check_win(0, 0, 3), 1)
        print("Passed all tests")

    def checkMinMax(self):
        game = Game()
        game.parse_rough_tree()
        #create_graph(game.root)
        self.assertEqual(game._minmax(game.root).val, 25)
        create_graph(game.root)

obj = GameTest()
obj.testHeuristics()